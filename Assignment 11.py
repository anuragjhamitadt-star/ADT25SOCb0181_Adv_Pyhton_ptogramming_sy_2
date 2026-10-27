import numpy as np
import pandas as pd

# Create a Series containing ten random numbers
np.random.seed(42)
series = pd.Series(np.random.randint(1, 101, 10))

print("Series:")
print(series)

# Indexing
print("\nValue at index 3:")
print(series[3])

# Filtering values greater than 50
print("\nValues greater than 50:")
print(series[series > 50])

# Statistical operations
print("\nMean:", series.mean())
print("Median:", series.median())
print("Minimum:", series.min())
print("Maximum:", series.max())
