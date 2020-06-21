def metade(valor=0, formato = False):
    """
    >> Calcula a metade de número
    :param valor: valor a ser calculado a metade do mesmo.
    :param formato: Campo opcional. Caso desejar visualizar no formato de moeda (R$) com 2 casas decimais, preencher 'True'
    :return: metade do valor digtiado.
    """
    if formato == False:
        return valor / 2
    else:
        return f'R$ {(valor / 2):.2f}'.replace('.', ',')

def dobro(valor=0, formato = False):
    """
    >> Calcula o dobro de um número
    :param valor: valor a ser calculado o dobro do mesmo.
    :param formato: Campo opcional. Caso desejar visualizar no formato de moeda (R$) com 2 casas decimais, preencher 'True'
    :return: retorna o dobro do valor.
    """
    if formato == False:
        return valor * 2
    else:
        return f'R$ {valor/2:.2f}'.replace('.', ',')

def aumentar(value=0, increase=10, formato = False):
    """
    >> Aumenta o valor em 10% ou de acordo com o % informado na função.
    :param value: valor a ser calculado o aumento.
    :param increase: % a ser aumento no valor escolhido. Se o campo não for preenchido por padrão aumentará 10%.
    :param formato: Campo opcional. Caso desejar visualizar no formato de moeda (R$) com 2 casas decimais, preencher 'True'
    :return: retorna o valor com o % de aumento digitado (ou 10% de aumento caso não tiver preenchido nada).
    """
    if  formato == False:
        return value * (1 + increase/100)
    else:
        return f'R$ {value*(1+increase/100):.2f}'.replace('.', ',')

def diminuir(value=0, decrease=5, formato = False):
    """
    >> Reduz o valor em 5% ou de acordo com o % informado na função.
    :param value: valor a ser calculado o aumento.
    :param decrease: % a ser reduzido no valor escolhido. Se o campo não for preenchido por padrão aumentará 5%.
    :param formato: Campo opcional. Caso desejar visualizar no formato de moeda (R$) com 2 casas decimais, preencher 'True'
    :return: retorna o valor com % de redução digitado (ou 5% de redução caso não tiver preenchido nada);
    """
    if  formato == False:
        return value * (1 - decrease/100)
    else:
        return f'R$ {value*(1-decrease/100):.2f}'.replace('.',',')

def moeda(value, moeda='R$ '):
    """
    >> Função para formatar um número como moeda.
    :param value: valor a ser formatado
    :param moeda: campo opcional. Por padrão preenche a moeda em real (R$) caso desejar utilizar outra moeda é só preencher
    entre aspas simples ou duplas qual a moeda a ser mostrada.
    IMPORTANTE... NÃO FAZ CONVERSÃO SOMENTE MOSTRA O SIMBOLO DA MOEDA DESEJADA
    :return: Retorna o valor com formato em moeda.
    """
    return f'{moeda}{value:.2f}'.replace('.',',')

def resumo(preço=0, A=10, R=5):
    """
    >> Todas as funções acima agrupada em uma só e mostra todos os resultados em forma de tabela
    :param preço: Preço a ser analisado
    :param A: Campo opcional. % de aumento, caso nao seja preenchido, por padrão é considerado 10%
    :param R: Campo opcional. % de redução, caso não seja preenchdido, por padrão é considerado 5%
    :return: retorna o preço analisado, dobro, metade, aumento e redução formato em tabela.
    """
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