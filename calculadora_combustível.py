print('-----------------------------------------')
print('         CONSUMO DE COMBUSTÍVEL          ')
print('-----------------------------------------')
print()

# Criando variáveis

modelo_do_veículo = ''
autonomia_do_veículo = 0
distância_percorrida = 0
valor_do_combustível = 0.0
quantidade_combustível_utilizado = 0.0
total_gasto_viagem = 0.0

# Entrada de dados

modelo_do_veículo = input('Modelo do carro? ')
autonomia_do_veículo = int(input('Autonomia do carro? '))
distância_percorrida = int(input('Distância da viagem? '))
valor_do_combustível = float(input('Preço do combustível? '))
print()

# Processando dados

quantidade_combustível_utilizado = distância_percorrida / autonomia_do_veículo
total_gasto_viagem = quantidade_combustível_utilizado * valor_do_combustível


# Saída de dados 


print('-----------------------------------------')
print('            R E S U L T A D O            ')
print('-----------------------------------------')
print()

print('Modelo do veículo: %s ' %(modelo_do_veículo))
print(f'Autonomia do veículo: {autonomia_do_veículo} KM/L')
print('Distância percorrida: ' + str(distância_percorrida) + ' KM')
print('Valor do combustível: ' + str(valor_do_combustível))
      
print('-----------------------------------------')      
print('Quantidade de combustível utilizado: %.2f'  % quantidade_combustível_utilizado)
print(f'Total gasto com a viagem: R$ {total_gasto_viagem: .2f}')
print('-----------------------------------------')


