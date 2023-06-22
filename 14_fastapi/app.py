from fastapi import FastAPI
from pydantic import BaseModel

class HelloResp(BaseModel):
    message: str

class Product(BaseModel):
    name: str
    desc: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()
app.counter = 0

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello/{name}", response_model=HelloResp)
async def hello_name(name: str):
    return HelloResp(message=f"Hello {name}")

@app.get("/counter")
async def counter():
    app.counter += 1
    return f"Counter = {app.counter}"

@app.post("/item")
async def create_item(item: Product):
    if item.tax == None:
        item.tax = 0
    return f"Name: {item.name}, gross: {item.price + item.tax}"


