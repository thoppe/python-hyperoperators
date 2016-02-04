import unittest
from hyperop import hyperop

class KnownValues(unittest.TestCase):

    def test_H4(self):
        H = hyperop(4)
        assert(H(3,3) == 7625597484987)

if __name__ == '__main__':
    unittest.main()

