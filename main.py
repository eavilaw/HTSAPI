from fastapi import FastAPI, HTTPException, Security, UploadFile, File
from src.Marca import getMarca, getallModeloMarca
from src.Modelo import getModelo
from src.Certificacion import getCertificacion,getCertificacionAll
from fastapi.security import APIKeyHeader
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from fastapi.responses import JSONResponse
from os import getcwd
from src.OrdenaArchivo import ordenararchivo
from src.BandasGSM import getbandasGsm
from src.lteMimo4x4 import get4glte

origins = [
   "http://localhost:3000"
]


api_keys = [
    "my_api_key"
]


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




api_key_header = APIKeyHeader(name="X-API-Key")
def get_api_key(api_key_header: str = Security(api_key_header)) -> str:
    
    if api_key_header in api_keys:
       
        return api_key_header
        
    raise HTTPException(
        status_code='HTTP_401_UNAUTHORIZED',
        detail="Invalid or missing API Key",
    )
@app.get("/protected")
async def protected_route(api_key: str = Security(get_api_key)):
    # Process the request for authenticated users
    return {"message": "Access granted!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

@app.get('/')
async def marca(api_key: str = Security(get_api_key)):
    message=getMarca()
    return(message)

@app.get('/modelo/{modelo}')
async def modelo(modelo,api_key: str = Security(get_api_key)):
    data=getModelo(modelo)
    return(data)

@app.get('/all')
async def allModeloMarca(api_key: str = Security(get_api_key)):
    data=getallModeloMarca()
    return(data)

@app.get('/certificacion/{marca}{modelo}')
async def read_item(marca:int,modelo:int,api_key: str = Security(get_api_key)):
    print(str(marca)+'-'+str(modelo))
    data=getCertificacion(marca,modelo)
    return(data)

@app.get('/certificacionall/')
async def read_item(api_key: str = Security(get_api_key)):
    data=getCertificacionAll()
    return(data)

@app.get('/bandasGsm/')
async def read_item(api_key: str = Security(get_api_key)):
    data=getbandasGsm()
    return(data)
@app.get('/4glte/')
async def read_item(api_key: str = Security(get_api_key)):
    data=get4glte()
    return(data)

@app.post("/multiple/json")
async def upload_files_json(filesjson: List[UploadFile] = File(...)):
    try:
        for file in filesjson:
            with open(getcwd()+'//Files//'+file.filename, "wb") as myfile:
                content =await file.read()
                myfile.write(content)
                myfile.close()
            print(file)
        data=ordenararchivo()
        return JSONResponse(content={"saved":True}, status_code=200)
    except FileNotFoundError:
        
        return JSONResponse(content={"saved":False}, status_code=404)
