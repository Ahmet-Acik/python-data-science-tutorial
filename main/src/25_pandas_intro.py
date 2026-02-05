"""
Pandas Introduction

This file provides an introduction to Pandas, a powerful data manipulation library in Python.
It covers Series, DataFrames, basic operations, and data handling best practices.
"""

import pandas as pd
import numpy as np

def demonstrate_series():
    """Demonstrate Pandas Series creation and operations."""
    print("=== Pandas Series ===")

    # Creating Series from list
    data = [1, 3, 5, 6, 8]
    series = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])
    print(f"Series from list:\n{series}\n")

    # Creating Series from dict
    data_dict = {'a': 1, 'b': 2, 'c': 3}
    series_dict = pd.Series(data_dict)
    print(f"Series from dict:\n{series_dict}\n")

    # Basic operations
    print(f"Mean: {series.mean()}")
    print(f"Sum: {series.sum()}")
    print(f"Max: {series.max()}\n")

def demonstrate_dataframe():
    """Demonstrate Pandas DataFrame creation and operations."""
    print("=== Pandas DataFrame ===")

    # Creating DataFrame from dict
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['NYC', 'LA', 'Chicago', 'Houston']
    }
    df = pd.DataFrame(data)
    print(f"DataFrame:\n{df}\n")

    # Basic operations
    print(f"Shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    print(f"Info:\n{df.info()}\n")

    # Selecting data
    print(f"First 2 rows:\n{df.head(2)}\n")
    print(f"Age column:\n{df['Age']}\n")
    print(f"Rows where Age > 30:\n{df[df['Age'] > 30]}\n")

def demonstrate_data_operations():
    """Demonstrate common data operations with Pandas."""
    print("=== Data Operations ===")

    # Sample data
    data = {
        'Product': ['A', 'B', 'C', 'A', 'B'],
        'Sales': [100, 150, 200, 120, 180],
        'Region': ['North', 'South', 'East', 'West', 'North']
    }
    df = pd.DataFrame(data)

    # Grouping and aggregation
    sales_by_product = df.groupby('Product')['Sales'].sum()
    print(f"Sales by Product:\n{sales_by_product}\n")

    # Adding new column
    df['Profit'] = df['Sales'] * 0.2
    print(f"DataFrame with Profit:\n{df}\n")

    # Handling missing data
    df_with_nan = df.copy()
    df_with_nan.loc[0, 'Sales'] = np.nan
    print(f"DataFrame with NaN:\n{df_with_nan}\n")
    print(f"After filling NaN:\n{df_with_nan.fillna(df_with_nan['Sales'].mean())}\n")

def demonstrate_file_io():
    """Demonstrate reading and writing data with Pandas."""
    print("=== File I/O ===")

    # Create sample data
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Score': [85, 92, 78]
    }
    df = pd.DataFrame(data)

    # Save to CSV
    csv_file = 'sample_data.csv'
    df.to_csv(csv_file, index=False)
    print(f"Saved to {csv_file}")

    # Read from CSV
    df_read = pd.read_csv(csv_file)
    print(f"Read from CSV:\n{df_read}\n")

    # Clean up
    import os
    if os.path.exists(csv_file):
        os.remove(csv_file)

def main():
    """Main function to run all Pandas demonstrations."""
    print("Pandas Introduction Examples\n")

    try:
        demonstrate_series()
        demonstrate_dataframe()
        demonstrate_data_operations()
        demonstrate_file_io()

        print("All Pandas examples completed successfully!")

    except Exception as e:
        print(f"Error in Pandas demonstration: {e}")

if __name__ == "__main__":
    main()