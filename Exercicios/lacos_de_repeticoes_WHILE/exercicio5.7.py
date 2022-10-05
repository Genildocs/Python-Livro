print('Tabuada')
print('-'*30)
n=int(input('Tabuada de: '))
x=int(input('Digite um numero para iniciar a tabuada: '))
final = int(input('Digite um numero para o fim da tabuada: '))
while x <= final:
    print(f'{n} x {x} = {x*n}')
    x = x + 1