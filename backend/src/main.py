import os

import pandas as pd

from backend.src.services.convert import convert_df_to_json, convert_dict_to_df
from backend.src.services.recommend import filter_products, recommended_products


def create_df():
    """
    Creates a DataFrame from the database data and performs preprocessing.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "database", "products.csv")
    df = pd.read_csv(file_path, sep=",")
    return df


def get_filtered_products(options):
    """
    Obtains filtered products based on the options provided by the user.
    """

    # Creates a DataFrame from the data in the .csv file (products.csv)
    df = create_df()

    # Filters products based on the options provided by the user
    df_filtered = filter_products(options["price_range"], options["color"], df)

    # Checks if the filtered DataFrame is empty
    if df_filtered.empty:
        return

    # Converts the filtered DataFrame to JSON format
    json_filtered = convert_df_to_json(df_filtered)

    return json_filtered


def get_recommendations(dict_chosen_product):
    """
    Obtains product recommendations based on the user-chosen clothing.
    """

    # Creates a DataFrame from the data in the .csv file (products.csv)
    df_products = create_df()

    # Converts the dictionary of the chosen product into a DataFrame
    df_chosen_product = convert_dict_to_df(dict_chosen_product)

    # Obtains product recommendations based on the chosen clothing
    df_recommendations = recommended_products(df_products, df_chosen_product)

    # Converts the recommendations DataFrame to JSON format
    json_recommendations = convert_df_to_json(df_recommendations)

    return json_recommendations
