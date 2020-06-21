from UtilidadesCev import moeda
from UtilidadesCev import dado

p = dado.leiaDinheiro('Digite o preço: R$ ')
acrescimo = float(input('Digite um percentual (%) de aumento [não digite o simbolo %] >> '))
redução = float(input('Digite um percentual (%) de redução [não digite o simbolo %] >> '))

moeda.resumo(p, acrescimo, redução)