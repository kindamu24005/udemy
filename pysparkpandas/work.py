import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_profiling as pdp

#df0 = pd.read_excel("Online Retail.xlsx")

#csvファイルに保存
#df0.to_csv("Online_Retail.csv", encoding="cp932", index=None)

df = pd.read_csv("Online_Retail.csv", encoding="cp932")
#print(df.head())
#print(df.tail())
#print(len(df))
#print(df.shape)
#print(df.columns)
#print(df.dtypes)
#print(df.describe())
pdp.ProfileReport(df)
