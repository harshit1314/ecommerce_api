from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class Product(BaseModel):
    name: str
    price: float
    quantity: int
    description: Optional[str] = None
    category: str

# New model for creating an order item
class OrderItemIn(BaseModel):
    product_name: str
    quantity: int

# New model for creating an order
class OrderIn(BaseModel):
    user_id: str
    items: List[OrderItemIn]

# The full Order model stored in the DB
class Order(BaseModel):
    timestamp: datetime = Field(default_factory=datetime.now)
    items: List[Product]
    total_amount: float
    user_id: str

# New model for the summary response
class OrderSummary(BaseModel):
    user_id: str
    total_orders: int
    total_value: float