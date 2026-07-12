#Escreva um programa que leia um número e informe se ele é:
#múltiplo de 2 e de 3 ao mesmo tempo

#apenas múltiplo de 2

#apenas múltiplo de 3
#não é múltiplo de nenhum dos dois

numero = int(input("Digite um número: "))
if numero %2 == 0 and numero % 3 == 0:
	print("múltiplo de 2 e de 3 ao mesmo tempo")

elif numero % 2 == 0 and numero % 3 != 0:
	print ("numero é apenas múltiplo de 2.")
elif numero %3 == 0 and numero % 2 != 0:
	print (	"numero é apenas múltiplo de 3")
else:
	 print ("numero não é múltiplo de nenhum dos dois")
	


