import pandas as pd


def convert_df_to_json(df):
    """
    Converts DataFrame data to JSON
    """
    json_data = df.to_json(orient="records")
    return json_data


def convert_json_to_df(json):
    """
    Converts JSON data to DataFrame
    """
    df = pd.DataFrame(json)
    return df


def convert_dict_to_df(dict):
    """
    Converts data from a dictionary to a DataFrame
    """
    df = pd.DataFrame([dict])
    return df
