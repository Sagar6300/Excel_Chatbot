import pandas as pd

def clean_column_names(df):
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    return df

def load_excel(file):
    df = pd.read_excel(file)
    df = clean_column_names(df)
    return df


