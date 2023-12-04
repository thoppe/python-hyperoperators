from functools import reduce

_errmsg_non_integral = "{} is not an integer, required for hyperop n≥4"
_errmsg_invalid_hyperop_n = "hyperoperators must be integers n>=0, " "created with n={}"

# Define the base of the recursion, H0 the successor function
# essentially for foldr to work, a (not b) must be ignored.


class base_hyperop0(object):
    def __call__(self, a, b):
        return 1 + b


# For convenience & speed define the lower hyperops


class base_hyperop1(object):
    def __call__(self, a, b, customFunction=None):
        if not customFunction:
            return a + b
        else:
            return customFunction(a, b)


class base_hyperop2(object):
    def __call__(self, a, b, customFunction=None):
        if not customFunction:
            return a * b
        else:
            return customFunction(a, b)


class base_hyperop3(object):
    def __call__(self, a, b, customFunction=None):
        if not customFunction:
            return a ** b
        else:
            return customFunction(a, b)


class hyperop(object):
    def __new__(cls, n, primitive=False, **kwargs):
        if n < 0 or int(n) != n:
            raise ValueError(_errmsg_invalid_hyperop_n.format(n))

        if n == 0:
            return base_hyperop0()

        if not primitive:
            if n == 1:
                return base_hyperop1(**kwargs)
            if n == 2:
                return base_hyperop2(**kwargs)
            if n == 3:
                return base_hyperop3(**kwargs)

        return object.__new__(cls)

    def __init__(self, n, customFunction=None, primitive=False):
        """
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
        """
        self.n = n
        if not customFunction:
            self.lower = hyperop(n - 1)
        else:
            assert hasattr(customFunction, "__call__"), "Object not a callable/function"
            self.lower = hyperop(n - 1, customFunction=customFunction)

    def _repeat(self, a, b):
        """
        Repeat is need to not overflow [a,]*b
        xrange can't handle large nums see,
        http://stackoverflow.com/a/22114284/249341
        """

        # For successor to work properly the base case
        # needs to be incremented by one
        if self.n == 1:
            yield a

        i = 1
        while True:
            yield a
            if i == b:
                break
            i += 1

    def __call__(self, a, b):
        """
        Evaluate and return expression H[n](a,b).
        (a,b) must be non-negative for n>4.
        """
        check = self._check_value(a, b)
        if check is not None:
            return check

        # Apply foldr
        return reduce(lambda x, y: self.lower(y, x), self._repeat(a, b))

    def _check_value(self, a, b):
        """
        H[n>5](a,b) both a,b must be integers.
        H[n=4](a,b) b must be and integer.
        check input values and raise Exception if they don't pass.

        If H[n](a,b) is a special case return that value instead of None
        """
        if self.n <= 3:
            return None

        # Special case for n>=4 and b=0
        if b == 0:
            return 1

        if b != int(b):
            raise ValueError(_errmsg_non_integral.format(b))

        if self.n <= 4:
            return None

        if a != int(a):
            raise ValueError(_errmsg_non_integral.format(a))

        return None


class bounded_hyperop(hyperop):

    infinity = float("inf")

    def __init__(self, n, bound=1000, **kwargs):
        """
        Create a bounded hyperoperator of order n.

        If n>=4, then if the intermediate result is larger than bound
        the result will be returned as infinite.
        """
        self.n = n
        self.lower = bounded_hyperop(n - 1)
        self.bound = bound

    def __call__(self, a, b):
        """
        Evaluate and return expression H[n](a,b).
        (a,b) must be non-negative for n>4.

        If the intermediate result is larger than the inital bound
        infinity will be returned.
        """
        check = self._check_value(a, b)
        if check is not None:
            return check

        vals = self._repeat(a, b)

        try:
            x = self.lower(next(vals), next(vals))
        except StopIteration:
            x = a

        if abs(x) > self.bound:
            return self.infinity

        for y in vals:
            x = self.lower(y, x)

            if abs(x) > self.bound:
                return self.infinity

        return x
