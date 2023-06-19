from datetime import datetime
from date_range_prefix import date_range_prefix

import unittest as ut


class TestDateRange(ut.TestCase):
    CASES = {
        'test_01': {'type': 'assertEqual', 'kw': {'start': None, 'end': None}, 'res': [datetime.today().strftime('%Y/%m/%d')]},
        'test_02': {'type': 'assertEqual', 'kw': {'start': '2021-01-05', 'end': None}, 'res': ['2021/01/05']},
        'test_03': {'type': 'assertEqual', 'kw': {'start': '2021-01-05', 'end': '2021-01-07'}, 'res': ['2021/01/05', '2021/01/06', '2021/01/07']},
        'test_04': {'type': 'assertEqual', 'kw': {'start': '2021-01-01', 'end': '2021-01-31'}, 'res': ['2021/01']},
        'test_05': {'type': 'assertEqual', 'kw': {'start': '2021-01-31', 'end': '2021-02-01'}, 'res': ['2021/01/31', '2021/02/01']},
        'test_06': {'type': 'assertEqual', 'kw': {'start': '2021-01-31', 'end': '2021-02-28'}, 'res': ['2021/01/31', '2021/02']},
        'test_07': {'type': 'assertEqual', 'kw': {'start': '2021-01-31', 'end': '2021-03-01'}, 'res': ['2021/01/31', '2021/02', '2021/03/01']},
        'test_08': {'type': 'assertEqual', 'kw': {'start': '2021-01-01', 'end': '2021-03-01'}, 'res': ['2021/01', '2021/02', '2021/03/01']},
        'test_09': {'type': 'assertEqual', 'kw': {'start': '2021-11-30', 'end': '2022-01-01'}, 'res': ['2021/11/30', '2021/12', '2022/01/01']},
        'test_10': {'type': 'assertEqual', 'kw': {'start': '2021-11-30', 'end': '2023-01-01'}, 'res': ['2021/11/30', '2021/12', '2022', '2023/01/01']},
        'test_11': {'type': 'assertEqual', 'kw': {'start': '2021-01-01', 'end': '2021-12-31'}, 'res': ['2021']},
        'test_12': {'type': 'assertEqual', 'kw': {'start': '2021-01-01', 'end': '2022-01-01'}, 'res': ['2021', '2022/01/01']},
    }

    def test(self):
        for case in self.CASES.values():
            getattr(self, case['type'])(date_range_prefix(**case['kw']), case['res'])

    def test_err_1(self):
        self.assertRaises(ValueError, date_range_prefix, start='2022-02-01', end='2022-01-01')

    def test_err_2(self):
        self.assertRaisesRegex(ValueError, 'day is out of range for month', date_range_prefix, start='2021-02-01', end='2021-02-29')


if __name__ == '__main__':
    ut.main()
