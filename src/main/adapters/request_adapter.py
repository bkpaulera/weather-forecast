from fastapi import Request as RequestFastApi
from typing import Callable


def request_adapter(request: RequestFastApi, callback: Callable):
    http_request = {
        'query_params': request.query_params
    }

    try:
        http_response = callable(request)
        return http_response
    except:
        print('Error')
