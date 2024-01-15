import secrets

def generateSecretKey(length=24):
    return secrets.token_hex(length)
