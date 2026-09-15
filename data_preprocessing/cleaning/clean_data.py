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
) 