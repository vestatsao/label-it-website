from fastapi import FastAPI
from pydantic import BaseModel
import math
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Building Physics Calculator API", version="1.0")

# Enable CORS for the Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["localhost", "127.0.0.1", "http://localhost:3000", "http://localhost:3001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CalcRequest(BaseModel):
    expression: str

@app.get("/")
async def health_check():
    return {"status": "Building Physics Calculator API is running"}

@app.post("/api/calc")
async def calculate(request: CalcRequest):
    """
    Calculate a mathematical expression.
    
    Accepts expressions like:
    - "100 + 50"
    - "sqrt(144)"
    - "2**3"
    - "(1500 - 1200) / 1500"
    """
    try:
        # Evaluate the expression safely with restricted builtins
        result = eval(request.expression, {"__builtins__": {}}, {"math": math})
        return {"result": result, "error": None}
    except Exception as e:
        return {"result": None, "error": str(e)}

if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting Building Physics Calculator API on http://localhost:8000")
    print("📊 Calculator ready to accept requests at POST /api/calc")
    uvicorn.run(app, host="0.0.0.0", port=8000)