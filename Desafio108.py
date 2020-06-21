from Packages import moedas
preço = float(input('Digite um preço: R$ '))
print(f'A metade de {moedas.moeda(preço)} é {moedas.moeda(moedas.dobro(preço))}')
print(f'O dobro de {moedas.moeda(preço)} é {moedas.moeda(moedas.dobro(preço))}')
print(f'Aumentando 10%, o novo preço é {moedas.moeda(moedas.aumentar(preço, 10))}')

