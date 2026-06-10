from plot import generate_plot
from fastapi import FastAPI
from pydantic import BaseModel
from validator import validate

app = FastAPI(
    title="Math Validator API",
    description="API do walidacji równań matematycznych (składnia, algebra, logika, topologia, numeryka)",
    version="1.0.0"
)

class Equation(BaseModel):
    equation: str

@app.post("/validate")
def validate_equation(data: Equation):
    result = validate(data.equation)
    return {
        "input": data.equation,
        "result": result
    }

@app.post("/plot")
def plot_equation(data: Equation):
    img = generate_plot(data.equation)
    return {
        "input": data.equation,
        "image_base64": img
    }
