import unittest
from samplitude import samplitude as s8e

class TestSamplitudeConsumers(unittest.TestCase):

    def setUp(self):
        self.seed = 1729

    def asserts8e(self, template, expected):
        self.assertEqual(str(expected),
                         str(s8e(template, seed=self.seed)))

    def test_tojson(self):
        self.asserts8e("'HT' | choice | sample(6) | counter | tojson",
                       """\
{"H": 3, "T": 3}""")

    def test_max_min_sum_len(self):
        base = 'range(1, 101) | scale(range(100,0,-1))'
        self.asserts8e('%s | max' % base, "2550")
        self.asserts8e('%s | min' % base, "100")
        self.asserts8e('%s | sum' % base, "171700")
        self.asserts8e('%s | len' % base, "100")


    def test_gobbler(self):
        base = 'range(1, 101) | scale(range(100,0,-1))'
        self.asserts8e('%s | gobble' % base, "[]")


if __name__ == '__main__':
    unittest.main()
