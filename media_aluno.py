#Programa que calcula a media das notas de um aluno
#Por aldo

print("\n************************")
print("       MEDIA FINAL      ")
print("************************\n")

#entrada dos dados
nome = input("Nome do aluno: ")
nota1 = float(input("Nota do bimestre 1: "))
nota2 = float(input("Nota do bimestre 2: "))
nota3 = float(input("Nota do bimestre 3: "))
nota4 = float(input("Nota do bimestre 4: "))

#processamento dos dados
media = (nota1 + nota2 + nota3 + nota4) / 4

#condicionais
situacao = ''

if media >= 7 :
    situacao = 'APROVADO !!'

elif media >= 5 and media < 7:
    situacao = 'DE RECUPERAÇÃO'

else :
    situacao = 'REPROVADO !!'

#saída dos dados
print("\n-----------------------\n")
print(f"{nome}, sua nota final é : {media}, e você está {situacao}")
print("\n-----------------------")
