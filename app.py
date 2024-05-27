from flask import Flask, render_template, request

from backend.src.main import get_filtered_products, get_recommendations

# Initialize the Flask application and define the static directory
app = Flask(__name__, static_folder="static")


# Define a route /filter
@app.route("/filter-products", methods=["GET", "POST"])
def filter():
    if request.method == "POST":
        # Extract parameters from the form submitted by POST method
        price_min = float(request.form.get("min-price", 0))
        price_max = float(request.form.get("max-price", 1000))
        color = request.form.get("color")

        # Display the extracted parameters
        print("Minimum Price:", price_min)
        print("Maximum Price:", price_max)
        print("Selected Color:", color)

        # Create a variable to store filtering options
        options = {"price_range": (float(price_min), float(price_max)), "color": color}

        # Get filtered products based on the provided options
        filtered_products = get_filtered_products(options)

        # Check if there are no filtered products
        if not filtered_products:
            return render_template("filter.html")

        return filtered_products

    else:
        # If it's a GET request, return the HTML recommendation page
        return render_template("filter.html")


# Define the route /recommend-products
@app.route("/recommend-products")
def recommend_products():
    # Get product data passed by the URL
    ID = request.args.get("id")
    title = request.args.get("title")
    color = request.args.get("color")
    rating = request.args.get("rating")
    price = request.args.get("price")
    image = request.args.get("image")

    # Create a dictionary containing the information of the chosen product
    dict_chosen_product = {
        "ID": ID,
        "title": title,
        "color": color,
        "rating": rating,
        "price": price,
    }

    # Get product recommendations based on the chosen product
    recommendations = get_recommendations(dict_chosen_product)

    # Render the HTML page passing the product details and new recommendations
    return render_template(
        "recommend.html",
        id=ID,
        title=title,
        color=color,
        rating=rating,
        price=price,
        image=image,
        recommendations=recommendations,
    )


# Define the root route of the application
@app.route("/")
def inicio():
    # Render the initial HTML page
    return render_template("home.html")


# Start the execution of the Flask application
if __name__ == "__main__":
    app.run(debug=True)
