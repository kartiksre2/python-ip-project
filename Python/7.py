from functions import *
import pandas as pd


series = pd.Series([10, 420, 521, 62, 46])

printHeading("series")
print(series)
breaker()
print(f"series.size = {series.size}")
print(f"series.shape = {series.shape}")
print(f"series.index = {list(series.index)}")
print(f"series.name = {series.name}")
print(f"series.index.name = {series.index.name}")
print(f"series.empty = {series.empty}")
