import requests



cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()
cotacao_dolar = cotacoes['USDBRL']['bid']
cotacao_euro = cotacoes['EURBRL']['bid']
print(f'Valor atual do dolar: R$ {cotacao_dolar}.')
print(f'Valor atual do euro: R$ {cotacao_euro}.')
