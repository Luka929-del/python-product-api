from fastapi import FastAPI, HTTPException
from models import Product
from pydantic import BaseModel

app = FastAPI()

class ProductAPI(BaseModel):
    name: str
    category: str
    price: float

@app.post("/product")
async def create_product(product: ProductAPI):
    new_product = Product(product.name, product.category, product.price)
    new_product.create()
    return {"message": "Product created successfully", "id": new_product.id}

@app.put("/product/{id}")
async def edit_product(id: int, product: ProductAPI):
    existing_product = Product.read(id)
    if not existing_product:
        raise HTTPException(status_code=404, detail="Product not found")
    existing_product.name = product.name
    existing_product.category = product.category
    existing_product.price = product.price
    existing_product.update()
    return {"message": "Product updated successfully"}

@app.get("/all_products")
async def get_products():
    products = Product.read_all()
    return [
        {"id": p.id, "name": p.name, "category": p.category, "price": p.price} for p in products
    ]

@app.get("/product/{id}")
async def get_product(id: int):
    product = Product.read(id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"id": product.id, "name": product.name, "category": product.category, "price": product.price}

@app.delete("/product/{id}")
async def delete_product(id: int):
    product = Product.read(id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    Product.delete(id)
    return {"message": "Product deleted successfully"}



