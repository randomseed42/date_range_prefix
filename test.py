import inspect
from datetime import datetime
from date_range_prefix import date_range_prefix
import unittest


def get_func_name():
    return inspect.getouterframes(inspect.currentframe())[1].function


class TestDateRange(unittest.TestCase):
    CASES = {
        'test_1': {'type': 'assertEqual', 'kw': {'start':None, 'end':None}, 'res': [datetime.today().strftime('%Y/%m/%d')]},
        'test_2': {'type': 'assertEqual', 'kw': {'start':'2021-01-05', 'end':None}, 'res': ['2021/01/05']},
        'test_3': {'type': 'assertEqual', 'kw': {'start':'2021-01-05', 'end':'2021-01-07'}, 'res': ['2021/01/05', '2021/01/06', '2021/01/07']},
        'test_4': {'type': 'assertEqual', 'kw': {'start':'2021-01-01', 'end':'2021-01-31'}, 'res': ['2021/01']},
        'test_5': {'type': 'assertEqual', 'kw': {'start':'2021-01-31', 'end':'2021-02-01'}, 'res': ['2021/01/31', '2021/02/01']},
        'test_6': {'type': 'assertEqual', 'kw': {'start':'2021-01-31', 'end':'2021-02-28'}, 'res': ['2021/01/31', '2021/02']},
        'test_7': {'type': 'assertEqual', 'kw': {'start':'2021-01-31', 'end':'2021-03-01'}, 'res': ['2021/01/31', '2021/02', '2021/03/01']},
        'test_8': {'type': 'assertEqual', 'kw': {'start':'2021-01-01', 'end':'2021-03-01'}, 'res': ['2021/01', '2021/02', '2021/03/01']},
        'test_9': {'type': 'assertEqual', 'kw': {'start':'2021-11-30', 'end':'2022-01-01'}, 'res': ['2021/11/30', '2021/12', '2022/01/01']},
        'test_10': {'type': 'assertEqual', 'kw': {'start':'2021-11-30', 'end':'2023-01-01'}, 'res': ['2021/11/30', '2021/12', '2022', '2023/01/01']},
        'test_11': {'type': 'assertEqual', 'kw': {'start':'2021-01-01', 'end':'2021-12-31'}, 'res': ['2021']},
        'test_12': {'type': 'assertEqual', 'kw': {'start':'2021-01-01', 'end':'2022-01-01'}, 'res': ['2021', '2022/01/01']},
    }

    def test_1(self):
        case = self.CASES.get(get_func_name())
        getattr(self, case['type'])(date_range_prefix(**case['kw']), case['res'])
    
    def test_2(self):
        case = self.CASES.get(get_func_name())
        getattr(self, case['type'])(date_range_prefix(**case['kw']), case['res'])

    def test_3(self):
        case = self.CASES.get(get_func_name())
        getattr(self, case['type'])(date_range_prefix(**case['kw']), case['res'])
    
    def test_4(self):
        case = self.CASES.get(get_func_name())
        getattr(self, case['type'])(date_range_prefix(**case['kw']), case['res'])
    
    def test_5(self):
        case = self.CASES.get(get_func_name())
        getattr(self, case['type'])(date_range_prefix(**case['kw']), case['res'])

    def test_6(self):
        case = self.CASES.get(get_func_name())
        getattr(self, case['type'])(date_range_prefix(**case['kw']), case['res'])
    
    def test_7(self):
        case = self.CASES.get(get_func_name())
        getattr(self, case['type'])(date_range_prefix(**case['kw']), case['res'])

    def test_8(self):
        case = self.CASES.get(get_func_name())
        getattr(self, case['type'])(date_range_prefix(**case['kw']), case['res'])
    
    def test_9(self):
        case = self.CASES.get(get_func_name())
        getattr(self, case['type'])(date_range_prefix(**case['kw']), case['res'])
    
    def test_10(self):
        case = self.CASES.get(get_func_name())
        getattr(self, case['type'])(date_range_prefix(**case['kw']), case['res'])
    
    def test_11(self):
        case = self.CASES.get(get_func_name())
        getattr(self, case['type'])(date_range_prefix(**case['kw']), case['res'])
    
    def test_12(self):
        case = self.CASES.get(get_func_name())
        getattr(self, case['type'])(date_range_prefix(**case['kw']), case['res'])

    def test_err_1(self):
        self.assertRaises(AssertionError, date_range_prefix, start='2022-02-01', end='2022-01-01')

    def test_err_2(self):
        self.assertRaisesRegex(ValueError, 'day is out of range for month', date_range_prefix, start='2021-02-01', end='2021-02-29')


if __name__ == '__main__':
    unittest.main()
    