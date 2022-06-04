from fastapi import APIRouter, Request as RequestFastAPI
from fastapi import Depends, status
from src.validations.get_login_user_validator import get_login_user_validator
from src.main.adapters.request_adapter import request_adapter
from src.main.config.env_config import get_settings, Settings

auth_routes: APIRouter = APIRouter()

#Realiza o Login
@auth_routes.get('/api/login')
def get_login_user(request: RequestFastAPI, user: str, password: str):
    # print(request.query_params['user'])
    # print(request.query_params['password'])
    valid = get_login_user_validator(request)
    red = request_adapter(request, print)
    if valid:
        return {"Message": "Funcionou"}
    else:
        return {"Message": "fail"}

#Registra um novo usuario
@auth_routes.post('/api/registration',status_code=status.HTTP_201_CREATED)
def registration_user(request: RequestFastAPI, user: str, password: str):
    # print(request.query_params['user'])
    # print(request.query_params['password'])
    valid = get_login_user_validator(request)
    red = request_adapter(request, print)
    if valid:
        return {"Message": "Usuario criado"}
    else:
        return {"Message": "Falha em criar o user"}

#faz o logout do usuario
@auth_routes.put('/api/logout/')
def logout_user(request: RequestFastAPI, user_id: str):
    return {"Message": "Logout"}

#Atualiza o password do usuario
@auth_routes.put('/api/login/')
def update_user(request: RequestFastAPI, user_id: str, password: str):
    return {"Message" : "Password Alterado"}

#Deleta o usuario
@auth_routes.delete('/api/login')
def delete_user(request: RequestFastAPI, user: str, password: str):
    return {"Message" : "Usuario deletado"}

@auth_routes.get("/ping")
async def ping(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing
    }
