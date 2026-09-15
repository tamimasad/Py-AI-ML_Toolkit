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

    # 4. Handle missing values

    if fill_missing:

        # Find numerical columns.
        numeric_columns = cleaned_df.select_dtypes(include="number").columns

        # Fill missing numerical values with the median.

        for column in numeric_columns:
            if cleaned_df[column].isna().any():
                median_value = cleaned_df[column].median()
                cleaned_df[column] = cleaned_df[column].fillna(median_value)

        # Find categorical/text columns.
        categorical_columns = cleaned_df.select_dtypes(
            include=["object", "category"]
        ).columns

        # Fill missing categorical values with the mode.
        for column in categorical_columns:
            if cleaned_df[column].isna().any():

                # Mode returns the most frequently occurring value.
                mode_values = cleaned_df[column].mode()

                # Only fill if a mode actually exists.
                if not mode_values.empty:
                    cleaned_df[column] = cleaned_df[column].fillna(mode_values.iloc[0])

    # 5. Convert suitable columns to numeric

    for column in cleaned_df.columns:

        # Try converting the column to numbers.
        converted_column = pd.to_numeric(cleaned_df[column], errors="coerce")

        # Count how many values could be converted.
        valid_numeric_values = converted_column.notna().sum()

        # If most values can be converted to numbers,
        # treat the column as a numerical column.
        if valid_numeric_values >= len(cleaned_df) * 0.8:
            cleaned_df[column] = converted_column

    # 6. Handle infinite values

    # Replace positive and negative infinity with NaN.
    cleaned_df = cleaned_df.replace([float("inf"), float("-inf")], pd.NA)

    # Remove rows that still contain missing values.

    cleaned_df = cleaned_df.dropna()

    # 7. Reset the DataFrame index

    cleaned_df = cleaned_df.reset_index(drop=True)

    return cleaned_df
