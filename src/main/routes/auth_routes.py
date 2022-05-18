from fastapi import APIRouter, Request as RequestFastAPI
from src.validations.get_login_user_validator import get_login_user_validator
from src.main.adapters.request_adapter import request_adapter

auth_routes: APIRouter = APIRouter()


@auth_routes.get('/api/login')
def get_login_user(request: RequestFastAPI):
    # print(request.query_params['user'])
    # print(request.query_params['password'])
    valid = get_login_user_validator(request)
    red = request_adapter(request,print)
    if valid:

        return {"Message": "Funcionou"}
    else:

        return {"Message": "fail"}
