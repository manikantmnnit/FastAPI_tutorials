# 🧾 Customer & Item Management API
**This is a FastAPI-based RESTful API that allows users to manage customer and item (order) data. It supports CRUD operations and calculates prices, discounts, and taxes based on the item category.**


## Features
       - Add, retrieve, and delete **customers**
    - Add, retrieve, and delete **items/orders**
    - Automatically calculates:
  - **Total price**
  - **Discount** (based on category)
  - **Tax** (fixed percentage)
    - Stores data in local **JSON files**
    - Fully typed and validated using **Pydantic models**



## 📮 API Endpoints

### 🔹 Root

- `GET /`  
  Returns a summary of the project and all available endpoints.

---

### 👤 Customer Endpoints

- `POST /add_customer/`  
  Add a new customer (auto-generates a customer ID).

- `GET /get_customer/{customer_id}`  
  Get a specific customer by ID.

- `GET /get_all_customers/`  
  Get all customers.

- `DELETE /delete_customer/{customer_id}`  
  Delete a customer by ID.

---

### 📦 Item/Order Endpoints

- `POST /add_item/`  
  Add a new item/order (auto-generates order ID and calculates price, discount, and tax).

- `GET /get_item/{order_id}`  
  Get a specific item/order by ID.

- `GET /get_all_items/`  
  Get all items/orders.

- `DELETE /delete_item/{order_id}`  
  Delete an item/order by ID.

##  Running the App
pip install fastapi uvicorn
uvicorn main:app --reload


- Open in browser: 
http://127.0.0.1:8000/docs