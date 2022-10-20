from fastapi import APIRouter, Body, HTTPException

from models.UsuarioModel import UsuarioCriarModel
from services.UsuarioSevice import (
    registrar_usuario
)
router = APIRouter()

@router.post("/", response_description="Rota para criar um novo Usuário")
async def rota_criar_usuario(usuario : UsuarioCriarModel = Body (...)):
    resultado = await registrar_usuario(usuario)

    if not resultado['status'] == 201:
        raise HTTPException(status_code=resultado['status'],detail=resultado['mensagem'])

    return resultado