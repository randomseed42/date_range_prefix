from datetime import datetime
from calendar import monthrange
from typing import List, Literal, Optional


def month_days(year: int, month: int) -> int:
    """
    Get how many days in the month of the year.

    Parameters
    ----------
    year : int
        Integer of the year
    month : int
        Integer of the month

    Returns
    -------
    int
        Integer of how many days in the month of the year
    """
    return monthrange(year, month)[1]


def is_month_last_day(date: datetime) -> bool:
    """
    Check if date is the last day of that month.

    Parameters
    ----------
    date: datetime
        Date to be checked

    Returns
    -------
    bool
        True if it is the last day of that month, else False
    """
    return date.day == month_days(date.year, date.month)


def date_range_prefix(
        start: Optional[str] = None,
        end: Optional[str] = None,
        input_delimiter: Literal['-', '/'] = '-',
        output_delimiter: Literal['-', '/'] = '/',
) -> List[str]:
    """
    By given the start date and end date,
    get list of all dates in between them,
    each date is in string format %Y/%m/%d,
    compress full month to %Y/%m,
    compress full year to %Y

    For example:

    >>> date_range_prefix(start='2023-01-30', end='2023-03-01')
    ['2023/01/30', '2023/01/31', '2023/02', '2023/03/01']

    >>> date_range_prefix(start='2023/01/01', end='2023/03/31', input_delimiter='/', output_delimiter='-')
    ['2023-01', '2023-02', '2023-03']

    >>> date_range_prefix(start='2021-01-01', end='2021-12-31')
    ['2021']

    >>> date_range_prefix(start='2021-02-10')
    ['2021/02/10']

    >>> date_range_prefix()
    ['2023/06/17']

    Parameters
    ----------
    start : str
        start date in string format, like %Y-%m-%d
    end : str
        end date in string format, like %Y-%m-%d
    input_delimiter : Literal['-', '/'], default '-'
        input start date and end date delimiter
    output_delimiter : Literal['-', '/'], default '/'
        output date prefixes delimiter

    Returns
    -------
    list
        List of date prefixes.
        Each prefix is in string format, like %Y/%m/%d, or %Y/%m, or %Y.

    """

    input_format = f'%Y{input_delimiter}%m{input_delimiter}%d'

    if start is None:
        start = datetime.today().strftime(input_format)
    if end is None:
        end = start

    start_date = datetime.strptime(start, input_format)
    end_date = datetime.strptime(end, input_format)

    if end_date < start_date:
        raise ValueError('end should be no earlier than start')

    prefixes = []

    if start_date.year == end_date.year:  # same year for start and end
        if start_date.month == end_date.month:  # same month for start and end
            if start_date.day == 1 and is_month_last_day(end_date):  # full month from start to end
                prefixes += [f'{start_date.year}{output_delimiter}{start_date.month:02d}']
            else:  # not full month, so list every day
                days = range(start_date.day, end_date.day + 1)
                prefixes += [f'{start_date.year}{output_delimiter}{end_date.month:02d}{output_delimiter}{day:02d}'
                             for day in days]
        elif start_date.month == 1 and start_date.day == 1 and end_date.month == 12 and end_date.day == 31:  # full year
            prefixes += [f'{start_date.year}']
        else:  # same year but across multiple months
            # get start month prefixes
            start_month_last_date = datetime(start_date.year,
                                             start_date.month,
                                             month_days(start_date.year, start_date.month)
                                             ).strftime(input_format)
            prefixes += date_range_prefix(start=start, end=start_month_last_date)

            # get full months prefixes in between start and end
            if end_date.month > start_date.month + 1:
                months = range(start_date.month + 1, end_date.month)
                prefixes += [f'{start_date.year}{output_delimiter}{month:02d}' for month in months]

            # get end month prefixes
            end_month_first_date = datetime(end_date.year, end_date.month, 1).strftime(input_format)
            prefixes += date_range_prefix(start=end_month_first_date, end=end)
    else:  # if start and end across multiple years
        # get start year prefixes
        start_year_last_date = datetime(start_date.year, 12, 31).strftime(input_format)
        prefixes += date_range_prefix(start=start, end=start_year_last_date)

        # get full years prefixes in between start and end
        if end_date.year > start_date.year + 1:
            years = range(start_date.year + 1, end_date.year)
            prefixes += [f'{year}' for year in years]

        # get end year prefixes
        end_year_first_date = datetime(end_date.year, 1, 1).strftime(input_format)
        prefixes += date_range_prefix(start=end_year_first_date, end=end)
    return prefixes
