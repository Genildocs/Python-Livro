import time

print('Faça um programa para escrever a contagem regressiva do lançamento de um foguete.'
      '\nO programa deve imprimir 10, 9, 8, …, 1, 0 e Fogo! na tela.')
print('-'*20)
x = 10
while x >= 0:
    print(x)
    time.sleep(1)
    x = x - 1
print('FOGO!')