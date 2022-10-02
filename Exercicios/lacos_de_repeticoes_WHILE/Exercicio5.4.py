print('imprimir de 1 até o número digitado pelo usuário, e mostrar apenas os números ímpares.')
print('-'*30)
usuario = int(input('Digite um numero inteiro: '))
x = 1
while x <= usuario:
    if x % 2 == 1:
        print(x)
    x = x + 1