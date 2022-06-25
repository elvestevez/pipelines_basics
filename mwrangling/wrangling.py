import pandas as pd

# wrangling method

def wrangling(df, year):
    df_filtered = df[df['Year'] == year]    
    return df_filtered
