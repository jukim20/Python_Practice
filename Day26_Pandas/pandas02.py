import pandas as pd
import numpy as np

data = {"names": ["Kilho", "Kilho", "Kilho", "Charles", "Charles"],
           "year": [2014, 2015, 2016, 2015, 2016],
           "points": [1.5, 1.7, 3.6, 2.4, 2.9]}
df = pd.DataFrame(data, columns=["year", "names", "points", "penalty"],
                          index=["one", "two", "three", "four", "five"])
print(df)
print(df["year"])
print(df.year)
print(df[["year","points"]])
df["penalty"] = 0.5
print(df)
df["penalty"]  = [0.1,0.2,0.3,0.4,0.5]
print(df)
df["zeros"] = np.arange(5)
print(df)
val = pd.Series([-1.2, -1.5, -1.7], index=["two", "four","five"])
df["debt"] = val
print(df)
df["net_points"]  = df["points"] - df["penalty"]
df["high_points"] = df["net_points"]>2.0
print(df)
del df["high_points"]
print(df)
df.index.name = "Order"
df.columns.name = "Info"
print(df)
print(df[0:3])
print(df["two":"four"])
print(df.loc["two"])
print(df.loc["two":"four"])
print(df.loc["two":"four","points"])
print(df.loc[:,"year"])
print(df.loc[:, ["year","names"]])
print(df.loc["three":"five", "year":"penalty"])
print(df)

df.loc["six", :] = [2013,"hayoung",4.0,0.1,3 ,1,1]
print(df)

print(df.iloc[3])
print(df.loc["four"])
