print('Escreva um programa que leia três numeros e que imprima o maior e o menor.')
print('='*6)
numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))
numero3 = int(input('Digite o terceiro numero: '))

maior = numero1

if numero2 > numero1 and numero3:
    maior = numero2
if numero3 > numero1 and numero1:
    maior = numero3


menor = numero1

if numero2 < numero3 and numero2 < numero1:
    menor = numero2
if numero3 < numero2 and numero3 < numero1:
    menor = numero3

print(f'O maior numero é {maior}')
print(f'O menor numero é {menor}')