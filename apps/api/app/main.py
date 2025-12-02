from fastapi import FastAPI

app = FastAPI(title="KODARA API", version="0.1.0")

@app.get("/")
def read_root():
    return {"message": "KODARA está viva! Bem-vindo ao futuro da educação tech."}

@app.get("/health")
def health():
    return {"status": "ok"}
