from cerberus import Validator


def get_login_user_validator(request: any):
    query_param_validator = Validator({
        'user': dict(type='string', required=True ),
        'password': dict(type='string', required=True),
    })
    response = query_param_validator.validate(request.query_params)
    if response is False:
        raise Exception(query_param_validator.errors)

    print(response)
    print(query_param_validator.errors)
    return(response)
