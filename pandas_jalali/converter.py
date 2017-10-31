# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np


#: Minimum year supported by the library.
MINYEAR = 1

#: Maximum year supported by the library.
MAXYEAR = 3178


def get_julian_day_from_jalali_date(year, month, day):
    base = year - np.where(year >= 0, 474, 473)
    julian_year = 474 + (base % 2820)
    return day + np.where(month <= 7, (month - 1) * 31, ((month - 1) * 30) + 6) \
           + np.floor(((julian_year * 682) - 110) / 2816) \
           + (julian_year - 1) * 365 \
           + np.floor(base / 2820) * 1029983 + (1948320.5 - 1)


def get_gregorian_date_from_julian_day(jd):

    jdm = jd + 0.5
    z = np.floor(jdm)
    f = jdm - z

    alpha = np.floor((z - 1867216.25) / 36524.25)
    b = (z + 1 + alpha - np.floor(alpha / 4)) + 1524
    c = np.floor((b - 122.1) / 365.25)
    d = np.floor(365.25 * c)
    e = np.floor((b - d) / 30.6001)
    day = b - d - np.floor(30.6001 * e) + f

    m = np.where(e < 14, e - 1, np.where((e == 14) | (e == 15), e - 13, 0))
    y = np.where(m > 2, c - 4716, np.where((m == 1) | (m == 2), c - 4715, 0))

    return pd.Series(np.where(pd.isnull(jd), np.NaN, y)), \
           pd.Series(np.where(pd.isnull(jd), np.NaN, m)), \
           pd.Series(np.where(pd.isnull(jd), np.NaN, day))


def is_jalali_leap_year(year):
    return ((((((year - np.where(year > 0, 474, 473)) % 2820) + 474) + 38) * 682) % 2816) < 682


def get_days_in_jalali_month(year, month):
    return np.where(
        (month >= 1) & (month <= 6), 31,
        np.where(
            (month >= 7) & (month < 12),
            30,
            np.where(
                is_jalali_leap_year(year),
                30,
                29
            )
        )
    )


def validate_jalali_date(year, month, day):
    days_in_month = get_days_in_jalali_month(year, month)

    valid_year = (year >= MINYEAR) & (year <= MAXYEAR)
    valid_month = (month >= 1) & (month <= 12)
    valid_day = (day >= 1) & (day <= days_in_month)

    year.loc[~(valid_year & valid_month & valid_day)] = None
    month.loc[~(valid_year & valid_month & valid_day)] = None
    day.loc[~(valid_year & valid_month & valid_day)] = None

    return year, month, day


def get_gregorian_date_from_jalali_date(year, month, day):
    year, month, day = validate_jalali_date(year, month, day)
    return get_gregorian_date_from_julian_day(get_julian_day_from_jalali_date(year, month, day))