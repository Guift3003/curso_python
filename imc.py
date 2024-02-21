#programa pra calcular imc
#desenvolvido por aldoTM
print("*********************************")
print("       CALCULADORA DE IMC       *")
print("*********************************")
print()

#criacao das variaveis
nome = ""
peso = 0
altura = 0.0
imc = 0.0

#entrada dos dados
nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura: "))
peso = int(input("Digite seu peso: "))

#processamento para obter imc
imc = peso / altura**2

situacao = ''

if imc < 18.5:
    situacao = 'Magreza'
    
elif imc >= 18.5 and imc <= 24.9:
    situação = 'Normal'

elif imc >= 25 and imc <= 29.9:
    situação = 'Sobrepeso'

elif imc >= 30 and imc <= 34.9:
    situação = 'Obesidade grau I'

elif imc >= 35 and imc <= 39.9:
    situação = 'Obesidade grau II'

else:
    situação = 'Obesidade grau III'




#saída
print()
print("****************************")
print("*        RESULTADO         *")
print("****************************")
print("*                          *")
print(f"NOME: {nome}")
print(f"PESO: {peso} Kg")
print(f"ALTURA: {altura} m")
print(f"IMC: {imc}")
print(f"Sua situação é: {situação}")


