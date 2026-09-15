"""
Data Cleaning Module
-----------------------

This module contains simple functions for cleaning a dataset
before applying preprocessing techniques
such as standardization or normalization.

"""

import pandas as pd  # type: ignore[import-untyped]


def clean_data(
    df: pd.DataFrame,
    remove_duplicates: bool = True,
    fill_missing: bool = True,
) -> pd.DataFrame:
    """
    Clean a Pandas DataFrame.
    The function:
    1. Removes completely empty rows and columns.
    2. Removes duplicate rows.
    3. Handles missing values.
    4. Attempts to convert suitable columns to numeric types.
    5. Removes rows containing invalid values.

    """

    # 1. Input validation check

    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a Pandas DataFrame.")

    if df.empty:
        raise ValueError("Dataset cannot be empty.")

    # Copy of the original dataset to work on.
    cleaned_df = df.copy()

    # 2. Remove completely empty rows and columns

    # Remove rows where every value is missing.
    cleaned_df = cleaned_df.dropna(axis=0, how="all")

    # Remove columns where every value is missing.
    cleaned_df = cleaned_df.dropna(axis=1, how="all")

    # 3. Remove duplicate rows

    if remove_duplicates:
        cleaned_df = cleaned_df.drop_duplicates()

   