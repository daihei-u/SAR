#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import sys

filename=sys.argv[1]


sardf=pd.read_csv(filename,names=["x","y","z","pl"],delim_whitespace=True,skiprows=2)
print(sardf.head())
print("----------------")
print(sardf.describe())
print(sardf.columns)
