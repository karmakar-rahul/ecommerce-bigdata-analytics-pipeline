from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).parent

def load_csv(filename):
    return pd.read_csv(
        BASE_DIR / "data" / filename
    )
