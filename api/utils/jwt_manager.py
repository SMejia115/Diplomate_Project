from jwt import encode, decode

pwd = "secretKey"

def create_token(data, secret=pwd):
    return encode(payload=data, key=secret, algorithm="HS256")

def decode_token(token):
    return decode(token, pwd, algorithms=["HS256"])