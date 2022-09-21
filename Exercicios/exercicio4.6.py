print('Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.\nCalcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,45 para viagens mais longas.')
print('='*6)
distancia = float(input('Digite quantos Km será sua viagem: '))
distancia_ate_200km = 0.50
distancia_acima_200km = 0.45

if distancia <= 200:
    passagem = distancia * distancia_ate_200km
else:
    passagem = distancia * distancia_acima_200km

print(f'O valor da sua viagem é de R$ {passagem}')