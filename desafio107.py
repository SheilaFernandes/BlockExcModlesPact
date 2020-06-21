from Packages import moedas
preço = float(input(f'Digite um preço: R$ '))
print(f'A metade de {preço} é R$ {moedas.metade(preço)}')
print(f'O dobro de {preço} é R$ {moedas.dobro(preço)}')
print(f'Aumentando 10%, o novo preço é R$ {moedas.aumentar(preço, 10)}')
print(f'Reduzindo 13%, o novo preço é R$ {moedas.diminuir(preço, 13)}')
