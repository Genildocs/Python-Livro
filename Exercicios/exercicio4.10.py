print('Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e '
      '\no tipo de instalação: R para residências, I para indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir.')
print('+',  '-'*30, '+',
      '\nPreço por tipo e faixa de consumo'
      '\nTipo        | Faixa (kWh)   | Preço  '
      '\nResidencial:  até R$ 500 preço de R$ 0,40, acima de 500 preço de R$ 0,65'
      '\nComercial:    até R$ 1000 preço de R$ 0,55, acima de 1000 preço de R$ 0,60'
      '\nIndustrial:   até R$ 5000 preço de R$ 0,55, acima de 5000 preço de R$ 0,60')
print('+',  '-'*30, '+')

consumo = float(input('Por favor me informe a quantidade de energia em kWh consumida: '))
tipo_instalacao = input('Qual seu tipo de instalação: R para residências, I para indústrias e C para comércios. ').upper()

if tipo_instalacao == 'R' and consumo <= 500 :
    total = consumo * 0.40
    print(f'O valor a ser pago é {total:.2f} para instalação residêncial.')
elif tipo_instalacao == 'R' and consumo > 500:
    total = consumo * 0.65
    print(f'O valor a ser pago é {total:.2f} para instalação residêncial.')
elif tipo_instalacao == 'C' and consumo <= 1000:
    total = consumo * 0.55
    print(f'O valor a ser pago é {total:.2f} para instalação comercial.')
elif tipo_instalacao == 'C' and consumo > 1000:
    total = consumo * 0.60
    print(f'O valor a ser pago é {total:.2f} para instalação comercial.')
elif tipo_instalacao == 'I' and consumo <= 5000:
    total = consumo * 0.55
    print(f'O valor a ser pago é {total:.2f} para instalação industrial.')
elif tipo_instalacao == 'I' and consumo > 5000:
    total = consumo * 0.60
    print(f'O valor a ser pago é {total:.2f} para instalação industrial.')
else:
    tipo_instalacao != 'R' and 'C' and 'I'
    print("Erro ! Tipo de instalação desconhecido!")