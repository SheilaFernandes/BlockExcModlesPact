from Packages import moedas2
p = float(input('Digite o preço>> R$ '))
acrescimo = float(input('Digite um percentual (%) de aumento [não digite o simbolo %] >> '))
redução = float(input('Digite um percentual (%) de redução [não digite o simbolo %] >> '))

moedas2.resumo(p, acrescimo, redução)