import pandas as pd
import numpy as np
from scipy import stats

# Load the Excel file
file_path = "Data set (2).xlsx"  # Update path if needed
data = pd.read_excel(file_path = r"C:\Users\DELL\Downloads\Data set (2).xlsx")


# Replace null values with 0
data_filled = data.fillna(0)

# Select only numeric columns for statistical analysis
numeric_data = data_filled.select_dtypes(include=[np.number])

# Calculate statistical metrics
mean_value = numeric_data.mean()                     # Mean
median_value = numeric_data.median()                 # Median
mode_value = numeric_data.mode().iloc[0]             # Mode (first mode if multiple)
variance_value = numeric_data.var()                  # Variance
std_dev_value = numeric_data.std()                   # Standard Deviation
range_value = numeric_data.max() - numeric_data.min()  # Range
skewness_value = stats.skew(numeric_data)            # Skewness
kurtosis_value = stats.kurtosis(numeric_data)        # Kurtosis

# Combine all results in one DataFrame
summary_stats = pd.DataFrame({
    "Mean": mean_value,
    "Median": median_value,
    "Mode": mode_value,
    "Variance": variance_value,
    "Standard Deviation": std_dev_value,
    "Range": range_value,
    "Skewness": skewness_value,
    "Kurtosis": kurtosis_value
})

# Round the values for better readability
summary_stats = summary_stats.round(2)

# Display the final summary statistics
print(summary_stats)
