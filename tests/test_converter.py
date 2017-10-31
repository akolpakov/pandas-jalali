import unittest
import pandas as pd
import numpy as np

from khayyam import JalaliDate
from datetime import timedelta
from pandas_jalali.converter import get_gregorian_date_from_jalali_date, validate_jalali_date


class TestConverter(unittest.TestCase):

    def setUp(self):
        dt = JalaliDate(1346, 12, 30)

        dt_jalali_y = []
        dt_jalali_m = []
        dt_jalali_d = []

        dt_gregorian_y = []
        dt_gregorian_m = []
        dt_gregorian_d = []

        for t in range(1, 10000):
            dt += timedelta(days=1)

            dt_jalali_y.append(dt.year)
            dt_jalali_m.append(dt.month)
            dt_jalali_d.append(dt.day)

            gregorian = dt.todate()

            dt_gregorian_y.append(gregorian.year)
            dt_gregorian_m.append(gregorian.month)
            dt_gregorian_d.append(gregorian.day)

        self.dt_jalali_y = pd.Series(dt_jalali_y)
        self.dt_jalali_m = pd.Series(dt_jalali_m)
        self.dt_jalali_d = pd.Series(dt_jalali_d)

        self.dt_gregorian_y = pd.Series(dt_gregorian_y)
        self.dt_gregorian_m = pd.Series(dt_gregorian_m)
        self.dt_gregorian_d = pd.Series(dt_gregorian_d)

    def test_get_gregorian_date_from_jalali_date(self):
        y, m, d = get_gregorian_date_from_jalali_date(
            self.dt_jalali_y,
            self.dt_jalali_m,
            self.dt_jalali_d
        )

        self.assertTrue(y.equals(self.dt_gregorian_y.astype(float)))
        self.assertTrue(m.equals(self.dt_gregorian_m.astype(float)))
        self.assertTrue(d.equals(self.dt_gregorian_d.astype(float)))

    def test_validate_jalali_date(self):
        dt_jalali_y = pd.Series([4178, 1346, 1346, None, None, 1346])
        dt_jalali_m = pd.Series([1, 1, 23, None, 1, 1])
        dt_jalali_d = pd.Series([1, 34, 1, None, 1, 1])

        y, m, d = validate_jalali_date(
            dt_jalali_y,
            dt_jalali_m,
            dt_jalali_d
        )

        self.assertTrue(y.equals(pd.Series([np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, 1346])))
        self.assertTrue(m.equals(pd.Series([np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, 1])))
        self.assertTrue(d.equals(pd.Series([np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, 1])))

    def test_invalid_date_convertation(self):
        dt_jalali_y = pd.Series([np.NaN, 1346])
        dt_jalali_m = pd.Series([np.NaN, 1])
        dt_jalali_d = pd.Series([np.NaN, 1])

        y, m, d = get_gregorian_date_from_jalali_date(
            dt_jalali_y,
            dt_jalali_m,
            dt_jalali_d
        )

        self.assertTrue(y.equals(pd.Series([np.NaN, 1967])))
        self.assertTrue(m.equals(pd.Series([np.NaN, 3])))
        self.assertTrue(d.equals(pd.Series([np.NaN, 21])))
