import itertools

_errmsg_non_integral = "{} is not integral, required for hyperop n>4"
_errmsg_invalid_hyperop_n = "hyperoperators must be integers n>=0, created with n={}"

# For convenience  & speed define the lower hyperops
class base_hyperop1(object):
    def __call__(self,a,b):
        return a + b

class base_hyperop2(object):
    def __call__(self,a,b):
        return a * b

class base_hyperop3(object):
    def __call__(self,a,b):
        return a ** b

class hyperop(object):
    
    def __new__(cls,n):
        if n<0 or int(n) != n:
            raise ValueError(_errmsg_invalid_hyperop_n.format(n))

        if n==1:  return base_hyperop1()
        if n==2:  return base_hyperop2()
        if n==3:  return base_hyperop3()
        return object.__new__(cls)
    
    def __init__(self, n):
        self.n = n
        self.lower = hyperop(n-1)

    def _repeat(self,a,b):
        '''
        Repeat is need to not overflow [a,]*b
        xrange can't handle large nums see,
        http://stackoverflow.com/a/22114284/249341
        '''
        for i in itertools.count(1):
            yield a
            if i==b: break
   
    def __call__(self,a,b):
        '''
        Apply foldr
        '''
        self._check_value(a,b)
        return reduce(lambda x,y: self.lower(y,x), self._repeat(a,b))

    def _check_value(self,a,b):
        '''
        H5 and greater can't handle non-integer values, 
        check input values and raise Exception if they don't pass.
        '''
        
        if self.n < 5:
            return True

        if a != int(a):
            raise ValueError(_errmsg_non_integral.format(a))

        if b != int(b):
            raise ValueError(_errmsg_non_integral.format(b))
