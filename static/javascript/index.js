// Function to toggle dropdown display
function toggleDropdown(id) {
	const dropdown = document.getElementById(id);
	dropdown.classList.toggle("show");
}

// Mapping of colors from Portuguese to English
const colorMap = {
	Navyblue: "navyblue",
	Yellow: "yellow",
	Red: "red",
	White: "white",
	Black: "black",
	Blue: "blue",
	Gray: "gray",
	Green: "green",
	Pink: "pink",
};

// Function to change the selected color
function changeColor(color) {
	const dropdownSummary = document.getElementById("dropdownSummary");
	dropdownSummary.textContent = "Color: " + color;

	const selectedColor = document.getElementById("selectedColor");
	selectedColor.value = colorMap[color] || color;
}

// Function to validate the form
function validateForm() {
	const minPrice = parseFloat(document.getElementById("min-price").value);
	const maxPrice = parseFloat(document.getElementById("max-price").value);
	const selectedColor = document.getElementById("selectedColor").value;

	if (!selectedColor) {
		alert("Please select a color.");
		return false;
	}

	if (minPrice < 0 || maxPrice < 0) {
		alert("Prices cannot be negative.");
		return false;
	}

	if (minPrice >= maxPrice) {
		alert("Minimum price must be less than maximum price.");
		return false;
	}

	genareteRecommendations();
	return false;
}

// Function to render a recommendation item
function renderizarItem(recommendation, recommendationsList) {
	const li = document.createElement("li");
	li.className = "title";

	const imagemProd = document.createElement("img");
	imagemProd.className = "clothing";
	const clothingType = [
		"tshirt",
		"short",
		"bikini",
		"tanktop",
		"jumpsuits",
		"femme",
		"top",
		"robe",
		"cap",
		"pant",
	];
	const title = recommendation.title
		.toLowerCase()
		.replace(/\s+/g, "")
		.replace(/-/g, "");

	clothingType.forEach(function (type) {
		if (title.includes(type) || title.includes(type + "s")) {
			imagemProd.src = `/static/assets/clothes/${type}-${recommendation.color}.jpg`;
		}
	});

	if (!imagemProd.src) {
		return; // Do not render the item if there is no corresponding image
	}

	imagemProd.alt = "Product image";
	li.appendChild(imagemProd);

	const hr = document.createElement("hr");
	li.appendChild(hr);

	const labels = {
		id: "ID",
		title: "Title",
		color: "Color",
		rating: "Rating",
		price: "Price",
	};

	Object.keys(labels).forEach((key) => {
		const span = document.createElement("span");
		let value = recommendation[key];
		if (key === "rating") {
			value += " stars";
		} else if (key === "price") {
			value = `$ ${value}`;
		}
		span.innerHTML = `<b>${labels[key]}: </b> ${value} <br>`;
		li.appendChild(span);
	});

	li.onclick = function () {
		redirectProduct(recommendation, imagemProd);
	};

	recommendationsList.appendChild(li);
}

// Function to redirect to product page
function redirectProduct(recommendation, imagemProd) {
	const recommendationsList = document.getElementById("recommendations");
	recommendationsList.innerHTML = "";
	const loading = document.getElementById("loading");
	loading.style.visibility = "visible";

	const queryString = new URLSearchParams({
		id: recommendation.id,
		title: recommendation.title,
		color: recommendation.color,
		rating: recommendation.rating,
		price: recommendation.price,
		image: imagemProd.src,
	}).toString();
	window.location.href = `/recommend-products?${queryString}`;
}

// Function to generate recommendations
function genareteRecommendations() {
	const recommendationsList = document.getElementById("recommendations");
	recommendationsList.innerHTML = "";

	const loading = document.getElementById("loading");
	loading.style.visibility = "visible";

	const formData = new FormData(document.getElementById("form"));

	const xhr = new XMLHttpRequest();
	xhr.open("POST", "/filter-products", true);
	xhr.onreadystatechange = function () {
		if (xhr.readyState == 4) {
			// Check if the request is complete
			loading.style.visibility = "hidden";
			if (xhr.status == 200) {
				try {
					const recommendations = JSON.parse(xhr.responseText);
					renderRecommendations(recommendations);
				} catch (e) {
					console.error("Failed to parse JSON response: ", e);
					renderRecommendations([]);
				}
			} else {
				console.error("Failed to fetch recommendations: ", xhr.status);
				renderRecommendations([]);
			}
		}
	};

	xhr.send(formData);
}

// Function to render all recommendations
function renderRecommendations(recommendations) {
	const recommendationsList = document.getElementById("recommendations");
	recommendationsList.innerHTML = "";

	if (recommendations.length === 0) {
		const noProductsMessage = document.createElement("div");
		noProductsMessage.className = "title-no-product";
		noProductsMessage.textContent =
			"No products available with the selected criteria.";

		recommendationsList.appendChild(noProductsMessage);

		return;
	}

	recommendations.forEach(function (recommendation) {
		renderizarItem(recommendation, recommendationsList);
	});
}

// Initialization when DOM is ready
document.addEventListener("DOMContentLoaded", function () {
	const currentURL = window.location.pathname; // Get the current page URL
	if (currentURL === "/recommend-products") {
		// Check if URL matches the /recommend-products route
		const recommendationsData = JSON.parse(
			document.getElementById("recommendations-container").dataset
				.recommendations
		);
		try {
			renderRecommendations(recommendationsData.slice(0, 100));
		} catch (error) {
			console.log("Error:", error);
		}
	}
});
