import pandas as pd

# analysis method

def analysis(df, group, agg, file='./data/result.csv'):
    analyzed = df.groupby(by=group)[agg].mean()
    analyzed.to_csv(file)
    return analyzed
