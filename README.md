# Recon-IA - Product Recommendation

## Project Description

This project is a web application developed with Flask for product recommendation. The application allows users to filter products by price range and color and receive personalized recommendations based on a specific selected product. The backend processes the data and calculates similarities between products to provide relevant recommendations.

## Technologies
- **Backend**:
  - **Python**: Python serves as the primary programming language for the backend development of the project. It is used for implementing core functionalities, data processing, and business logic.
  - **Flask**: Flask is utilized as the web framework for the backend. It provides routing capabilities, allowing the application to handle HTTP requests and responses efficiently. Flask is also responsible for integrating various components and modules of the backend.

- **Data Processing and Machine Learning**:
  - **Pandas**: Pandas is employed for data manipulation and analysis within the backend. It helps in loading and processing product data from CSV files, performing filtering operations, and preparing data for machine learning-based recommendations.
  - **Scikit-learn**: Scikit-learn is integrated into the backend for machine learning tasks. It facilitates the calculation of similarities between products using algorithms such as cosine similarity, enabling personalized product recommendations.

- **Frontend**:
  - **HTML/CSS**: HTML and CSS are used in conjunction to create the user interface (UI) of the web application. HTML defines the structure of web pages, while CSS styles them, ensuring visual consistency and enhancing the user experience.
  - **JavaScript**: JavaScript enhances the frontend interactivity of the application. It is responsible for implementing dynamic features, such as form validation, interactive product filtering, and asynchronous communication with the backend for seamless user interactions.

## Installation

1. **Clone the repository:**  
   `git clone https://github.com/brenocrepaldi/recon-ia-recommendation-system`  
   `cd recon-ia-recommendation-system`

2. **Create and activate a virtual environment:**  
   `python3 -m venv venv`  
   `venv\Scripts\activate`  
   `# for MacOS: source venv/bin/activate`  
   `# use 'deactivate' to deactivate the virtual environment`

4. **Install dependencies:**  
   `pip install -r requirements.txt`

5. **Run the application:**  
   `python app.py`

6. **Access the application:**  
   Open a browser and go to http://127.0.0.1:5000.

## Project Structure

The project structure is organized as follows:

### Files Description

- `app.py`: Contains the routes of the Flask application and the main server logic.
- `backend/src/main.py`: Contains the main functions to get filtered products and recommendations.
- `backend/src/services/calculate.py`: Contains functions to calculate cosine similarity between products.
- `backend/src/services/convert.py`: Contains functions for DataFrame to JSON conversion and vice versa.
- `backend/src/services/recommend.py`: Contains functions for product filtering and recommendation.
- `backend/src/database/produtos.csv`: CSV file containing product data.
- `templates/`: Directory containing HTML files for page rendering.
- `static/`: Directory for static files such as CSS, JavaScript, and images.

# Features

1. **Home Page (`/`)**  
   - Displays the home page of the application.

2. **Filter Page (`/filter-products`)**  
   - **GET Method:** Displays the form to filter products.
   - **POST Method:** Processes the filters (minimum price, maximum price, and color) and displays the products that match the criteria.

3. **Recommendation Page (`/recommend-products`)**  
   - Shows after an interation with a product on the filter page.
   - Displays details of the selected product and shows recommendations based on it characteristics.

## Recommendation Logic

### Product Filtering
- The `get_filtered_products(options)` function filters products based on the price range and color provided by the user.
- The `filter_products(price_range, color, df_products)` function applies filters to the products DataFrame and returns the filtered products.

### Product Recommendations
- The `get_recommendations(dict_chosen_product)` function obtains recommendations based on a specific selected product.
- Cosine similarity is used to calculate the similarity between products.
- The `vectorize_features`, `normalize_features`, `encode_features`, and `combine_features` functions process product data to calculate their similarities.

## Final Considerations

This project demonstrates a practical application of product recommendation using data processing, machine learning, and artificial intelligence techniques. It can be expanded with more features, such as the inclusion of more product filters, improvement in the user interface, and optimization of recommendation algorithms.

To contribute to the project, feel free to open issues or send pull requests on the GitHub repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, feel free to contact us at [brenogaia2004@gmail.com](mailto:brenogaia2004@gmail.com).

## Acknowledgments

I would like to thank Marcos Antonio Valério Filho and João Vitor Custódio for their contributions to this project.
