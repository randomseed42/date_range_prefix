from datetime import datetime
from date_range_prefix import date_range_prefix
import unittest


class TestDateRange(unittest.TestCase):

    def test_1(self):
        rng = date_range_prefix()
        self.assertEqual(rng, [datetime.today().strftime('%Y/%m/%d')])
    
    def test_2(self):
        rng = date_range_prefix(start='2022-02-26')
        self.assertEqual(rng, ['2022/02/26'])

    def test_3(self):
        rng = date_range_prefix(start='2022-02-26', end='2022-02-28')
        self.assertEqual(rng, ['2022/02/26', '2022/02/27', '2022/02/28'])
    
    def test_4(self):
        rng = date_range_prefix(start='2022-02-26', end='2022-03-02')
        self.assertEqual(rng, ['2022/02/26', '2022/02/27', '2022/02/28', '2022/03/01', '2022/03/02'])
    
    def test_5(self):
        rng = date_range_prefix(start='2022-02-26', end='2022-04-02')
        self.assertEqual(rng, ['2022/02/26', '2022/02/27', '2022/02/28', '2022/03', '2022/04/01', '2022/04/02'])

    def test_6(self):
        rng = date_range_prefix(start='2022-02-01', end='2022-04-02')
        self.assertEqual(rng, ['2022/02', '2022/03', '2022/04/01', '2022/04/02'])

if __name__ == '__main__':
    unittest.main()
    