from backend.src.services.calculate import get_cosine_similarity


def recommended_products(df_products, df_chosen_product):
    """
    Gets recommended products based on the user-chosen clothing.
    """
    # Calculate cosine similarity between the chosen clothing and all products in the DataFrame
    cosine_sim = get_cosine_similarity(df_products, df_chosen_product)

    # Add a similarity column to the original DataFrame
    df_products["similarity"] = cosine_sim["similarity"]

    # Sort the products based on similarity, from highest to lowest
    df_products = df_products.sort_values(by="similarity", ascending=False)

    # Return the DataFrame with the recommended products
    return df_products


def filter_products(price_range, color, df_products):
    """
    Filters products based on the specified price range and color.
    """
    # Filtering the data (price range and color)
    df_filtered_products = df_products[
        (df_products["price"] >= price_range[0])
        & (df_products["price"] <= price_range[1])
        & (df_products["color"] == color)
    ]

    # Sort the filtered products based on rating, from highest to lowest
    df_filtered_products = df_filtered_products.sort_values(
        by="rating", ascending=False
    )

    # Return the DataFrame with the filtered products
    return df_filtered_products
