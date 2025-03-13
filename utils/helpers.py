import pandas as pd

def normalize_data(df):
    return (df - df.min()) / (df.max() - df.min())
