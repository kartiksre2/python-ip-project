from functions import *
import pandas as pd

array1 = pd.array([10, 42, 523, 63, 85])

series = pd.Series(array1)

printHeading("series")
print(series)
breaker()
print(f"size = {series.size}")
print(f"index = {list(series.index)}")
print(f"shape = {series.shape}")
