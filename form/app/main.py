from fastapi import FastAPI,Form
from fastapi.responses import HTMLResponse
from typing import Annotated

app=FastAPI()

## call default
@app.get("/")
async def home():
    return "Helloworld"

# # Simple Html form for testing
@app.get("/handleFormData",response_class=HTMLResponse)
async def get_form():
    return """
    <html>
        <body>
        <h2>Login Form</h2>
        <form action="/login/" method="post">
            <label for="username">Username:</label>
            <br>
            <input type="text" id="username" name="username">
            <br>
            <label for="password">Password:</label>
            <br>
            <input type="password" id="password" name="password">
            <br>
            <br>
            <input type="submit" value="Submit">
        </form>
    """

# @app.post("/login/")
# async def login(username:Annotated[str,Form()],password:Annotated[str,Form()]):
#     return {"usernane":username,"password_length":len(password)}


@app.post("/login/")
async def login(username:Annotated[str,Form(min_length=3)],
                password:Annotated[str,Form(min_length=3,max_length=10)]):
    return {"usernane":username,
            "password_length":len(password)}