from fastapi import FastAPI, HTTPException
from typing import List

from models import Product, Order, OrderIn, OrderSummary
from database import product_collection, order_collection

app = FastAPI(
    title="E-commerce API",
    description="An API for a simple e-commerce platform.",
    version="1.0.0"
)

# --- Product Endpoints ---
@app.post("/products", response_model=List[Product], status_code=201)
def create_products(products: List[Product]):
    """Creates one or more new products in the database."""
    product_dicts = [p.dict() for p in products]
    product_collection.insert_many(product_dicts)
    return products

@app.get("/products", response_model=List[Product])
def list_products(limit: int = 10, offset: int = 0):
    """Lists all products with pagination."""
    # The second argument {"_id": 0} excludes the MongoDB internal ID
    products = [Product(**p) for p in product_collection.find({}, {"_id": 0}).skip(offset).limit(limit)]
    return products

# --- Order Endpoints ---
@app.post("/orders", response_model=Order, status_code=201)
def create_order(order_in: OrderIn):
    """
    Creates an order. The server finds each product in the database
    and calculates the total price automatically.
    """
    full_items = []
    total_amount = 0

    # Fetch each product from the DB and calculate total
    for item_in in order_in.items:
        product_db = product_collection.find_one({"name": item_in.product_name})
        if not product_db:
            raise HTTPException(status_code=404, detail=f"Product '{item_in.product_name}' not found")
        
        product = Product(**product_db)
        total_amount += product.price * item_in.quantity
        
        # We store the full product details in the order
        product.quantity = item_in.quantity
        full_items.append(product)

    # Create the final order object
    order = Order(
        user_id=order_in.user_id,
        items=full_items,
        total_amount=round(total_amount, 2)
    )
    
    order_collection.insert_one(order.dict())
    return order

@app.get("/orders/{user_id}", response_model=List[Order])
def list_orders_for_user(user_id: str, limit: int = 10, offset: int = 0):
    """Lists all orders for a specific user, with pagination."""
    orders = [Order(**o) for o in order_collection.find({"user_id": user_id}, {"_id": 0}).skip(offset).limit(limit)]
    if not orders:
        raise HTTPException(status_code=404, detail=f"No orders found for user {user_id}")
    return orders

# --- User Summary Endpoint ---
@app.get("/users/{user_id}/order-summary", response_model=OrderSummary)
def get_user_order_summary(user_id: str):
    """
    Gets the total number of orders and the total value of all orders for a user.
    """
    pipeline = [
        {"$match": {"user_id": user_id}},
        {"$group": {
            "_id": "$user_id",
            "total_value": {"$sum": "$total_amount"},
            "total_orders": {"$sum": 1}
        }}
    ]
    
    result = list(order_collection.aggregate(pipeline))
    
    if not result:
        raise HTTPException(status_code=404, detail=f"No orders found for user {user_id}")
    
    summary_data = result[0]
    return OrderSummary(
        user_id=summary_data["_id"],
        total_orders=summary_data["total_orders"],
        total_value=summary_data["total_value"]
    )
     @app.get("/")
def read_root():
    """A welcome message for the root endpoint."""
    return {"message": "Welcome to the E-commerce API!"}
