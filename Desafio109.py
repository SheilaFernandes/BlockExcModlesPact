from Packages import moedas2
preço = float(input(f'Digite um preço: R$ '))
print(f'A metade de {moedas2.moeda(preço)} é R$ {moedas2.metade(preço,True)}')
print(f'O dobro de {moedas2.moeda(preço)} é R$ {moedas2.dobro(preço,True)}')
print(f'Aumentando 10%, o novo preço é R$ {moedas2.aumentar(preço, 10,True)}')
print(f'Reduzindo 13%, o novo preço é R$ {moedas2.diminuir(preço, 13, True)}')
