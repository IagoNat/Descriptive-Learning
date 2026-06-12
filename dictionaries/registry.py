from pathlib import Path
import pandas as pd

class DictionaryRegistry:
    def __init__(self, base_path="gov/rais/dictionaries"):
        self.base_path = Path(base_path)

    def load(self, column_name: str) -> pd.DataFrame:
        return pd.read_csv(self.base_path/f"{column_name}.csv")
