from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.controllers.auth_controller import AuthController

router = APIRouter(prefix='/api/auth', tags=['autenticação'])
controller = AuthController()


class Login(BaseModel):
    nome: str
    senha: str


@router.post('/login')
def login(dados: Login):
    usuario = controller.login(dados.nome, dados.senha)

    if usuario is None:
        raise HTTPException(401, 'nome ou senha inválidos')

    return usuario