#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import sys

filename=sys.argv[1]

COLS=["x","y","z","pl"]
sardf=pd.read_csv(filename,names=COLS,delim_whitespace=True,skiprows=2)
print(sardf.columns)
print("sardf--------------------------------")
print(sardf.head())
print(sardf.describe())

print("sardf1 x>=-60 -----------------------")
sardf1=sardf[sardf["x"]>=-60]
print(sardf1.head())
print(sardf1.describe())

print("sardf2 x<=60(base sardf1)------------")
sardf2=sardf1[sardf["x"]<=60]
print(sardf2.head())
print(sardf2.describe())

print("sardf3 x>=-60 & x<=60(base sardf)----")
sardf3=sardf[(sardf["x"]>=-60)&(sardf["x"]<=60)]
print(sardf3.head())
print(sardf3.describe())
