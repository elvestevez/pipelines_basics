import pandas as pd

# acquisition method

def acquisition(path):
    df = pd.read_csv(path)
    return df
