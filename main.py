from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()

nomi = []
class NomePostReq(BaseModel):
    nome: str

@app.get("/")
def saluta():
    return {"text":"ciao"}

@app.get("/nome")
def get_nome():
    if nomi == []:
        raise HTTPException(status_code=404, detail="lista nomi vuota.")
    return nomi

@app.post("/nome")
def post_nome(nomeReq: NomePostReq):
    nomi.append(nomeReq.nome)
    return nomeReq

@app.delete("/nome/{nome}")
def delete_nome(nome: str):
    if nome not in nomi:
        raise HTTPException(status_code=404, detail="nome non trovato.")
    
    nomi.remove(nome)
    return "nome: "+ nome +", cancellato con successo"