from fastapi import FastAPI
from models.product import Product

data = [
    Product(id=1,name="Camiseta",description="Descricao do produto 1",price=12.34,in_stock=True),
    Product(id=2,name="Calça",description="Descricao do produto 2",price=12.34,in_stock=True),
    Product(id=3,name="Casaco",description="Descricao do produto 3",price=12.34,in_stock=True),
]

app = FastAPI()

@app.get("/")
def say_hello():
    return {"FastAPI":"Hello"}

@app.get("/{name}")
def say_hi(name:str):
    return {"Hello": f"{name}!"}

@app.get("/api/produtos")
def get_products():
    """
    Retorna todos os produtos
    """
    return data

@app.get("/api/produtos/{id}")
def get_product_by_id(id: int):
    """
    Retorna um produto especifico
    """
    for product in data:
        if product.id == id:
            return product
    return {"message": "Nenhum produto encontrado com o ID fornecido"}
