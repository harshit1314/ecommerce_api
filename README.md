# FastAPI E-commerce API

A simple yet powerful REST API for a mock e-commerce platform, built with Python, FastAPI, and MongoDB. This application allows for the management of products and orders, providing a foundation for a scalable e-commerce backend.

## ✨ Features

-   **Product Management**: Create and list products in the inventory.
-   **Order Processing**: Create orders with items from the inventory.
-   **Automatic Price Calculation**: The total order price is calculated automatically on the server side.
-   **User-Specific Data**: List all orders placed by a specific user.
-   **Order Analytics**: Get a summary of the total number and value of orders for any user.
-   **Interactive Documentation**: Automatic, interactive API documentation powered by Swagger UI.

## 🛠️ Tech Stack

-   **Backend**: Python
-   **Framework**: FastAPI
-   **Database**: MongoDB (with MongoDB Atlas)
-   **Python Driver**: Pymongo
-   **Server**: Uvicorn

---

## 🚀 Setup and Installation

Follow these steps to get the project running on your local machine.

### 1. Prerequisites

-   Python 3.8+
-   Git
-   A MongoDB Atlas account and a connection string.

### 2. Clone the Repository

```bash
git clone [https://github.com/YourUsername/fastapi-ecommerce-api.git](https://github.com/harshit1314/fastapi-ecommerce-api.git)
cd fastapi-ecommerce-api
```

### 3. Create and Activate a Virtual Environment

-   **Windows (Git Bash):**
    ```bash
    python -m venv venv
    source venv/Scripts/activate
    ```
-   **macOS/Linux:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```
*(Note: You will need to create a `requirements.txt` file by running `pip freeze > requirements.txt`)*

### 5. Configure Database

Open the `database.py` file and replace the placeholder with your MongoDB Atlas connection string.

```python
MONGO_URI = "mongodb+srv://<username>:<password>@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority"
```

### 6. Run the Server

```bash
uvicorn main:app --reload
```
The application will be running at `http://127.0.0.1:8000`.

---

## 📚 API Endpoints

All endpoints are accessible via the interactive documentation at `http://127.0.0.1:8000/docs`.

### Product Endpoints

| Method | Path         | Description                | Request Body Example                                                                                                                              |
| :----- | :----------- | :------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------ |
| `POST` | `/products`  | Creates one or more products. | `[{"name": "Laptop", "price": 1200, "quantity": 50, "category": "Electronics"}]`                                                                  |
| `GET`  | `/products`  | Lists all available products.  | N/A                                                                                                                                               |

### Order Endpoints

| Method | Path         | Description                | Request Body Example                                                                                                                              |
| :----- | :----------- | :------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------ |
| `POST` | `/orders`    | Creates a new order.       | `{"user_id": "test-user-1", "items": [{"product_name": "Laptop", "quantity": 1}]}`                                                                   |
| `GET`  | `/orders/{user_id}` | Lists all orders for a user. | N/A                                                                                                                                               |

### User Summary Endpoint

| Method | Path                           | Description                               |
| :----- | :----------------------------- | :---------------------------------------- |
| `GET`  | `/users/{user_id}/order-summary` | Gets a summary of a user's order history. |
