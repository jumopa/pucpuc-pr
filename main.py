from fastapi import FastAPI
import random
from main 
import somar, subtrair, multiplicar, dividir, eh_par
import pytest

# Restante do código dos testes...

app = FastAPI()

@app.get("/helloworld")
async def root():
    return {"message": "Hello World"}

@app.get("/funcaoteste")
async def funcaoteste():
    return {"teste": True, "num_aleatorio": random.randint(0,1000)}
