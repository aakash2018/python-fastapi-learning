from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Hello, World!"}

@app.get("/product")
async def all_products():
    return {"response": "All Products"}

##Read or Fetch a single product
# @app.get("/product/{product_id}")
# async def single_product(product_id: int):
#     return {"response": f"Single Product with ID: {product_id}"}

# POST Request
## Create Or Insert a new product
@app.post("/product")
async def create_product(new_product: dict):
    # return {"response": f"Create a new Product : {new_product}"}
    return {"response":"product created successfully","new Product":new_product}
# PUT Request
## Update an existing product
@app.put("/product/{product_id}")   
async def update_product(product_id: int, new_updated_product: dict):
    return {"response": f"Update Product with ID: {product_id}", "updated Product": new_updated_product}

#PATCH Request
## Update partially an existing product
@app.patch("/product/{product_id}")
async def partial_update_product(product_id: int, new_partial_product: dict):
    return {"response": f"Partially Update Product with ID: {product_id}", "partially updated Product": new_partial_product}

# DELETE Request
## Delete an existing product
@app.delete("/product/{product_id}")
async def delete_product(product_id: int):
    return {"response": f"Delete Product with ID: {product_id}"}    

## Order Matters
@app.get("/product/rode_nt_usb")
async def single_product_static():
    return {"response": "Single Data fetch"}

## Paramter with Type
@app.get("/product/{product_title}")
async def single_product(product_title: str):
    return {"response": "Single Product with ID:", "product_title":product_title}

