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
#outra forma de fazer a função moeda, porém utilizando mais variáveis e pode gerar erros ao precisar realizar contas.
'''def moeda(value):
    b = f'{value:.2f}'
    a = str(b)
    return f'R${a.replace(".", ",")}'''

def moeda(value, moeda='R$'):
    return f'{moeda}{value:.2f}'.replace('.',',')
