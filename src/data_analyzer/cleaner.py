# src/data_analyzer/cleaner.py

import pandas as pd
from typing import Optional


class DataCleaner:
    """
    A class used to clean tabular data using pandas.
    """

    def __init__(self, df: Optional[pd.DataFrame] = None):
        """
        Initialize with a pandas DataFrame.

        :param df: Input pandas DataFrame
        """
        self.df = df

    def load_csv(self, filepath: str) -> None:
        """
        Load data from a CSV file.

        :param filepath: Path to the CSV file
        """
        try:
            self.df = pd.read_csv(filepath)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {filepath}")

    def clean_data(self) -> pd.DataFrame:
        """
        Perform standard cleaning operations:
        1. Normalize column names (lowercase, spaces to underscores)
        2. Remove duplicate rows
        3. Drop rows with missing values

        :return: Cleaned DataFrame
        """
        if self.df is None:
            raise ValueError("No data loaded. Please load data first.")

        # 1. Normalize column names
        self.df.columns = self.df.columns.str.lower().str.strip()

        # 2. Remove duplicates
        initial_rows = len(self.df)
        self.df = self.df.drop_duplicates()

        # 3. Drop missing values
        self.df = self.df.dropna()

        final_rows = len(self.df)
        print(f"Cleaned data: Removed {initial_rows - final_rows} rows.")

        return self.df
