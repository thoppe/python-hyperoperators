import unittest, itertools, math
from hyperop import hyperop

testing_values = range(1,20)

class SmallValues(unittest.TestCase):
    
    def test_H1(self):
        H = hyperop(1)
        for a,b in itertools.product(testing_values,repeat=2):
            assert( H(a,b) == a+b )
            
    def test_H2(self):
        H = hyperop(2)
        for a,b in itertools.product(testing_values,repeat=2):
            assert( H(a,b) == a*b )

    def test_H3(self):
        H = hyperop(3)
        for a,b in itertools.product(testing_values,repeat=2):
            assert( H(a,b) == a**b )


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
        
if __name__ == '__main__':
    unittest.main()

