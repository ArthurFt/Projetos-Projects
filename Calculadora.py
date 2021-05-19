escolha = input(
    'Escolha a operação: Soma(1), Subtração(2), Divisão(3), Multiplicação(4)')

if escolha == '1':
    a = int(input('Primeiro número:'))
    b = int(input('Segundo número:'))
    soma = a + b
    print('a soma entre {} e {} é igual a {}'.format(a, b, soma))
if escolha == '2':
    a = int(input('Primeiro número:'))
    b = int(input('Segundo número:'))
    subtracao = a - b
    print('a subtração entre {} e {} é igual a {}'.format(a, b, subtracao))
if escolha == '3':
    a = int(input('Primeiro número:'))
    b = int(input('Segundo número:'))
    divisao = a / b
    resto = a % b
    print('A divisão de {} e {} é igual a {}\n O resto da divisão é {}'.format(
        a, b, divisao, resto))
if escolha == '4':
    a = int(input('Primeiro número:'))
    b = int(input('Segundo número:'))
    multiplicacao = a * b
    print('multiplicar {} e {} é igual a {}'.format(a, b, multiplicacao))
