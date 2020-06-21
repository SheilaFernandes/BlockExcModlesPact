def metade(valor, formato = False):
    if formato == False:
        return valor / 2
    else:
        return f'R$ {(valor / 2):.2f}'.replace('.', ',')

def dobro(valor, formato = False):
    if formato == False:
        return valor * 2
    else:
        return f'R$ {valor/2:.2f}'.replace('.', ',')

def aumentar(value, increase, formato = False):
    if  formato == False:
        return value * (1 + increase/100)
    else:
        return f'R$ {value*(1+increase/100):.2f}'.replace('.', ',')

def diminuir(value, decrease, formato = False):
    if  formato == False:
        return value * (1 - decrease/100)
    else:
        return f'R$ {value*(1-decrease/100):.2f}'.replace('.',',')

def moeda(value, moeda='R$ '):
    return f'{moeda}{value:.2f}'.replace('.',',')

def resumo(preço=0, A=10, R=5):
    msg = 'RESUMO DO VALOR'
    n = 30
    print(f'-'* n)
    print(msg.center(n))
    print(f'-'* n)
    print(f'{"Preço Analisado:"} \t{moeda(preço)}')
    print(f'{"Dobro do preço:"} \t{dobro(preço,True)}')
    print(f'{"Metade do preço:"} \t{metade(preço,True):}')
    print(f'{A}{"% de aumento:"} \t{aumentar(preço,A,True)}')
    print(f'{R}{"% de redução:"} \t{diminuir(preço,R,True)}')
    print('-'* n)

