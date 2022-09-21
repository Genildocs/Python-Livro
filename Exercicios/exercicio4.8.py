print('Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar.\nVocê deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.')
print('='*10)
numero1 = float(input('Digite o primeiro numero: '))
numero2 = float(input('Digite o segundo numero: '))
operacao = int(input('Digite qual operacao deseja realizar: \n'
                 '1 = Soma \n'
                 '2 = Subtração \n'
                 '3 = Multiplicação \n'
                 '4 = Divisão \n'))
if operacao == 1:
    print(f'Soma é {numero1 + numero2}')
elif operacao == 2:
    print(f'Subtração é {numero1-numero2}')
elif operacao == 3:
    print(f'Multplicação é {numero1*numero2}')
elif operacao == 4:
    print(f'Divisão é {numero1 / numero2:.1f}')
else:
    print('Numero de operação invalido.')