"""
Python Pandas Interview Questions
"""

# 1) Create a df using list

import pandas as pd

a = ['python', 'pandas']
info = pd.DataFrame(a)
print(info)

# 2) Create a df from dict of ndarrays

import pandas as pd

info = {
    'ID': [101, 102, 103],
    'Department': ['B.Sc', 'B.Tech', 'M.Tech']
}
info = pd.DataFrame(info)
print(info)

# 3) Create a series (aka a vector) from dict in pandas

import pandas as pd
import numpy as np

info = {
    'x': 0.,
    'y': 1.,
    'z': 2.
}
a = pd.Series(info)
print(a)

# 4) Create an empty df

import pandas as pd

info = pd.DataFrame()
print(info)