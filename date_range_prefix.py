from datetime import datetime
import calendar

def date_range_prefix(start=None, end=None):
    if isinstance(start, type(None)):
        start = datetime.today().strftime('%Y-%m-%d')
    if isinstance(end, type(None)):
        end = start

    s = datetime.strptime(start, '%Y-%m-%d')
    e = datetime.strptime(end, '%Y-%m-%d')

    assert e >= s

    rng = []

    if s.year == e.year:
        year = s.year
        if s.month == e.month:
            month = s.month
            if (s.day == 1) & (e.day == calendar.monthrange(year, month)[1]):
                rng += [f'{year}/{month:02d}']
            else:
                days = range(s.day, e.day+1)
                rng += [f'{year}/{month:02d}/{day:02d}' for day in days]
        else:
            _end = datetime(s.year, s.month, calendar.monthrange(s.year, s.month)[1]).strftime('%Y-%m-%d')
            rng += date_range_prefix(start=start, end=_end)
            
            if e.month - s.month > 1:
                rng += [f'{year}/{month:02d}' for month in range(s.month+1, e.month)]
            
            _start = datetime(e.year, e.month, 1).strftime('%Y-%m-%d')
            rng += date_range_prefix(start=_start, end=end)
    else:
        rng += date_range_prefix(start, f'{s.year}-12-31')

        if s.year != e.year:
            rng += [f'{year}' for year in range(s.year+1, e.year)]
        
        rng += date_range_prefix(f'{e.year}-01-01', end)
    return rng


if __name__ == '__main__':
    cases = [
        ('2021-01-15', '2021-01-25'),
        ('2021-01-15', '2021-02-25'),
        ('2021-01-15', '2021-03-25'),
        ('2021-01-01', '2021-01-01'),
        ('2021-01-01', '2021-01-31'),
        ('2021-01-01', '2021-02-01'),
        ('2021-01-01', '2021-02-05'),
        ('2021-01-01', '2021-02-28'),
        ('2021-01-01', '2021-03-31'),
        ('2021-12-29', '2022-01-05'),
        ('2021-12-29', '2023-01-05'),
        ('2021-12-19', '2023-02-28'),
    ]

    for case in cases:
        print(*case)
        print(date_range_prefix(*case), '\n')