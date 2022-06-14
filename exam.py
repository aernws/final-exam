from email import message
from fastapi import FastAPI

app1 = FastAPI()
buyers={}
products={}


@app1.get("/buyers")
async def getbuyers():
    return{buyers}

@app1.get("/products")
async def getproducts():
    return{products}

@app1.post("/buyers?name=")
async def addbuyer(BUYER_NAME: str):
    message = "Duplicate entry"
    if BUYER_NAME not in buyers:
        message = "OK"
        buyers[BUYER_NAME]
    return{"Result": message}

@app1.post("/products?name=")
async def addproduct(PRODUCT_NAME: str):
    message = "Duplicate entry"
    if PRODUCT_NAME not in products:
        message = "OK"
        products[PRODUCT_NAME]
    return{"Result": message}

@app1.post("/buyers/{BUYER_NAME}?prod_name={PRODUCT_NAME}")
async def buy(BUYER_NAME: str, PRODUCT_NAME: str, count: int = 1):
    if BUYER_NAME in buyers:
        if PRODUCT_NAME in products:
            message = "OK"
            count = count + 1
            buyers[BUYER_NAME] = PRODUCT_NAME, count
        else:
            message = "Error: no product",PRODUCT_NAME
    else:
        message = "Error: no buyer",BUYER_NAME
    return{"result": message}

@app1.get("/buyers/","/purchased")
async def getbuy(BUYER_NAME:str):
    if BUYER_NAME in buyers:
        message = buyers[BUYER_NAME]
    else:
        message = "Error: no buyer", BUYER_NAME
    return{"result": message}
