import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder


def unify_dfs(df_products, df_chosen_product):
    """
    Unifies the DataFrame of products with the DataFrame of the chosen product
    """
    unified_df = pd.concat([df_chosen_product, df_products], ignore_index=True)
    return unified_df


def vectorize_features(df, Vectorizer):
    """
    Vectorizes the titles of the DataFrame
    """
    # Vectorizing the titles of the DataFrame into a matrix
    matrix = Vectorizer.fit_transform(df["title"])
    return matrix


def normalize_features(df, Scaler):
    """
    Normalizes the numerical features (price and rating) of the DataFrame
    """
    # Selects the features from the DataFrame
    numeric_features = df[["price", "rating"]]

    # Normalization of the features
    numeric_features_normalized = Scaler.fit_transform(numeric_features)
    return numeric_features_normalized


def encode_features(df, Encoder):
    """
    Encodes colors using one-hot encoding for the DataFrame
    """
    # Selects the features from the DataFrame
    features = df[["color"]]

    # Encodes the features
    features_encoded = Encoder.fit_transform(features).toarray()
    return features_encoded


def combine_features(
    vectorized_titles, normalized_price_and_rating, encoded_colors, Vectorizer, Encoder
):
    """
    Combines the processed data (titles, colors, prices, and ratings) into a single feature DataFrame
    """
    # Creates a DataFrame of features and inserts the vectorized titles
    df_features = pd.DataFrame(
        vectorized_titles.toarray(), columns=Vectorizer.get_feature_names_out()
    )

    # Inserts the normalized prices and ratings into the created DataFrame
    df_features = df_features.join(
        pd.DataFrame(normalized_price_and_rating, columns=["price", "rating"])
    )

    # Inserts the encoded colors into the created DataFrame
    df_features = df_features.join(
        pd.DataFrame(
            encoded_colors,
            columns=Encoder.get_feature_names_out(["color"]),
        )
    )
    return df_features


def calculate_cosine_similarity(df_features):
    """
    Calculates the cosine similarity between all products in the DataFrame
    """
    similarity = cosine_similarity(df_features)

    # Returns only the similarity of the first product in the DataFrame - chosen product
    return similarity[0][1:]


def get_cosine_similarity(df_products, df_chosen_product):
    # Initialize the TF-IDF vectorizer
    Vectorizer = TfidfVectorizer()
    # Initialize the scaler (normalizer)
    Scaler = MinMaxScaler()
    # Initialize the one-hot encoder
    Encoder = OneHotEncoder()

    # Unify the DataFrame of products with the chosen product DataFrame
    unified_df = unify_dfs(df_products, df_chosen_product)

    # Vectorize the titles of the DataFrame
    vectorized_df_titles = vectorize_features(unified_df, Vectorizer)

    # Normalize the ratings and prices of the DataFrame
    normalized_df_price_and_rating = normalize_features(unified_df, Scaler)

    # Encode the colors of the DataFrame
    encoded_df_colors = encode_features(unified_df, Encoder)

    # Combine the features into a single DataFrame
    df_features = combine_features(
        vectorized_df_titles,
        normalized_df_price_and_rating,
        encoded_df_colors,
        Vectorizer,
        Encoder,
    )

    # Calculate the cosine similarity between the chosen product and all clothes in the DataFrame
    similarity = calculate_cosine_similarity(df_features)

    # Create a DataFrame with the titles of the clothes and their respective similarities
    df_similarity_clothes = pd.DataFrame(
        {"title": df_products["title"], "similarity": similarity}
    )

    return df_similarity_clothes
