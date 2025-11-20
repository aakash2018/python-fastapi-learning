from fastapi import FastAPI,status

app = FastAPI()

PRODUCTS = [
    {"id": 1, "name": "Laptop", "price": 999.99,"description": "A high-performance laptop.Perfect for work and play."},
    {"id": 2, "name": "Smartphone", "price": 499.99,"description": "A sleek smartphone with a stunning display and powerful features."},
    {"id": 3, "name": "Headphones", "price": 199.99,"description": "Noise-cancelling headphones for an immersive audio experience."},
]  

# GET Request
## Read or Fetch all data
@app.get("/products",status_code=status.HTTP_200_OK)
async def get_products():
    return PRODUCTS

## Read or Fetch All Data
@app.get("/products/{product_id}")
async def single_product(product_id: int):
    for product in PRODUCTS:
        if product["id"] == product_id:
            return product
    return {"error": "Product not found"}

# POST Request
## Create or Insert Data
@app.post("/products",status_code=status.HTTP_201_CREATED)
async def create_product(new_product:dict):
    PRODUCTS.append(new_product)
    return {"status":"created","new_product":new_product}
    

# PUT Request
## Update Complete Data
@app.put("/products/{product_id}")
async def update_product(product_id:int,new_update_product:dict):
    for index, product in enumerate(PRODUCTS):
        if PRODUCTS["id"] == product_id:
            PRODUCTS[index] = new_update_product
            return {"status":"Update","product_id":product_id,
            "new update product":new_update_product}
            
# PATCH Request
## Partial Update Data
@app.patch("/products/{product_id}")
async def partial_product(product_id:int,new_update_product:dict):
    for product in PRODUCTS:
        if product["id"] == product_id:
            product.update(new_update_product)
            return {"status":"Partial Update","product_id":product_id,
            "new update product":new_update_product}

# DELETE Request
## Delete Data
@app.delete("/product/{product_id}")
async def delete_product(product_id:int):
    for index ,product in enumerate(PRODUCTS):
        if product["id"] == product_id:
            PRODUCTS.pop(index)
            return {"status":"Deleted","product_id":product_id}