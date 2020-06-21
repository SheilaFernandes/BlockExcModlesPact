def metade(valor):
    resultado = valor /2
    return resultado

def dobro(valor):
    resul = valor * 2
    return resul

def aumentar(value, increase):
    resp = value * (1 + increase/100)
    return resp

def diminuir(value, decrease):
    resp = value * (1 - decrease/100)
    return resp

def moeda(value):
    return f'R${value}'
