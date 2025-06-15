from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"mensagem": "API da CED Brasil rodando via CapRover!"}
