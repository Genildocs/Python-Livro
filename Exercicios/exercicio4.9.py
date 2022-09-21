print('Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.\nO programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar.\nO valor da prestação mensal não pode ser superior a 30% do salário.'
      '\nCalcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.')
print('='*10)
valor_da_casa = float(input('Qual o valor da casa que deseja comprar: '))
seu_salario = float(input('Qual seu salario: '))
anos_para_pagar = int(input('Digite a quantidades de anos para pagar: '))
prestacao_mensal = valor_da_casa / (anos_para_pagar * 12)
salario_porcentagem = seu_salario * (30/100)
print('-'*30)
if salario_porcentagem < prestacao_mensal:
    print(f'Seu salario é R$ {seu_salario} e 30% dele é R$ {salario_porcentagem:.1f}')
    print(f'Você não pode comprar a casa, pois a prestação mensal de R$ {prestacao_mensal:.1f} ultrapassa 30% do seu salario.')
else:
    print(f'Seu salario é R$ {seu_salario} e 30% dele é R$ {salario_porcentagem:.1f}')
    print(f'Você pode comprar a casa, pois a prestação mensal de R$ {prestacao_mensal:.1f} não ultrapassa 30% do seu salario.')


