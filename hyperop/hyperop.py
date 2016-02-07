_errmsg_non_integral = "{} is not integral, required for hyperop n>4"
_errmsg_invalid_hyperop_n = "hyperoperators must be integers n>=0, created with n={}"

# Define the base of the recursion, H0 the successor function
# essentially for foldr to work, a (not b) must be ignored.
class base_hyperop0(object):
    def __call__(self,a,b):
        return 1 + b

# For convenience & speed define the lower hyperops
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
    
    def __new__(cls,n,primitive=False):
        if n<0 or int(n) != n:
            raise ValueError(_errmsg_invalid_hyperop_n.format(n))
        
        if n==0:  return base_hyperop0()

        if not primitive:
            if n==1:  return base_hyperop1()
            if n==2:  return base_hyperop2()
            if n==3:  return base_hyperop3()
            
        return object.__new__(cls)
    
    def __init__(self, n, primitive=False):
        '''
        Create a hyperoperator of order n. 

        n must be a non-negative integer.
        If primitive is True, evaluate everything from the successor 
        function, otherwise hardcode in base cases all 
        the way to exponentiation.

        Hyperoperation 0, H0 is the successor function, H0(None, 4) = 5
        H1 is addition, H1(2,4) = 2 + (1+1+1+1) = 6
        H2 is multiplication (repeated addition), H2(2,4) = 2+2+2+2 = 8
        H3 is exponentiation (repeated multiplication), H3(2,4) = 2*2*2*2 = 16
        H4 is tetration H4(2,4) = 2^(2^(2^(2))) = 65536
        Hyperoperation n is repeated Hyperoperation (n-1)

        Evaluate the hyperoperator by calling it:
        H3 = hyperop(3)
        print H3(2,5)
        >> 32
        '''
        self.n = n
        self.lower = hyperop(n-1)

    def _repeat(self,a,b):
        '''
        Repeat is need to not overflow [a,]*b
        xrange can't handle large nums see,
        http://stackoverflow.com/a/22114284/249341
        '''

        # For successor to work properly the base case
        # needs to be incremented by one
        if self.n == 1:
            yield a

        i = 1
        while True:
            yield a
            if i==b: break
            i += 1
   
    def __call__(self,a,b):
        '''
        Evaluate and return expression H[n](a,b).
        (a,b) must be non-negative for n>4.
        '''       
        self._check_value(a,b)
        # Apply foldr
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
