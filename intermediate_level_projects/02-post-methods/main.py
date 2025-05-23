import fastapi
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel, Field, EmailStr, computed_field,validator
from typing import Optional,Annotated,List,Dict,Literal
import os
from enum import Enum

import json



# File names
customer_file = 'customer.json'
order_file = 'order.json'

# Ensure JSON files exist
for file in [customer_file, order_file]:
    if not os.path.exists(file):
        with open(file, 'w') as f:
            json.dump({}, f)

class Customer(BaseModel):
    id: Annotated[Optional[str], Field(default=None, example="2025-01", title="Customer ID")]

    name: Annotated[str ,Field(..., title="Name of the customer", max_length=50,description="Name of the customer")]
    Gender: Annotated[Literal['Male','Female','Other'],Field(...,description='gender of the customer')]
    email:Annotated[EmailStr,Field(..., title="Email of the customer", max_length=50,description="Email of the customer")]
    mobile: Annotated[int,Field(..., title="Mobile number of the customer",description="Mobile number of the customer")]
    # @validator('mobile')
    # def validate_mobile(cls, v):
    #     if not v.isdigit() or len(v) != 10:
    #         raise ValueError('Mobile number must be 10 digits long')
    #     return v
      
    @validator('name')
    def validate_name(cls, v):
        if not v.isalpha():
            raise ValueError('Name must contain only alphabetic characters')
        return v


class Category(str, Enum):
    electronics = "electronics"
    groceries = "groceries"
    fashion = "fashion"
    medicine = "medicine"
    furniture = "furniture"
   
class Items(BaseModel):
    
    # order_id: Annotated[str,Field(...,example="Order-2025-01",title="Order ID",description="Order ID")]
    customer_id: Annotated[str,Field(...,example="2025-01",title="Customer ID")]
    item_name: str =Field(..., title="Name of the item", max_length=50)
    price: float =Field(..., title="Price of the item", gt=0)
    quantity: int =Field(..., title="Quantity of the item", gt=0)
    category: Category =Field(..., title="Category of the item",description="Category of the item")
    description: Optional[str] =Field(None, title="Description of the item", max_length=100,description="Description of the item")

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity
    
    @computed_field
    @property
    def total_price_with_discount(self) -> float:
        """Calculate price after applying discount"""
        if self.total_price < 100:
            discount = 0.0  # No discount below $100
        elif 100 <= self.total_price < 500:
            discount = 0.02  # 2% discount
        elif 500 <= self.total_price < 1000:
            discount = 0.04  # 4% discount
        else:
            discount = 0.05  # 5% discount for $1000+
            
        return round(self.total_price * (1 - discount), 2)
    @computed_field
    @property
    def total_price_with_tax(self) -> float:
        """Calculate price after applying tax"""
        if self.category == Category.electronics:
            tax = 0.20
        elif self.category == Category.groceries:
            tax = 0.05
        elif self.category == Category.fashion:
            tax = 0.10
        elif self.category == Category.medicine:
            tax = 0.12
        elif self.category == Category.furniture:
            tax = 0.15
        else:
            tax = 0.18
        return self.total_price_with_discount + (self.total_price * tax)
    


app=FastAPI()

@app.get("/")
async def root():
    return {
        "project_summary": "This FastAPI project manages customers and their item orders. It supports operations like adding, retrieving, and deleting customers and items. The application calculates total prices, discounts, and taxes for items and stores data in JSON files.",
        "endpoints": {
            "/": "Project summary and available endpoints (this endpoint).",
            
            # Customer endpoints
            "/add_customer/ [POST]": "Add a new customer (auto-generates customer ID).", 
            
            "/get_customer/{customer_id} [GET]": "Get details of a specific customer by ID.",

            "/get_all_customers/ [GET]": "Get details of all customers.",

            "/delete_customer/{customer_id} [DELETE]": "Delete a customer by ID.",
            
            # Item/Order endpoints
            "/add_item/ [POST]": "Add a new item for a customer (auto-generates order ID, calculates price, discount, and tax).",
            "/get_item/{order_id} [GET]": "Get item/order details by order ID.",
            
            "/get_all_items/ [GET]": "Get all item/order records.",
            "/delete_item/{order_id} [DELETE]": "Delete an item/order by order ID."
        }
    }

def load_customer_data(customer_file):
    try:
        with open(customer_file, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
            return {}

def save_customer_data(data):
    with open(customer_file, 'w') as f:
        json.dump(data, f, indent=4)

@app.post("/add_customer/")
async def add_customer(customer: Customer):
    customer_data = load_customer_data(customer_file)

    # create customer ID created automatically
    existing_customer_ids = list(customer_data.keys())
    if existing_customer_ids:
        last_id_num = max(int(cid.split('-')[-1]) for cid in existing_customer_ids if '-' in cid)
        new_customer_id = f"2025-{last_id_num + 1}"
    else:
        new_customer_id = "2025-1"
    customer.id = new_customer_id

   
    # Save customer data
    customer_data[customer.id] = {
        "name": customer.name,
        'Gender': customer.Gender,
        "email": customer.email,
        "mobile": customer.mobile,
    }
        

    save_customer_data(customer_data)
    return {
        "message": "Customer added successfully",
        "customer_id": customer.id
    } 


@app.get('/get_customer/{customer_id}')
async def get_customer(customer_id: str):
    data = load_customer_data(customer_file)
    if customer_id not in data:
        raise HTTPException(status_code=404, detail="Customer not found")
    return data[customer_id]
@app.get('/get_all_customers/')
async def get_all_customers():
    data = load_customer_data(customer_file)
    if not data:
        raise HTTPException(status_code=404, detail="No customers found")
    return data
@app.get('/get_item/{order_id}')
async def get_item(order_id: str):
    data = load_order_data(order_file)
    if order_id not in data:
        raise HTTPException(status_code=404, detail="Item not found")
    return data[order_id]
@app.get('/get_all_items/')
async def get_all_items():
    data = load_order_data(order_file)
    if not data:
        raise HTTPException(status_code=404, detail="No items found")
    return data
def load_order_data(order_file):
    try:
        with open(order_file, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
            return {}
def save_order_data(data):
    with open(order_file, 'w') as f:
        json.dump(data, f, indent=4)

@app.post("/add_item/")
async def add_item(item: Items):
    customer_data = load_customer_data(customer_file)

    # Check if customer exists
    if item.customer_id not in customer_data:
        raise HTTPException(status_code=400, detail="Customer not found. Please add customer first.")

    order_data = load_order_data(order_file)

    # Auto-generate order ID
    existing_order_ids = list(order_data.keys())
    if existing_order_ids:
        last_id_num = max(int(oid.split('-')[-1]) for oid in existing_order_ids if '-' in oid)
        new_order_id = f"2025-{last_id_num + 1}"
    else:
        new_order_id = "2025-1"

    # Save item using generated order_id
    order_data[new_order_id] = {
        "customer_id": item.customer_id,
        "item_name": item.item_name,
        "price": item.price,
        "quantity": item.quantity,
        "category": item.category,
        "description": item.description,
        "total_price": item.total_price,
        "total_price_with_discount": item.total_price_with_discount,
        "total_price_with_tax": item.total_price_with_tax
    }

    save_order_data(order_data)

    return {
        "message": "Item added successfully",
        "order_id": new_order_id,
        'total_price': item.total_price,
        'discounted_price': item.total_price_with_discount-item.total_price,
        'total_price_with_tax': item.total_price_with_tax,

    }

@app.delete("/delete_customer/{customer_id}")
async def delete_customer(customer_id: str):
    data = load_customer_data(customer_file)
    if customer_id not in data:
        raise HTTPException(status_code=404, detail="Customer not found")
    del data[customer_id]
    save_customer_data(data)
    return {"message": "Customer deleted successfully"}

@app.delete("/delete_item/{order_id}")
async def delete_item(order_id: str):
    data = load_order_data(order_file)
    if order_id not in data:
        raise HTTPException(status_code=404, detail="Item not found")
    del data[order_id]
    save_order_data(data)
    return {"message": "Item deleted successfully"}

print(Category.electronics)



