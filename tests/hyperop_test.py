import unittest
import itertools
import math
import operator
from hyperop import hyperop, bounded_hyperop

testing_values = range(1, 15)


def check_range(fA, fB):
    for x, y in itertools.product(testing_values, repeat=2):
        assert fA(x, y) == fB(x, y)


class PrimitiveSmallValues(unittest.TestCase):

    def test_primitive_H1(self):
        check_range(hyperop(1, primitive=True), operator.add)

    def test_primitive_H2(self):
        check_range(hyperop(2, primitive=True), operator.mul)

    def test_primitive_H3(self):
        check_range(hyperop(3, primitive=True), operator.pow)


class SmallValues(unittest.TestCase):

    def test_H0(self):
        def successor(_, b):
            return 1 + b
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
        assert H(2, 1) == 2
        assert H(2, 2) == 4
        assert H(2, 3) == 16
        assert H(2, 4) == 65536

        # Small fixed values, a=3
        assert H(3, 1) == 3
        assert H(3, 2) == 27
        assert H(3, 3) == 7625597484987

        # Log of large value should be related to smaller one
        a2_5 = round(math.log(H(2, 5), 2))
        assert a2_5 == H(2, 4)

    def test_H5(self):
        H = hyperop(5)

        # Small fixed values, a=2
        assert H(2, 1) == 2
        assert H(2, 2) == 4
        assert H(2, 3) == 65536

        # Small fixed values, a=3
        assert H(3, 1) == 3
        assert H(3, 2) == 7625597484987


class ValidRanges(unittest.TestCase):

    def test_non_integral_H4(self):
        H = hyperop(4)

        with self.assertRaises(ValueError):
            H(2, 0.5)

    def test_non_integral_H5(self):
        H = hyperop(5)

        with self.assertRaises(ValueError):
            H(1.1, 2)
        with self.assertRaises(ValueError):
            H(2, 1.1)

    def test_non_integral_n(self):
        with self.assertRaises(ValueError):
            hyperop(1.2)

    def test_non_negative_n(self):
        with self.assertRaises(ValueError):
            hyperop(-1)


class BoundedHyperop(unittest.TestCase):

    def test_integer_bounds(self):
        H = bounded_hyperop(4, bound=1000)
        assert H(2, 5) == H.infinity

    def test_complex_bounds(self):
        H = bounded_hyperop(4, bound=1000)
        assert H(5.0, 5) == H.infinity

    def test_coorespondance(self):
        '''
        Check if the bounded hyperop matches with the regular
        version for small values of a,b.
        '''

        bound = hyperop(4)(3, 3)

        vals = range(1, 4)
        for N in range(0, 5):
            H = hyperop(N, primitive=True)
            Hb = bounded_hyperop(N, bound=bound, primitive=True)

            for a, b in itertools.product(vals, repeat=2):
                assert H(a, b) == Hb(a, b)


class SpecialCases(unittest.TestCase):

    def test_special_case_b0(self):

        H0 = dict([(n, hyperop(n)) for n in range(15)])
        Hb = dict([(n, bounded_hyperop(n)) for n in range(15)])

        for H in [H0, Hb]:

            for a in testing_values:
                assert H[0](a, 0) == 1
                assert H[1](a, 0) == a
                assert H[2](a, 0) == 0

                for n in range(3, 15):
                    assert H[n](a, 0) == 1

    def test_special_case_a0(self):

        H0 = dict([(n, hyperop(n)) for n in range(15)])
        Hb = dict([(n, bounded_hyperop(n)) for n in range(15)])

        for H in [H0, Hb]:

            for b in testing_values:
                assert H[0](0, b) == b + 1
                assert H[1](0, b) == b
                assert H[2](0, b) == 0
                assert H[3](0, b) == 0

                for n in range(4, 15):
                    assert H[n](0, b) == (b % 2 == 0)

if __name__ == '__main__':
    unittest.main()
