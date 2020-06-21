def leiaDinheiro(msg):
    """
    >> Recebe um numero e valida se o mesmo é um número válido ou nao. Aceita número tanto com '.' quanto com ','
    :param msg: Texto que o usuário vai visualizar com a instrução a ser realizada.
    o usuário pode digitar com vigurla que o sistema irá aceitar
    :return: valor que o usuário digitou
    """

    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '' or entrada.isalnum():
            print(f'\033[1;31mERRO: \"{entrada}\" é um número inválido\033[m')
        else:
            valido == True
            return float(entrada)
