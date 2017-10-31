# pandas-jalali

Package for converting dates from Gregorian to A Persian Date (aka: Jalali Calendar) and back.

This package is port of package [khayyam](https://github.com/pylover/khayyam) to use with Pandas dataframes.

# Installation

To install from package manager:

```
pip install pandas-jalali
```


# Usage

To convert from Jalali dates to Gregorian:

```python
import pandas as pd
from pandas_jalali.converter import get_gregorian_date_from_jalali_date

df = pd.DataFrame([
    [1346, 1, 1],
    [1346, 10, 20]
], columns=['year', 'month', 'day'])

df['year_gregorian'], df['month_gregorian'], df['day_gregorian'] = get_gregorian_date_from_jalali_date(df['year'], df['month'], df['day'])

print df
```

```
     year  month   day  year_gregorian  month_gregorian  day_gregorian
0  1346.0    1.0   1.0          1967.0              3.0           21.0
1  1346.0   10.0  20.0          1968.0              1.0           10.0

```

To convert from Gregorian dates to Jalali:
*Not yet implemented*

# Tests
At first make sure that you are in virtualenv.

Install all dependencies:
```
make setup
```
To run tests:
```
make test
```

# License
[MIT licence](./LICENSE)
