import unittest, itertools, math, operator
from hyperop import hyperop

testing_values = range(1,15)

def check_range(fA, fB):
    for x,y in itertools.product(testing_values,repeat=2):
        assert( fA(x,y) == fB(x,y) )

class PrimitiveSmallValues(unittest.TestCase):

    def test_primitive_H1(self):
        check_range(hyperop(1,primitive=True), operator.add)

    def test_primitive_H2(self):
        check_range(hyperop(2,primitive=True), operator.mul)

    def test_primitive_H3(self):
        check_range(hyperop(3,primitive=True), operator.pow)
        

class SmallValues(unittest.TestCase):

    def test_H0(self):
        successor = lambda a,b: 1+b
        check_range(hyperop(0), successor)
    
    def test_H1(self):
        check_range(hyperop(1), operator.add)
            
    def test_H2(self):
        check_range(hyperop(2), operator.mul)

    def test_H3(self):
        check_range(hyperop(3), operator.pow)

class KnownValues(unittest.TestCase):
    def test_H4(self):
        H = hyperop(4)

        # Small fixed values, a=2
        assert(H(2,1) == 2)
        assert(H(2,2) == 4)
        assert(H(2,3) == 16)
        assert(H(2,4) == 65536)

        # Small fixed values, a=3
        assert(H(3,1) == 3)
        assert(H(3,2) == 27)
        assert(H(3,3) == 7625597484987)

        # Log of large value should be related to smaller one
        a2_5 = round(math.log(H(2,5),2))
        assert(a2_5 == H(2,4))

    def test_H5(self):
        H = hyperop(5)

        # Small fixed values, a=2
        assert(H(2,1) == 2)
        assert(H(2,2) == 4)
        assert(H(2,3) == 65536)

        # Small fixed values, a=3
        assert(H(3,1) == 3)
        assert(H(3,2) == 7625597484987)

class ValidRanges(unittest.TestCase):
    def test_non_integral_H5(self):
        H = hyperop(5)

        with self.assertRaises(ValueError):
            H(1.1,2)
        with self.assertRaises(ValueError):
            H(2,1.1)
        
    def test_non_integral_n(self):
        with self.assertRaises(ValueError):
            H = hyperop(1.2)

    def test_non_negative_n(self):
        with self.assertRaises(ValueError):
            H = hyperop(-1)        
        
if __name__ == '__main__':
    unittest.main()

