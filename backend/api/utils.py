from random import choice

ID_size = 32

def getID():
    return "".join([choice("0123456789") for _ in range(ID_size)])

