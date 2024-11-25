from flask import Flask, jsonify, request

app = Flask(__name__)

# Mocked product data (in-memory store)
products = [
    {
        "productid": 1,
        "productname": "Apple",
        "description": "Fresh Red Apple",
        "image": "apple.jpg",
        "wholesaleprice": 2.5,
        "retailprice": 3.0,
        "quantity": 100,
        "type": "fruit",
        "fid": 1
    },
    {
        "productid": 2,
        "productname": "Banana",
        "description": "Ripe Yellow Banana",
        "image": "banana.jpg",
        "wholesaleprice": 1.2,
        "retailprice": 1.5,
        "quantity": 150,
        "type": "fruit",
        "fid": 2
    },
    {
        "productid": 3,
        "productname": "Carrot",
        "description": "Fresh Organic Carrot",
        "image": "carrot.jpg",
        "wholesaleprice": 3.0,
        "retailprice": 3.5,
        "quantity": 50,
        "type": "vegetable",
        "fid": 3
    }
]

# Endpoint to get all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify({"products": products}), 200

# Endpoint to get a single product by its ID
@app.route('/product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((product for product in products if product['productid'] == product_id), None)
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    return jsonify({"product": product}), 200

# Endpoint to add a new product (mock data, no SQL)
@app.route('/product', methods=['POST'])
def add_product():
    data = request.json
    new_product = {
        "productid": len(products) + 1,
        "productname": data.get("productname"),
        "description": data.get("description"),
        "image": data.get("image"),
        "wholesaleprice": data.get("wholesaleprice"),
        "retailprice": data.get("retailprice"),
        "quantity": data.get("quantity"),
        "type": data.get("type"),
        "fid": data.get("fid")  # Mock farmer ID or product owner
    }
    products.append(new_product)
    return jsonify({"message": "Product added successfully", "product": new_product}), 201

# Running the Flask app
if __name__ == '__main__':
    app.run(debug=True)
