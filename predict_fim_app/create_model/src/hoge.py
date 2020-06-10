import pandas as pd
import numpy as np

c = ["a", "c"]
a = pd.DataFrame([[1,2,3],[4,5,6]], columns=["a", "b", "c"])

b = a[c]

print(a)

print(b)