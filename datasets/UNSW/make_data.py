import pandas as pd
import sys

path = sys.argv[1]
add_name = sys.argv[2]

if path is None or add_name is None:
    print("please add as argument, the path and the aditional name")

data = pd.read_csv(path, header=None)
data = data.fillna({47:"Normal"})
data = data.replace(" ", 0)
data = data.fillna(0)
cat = data[47].unique()
ldata = dict()
col_to_rm = [0,1,2,3,4,5,13,20,21,47,48]
print(cat)
for c in cat:
    d = data.loc[data[47] == c]
    d = d.drop(col_to_rm, axis = 1)
   # if str(c) == "nan":
   #     c = "Normal"
    if c[0] == " ":
        c = c[1:]
    if c[-1] == " ":
        c = c[:-1]
    d.to_csv("refined/{}_{}UNSW.csv".format(c, add_name), header=False, index=False, index_label=False)
