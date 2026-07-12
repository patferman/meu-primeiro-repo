#Escreva um programa que receba a quantidade de faltas de um aluno e sua nota. Se a nota for maior ou igual a 60 e as faltas forem menores ou iguais a 5, imprima "Aprovado". Caso contrário, imprima "Reprovado".

nota = float(input("Digite a nota:  "))
faltas = int(input("Digite as faltas:  "))

if nota >= 6 and faltas <=5:
	print("Aprovado")
else:
	print ("Reprovado")