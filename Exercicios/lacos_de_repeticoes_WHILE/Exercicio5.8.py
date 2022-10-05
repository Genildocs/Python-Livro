print('Escreva um programa que leia dois números.'
      '\nImprima o resultado da multiplicação do primeiro pelo segundo.'
      '\nUtilize apenas os operadores de soma e subtração para calcular o resultado.'
      '\nLembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles.')
print('Assim, 4 × 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.')
print('-'*30)
numero1=int(input('Digite um numero: '))
numero2=int(input('Digite outro numero: '))
x = 2
r = 0
while x <= numero2:
    r = r + numero1
    x = x + 1

    print(r)

print(f'{numero1} x {numero2} = {r}')