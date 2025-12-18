from fastapi import FastAPI, Request
from app.middlewares import my_firsy_middleware

app = FastAPI()

app.middleware("http")(my_firsy_middleware)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/users")
async def get_users():
    print("Processing get_users request")
    return {"data": "All users data"}


@app.get("/products")
async def get_products():
    print("Processing get_products request")
    return {"data": "All products data"}
