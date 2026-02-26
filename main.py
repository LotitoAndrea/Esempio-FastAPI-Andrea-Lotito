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

@app.patch("/nome/{nomeVecchio}/{nomeNuovo}")
def patch_nome(nomeVecchio: str, nomeNuovo: str):
    if nomeVecchio not in nomi:
        raise HTTPException(status_code=404, detail="nome non trovato.")
    
    nomi.remove(nomeVecchio)
    nomi.append(nomeNuovo)
    return "nome vecchio '"+ nomeVecchio +"', sovrascritto con nome nuovo '"+ nomeNuovo + "'."

@app.delete("/nome/{nome}")
def delete_nome(nome: str):
    if nome not in nomi:
        raise HTTPException(status_code=404, detail="nome non trovato.")
    
    nomi.remove(nome)
    return "nome: "+ nome +", cancellato con successo"