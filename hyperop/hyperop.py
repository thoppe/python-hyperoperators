import itertools

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
        if n==1:  return base_hyperop1()
        if n==2:  return base_hyperop2()
        if n==3:  return base_hyperop3()
        return object.__new__(cls)
    
    def __init__(self, n):
        print "Building hyperop", n
        self.n = n
        self.lower = hyperop(n-1)

    # Repeat is need to not overflow [a,]*b
    # xrange can't handle large nums http://stackoverflow.com/a/22114284/249341
    def _repeat(self,a,b):
        for i in itertools.count(1):
            yield a
            if i==b: break
   
    def __call__(self,a,b): # Apply foldr
        vals = self._repeat(a,b)
        return reduce(lambda x,y: self.lower(y,x), vals)
