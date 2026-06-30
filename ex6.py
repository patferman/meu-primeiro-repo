#Crie um programa que leia um caractere e informe se ele é uma vogal ou uma consoante. (Desconsidere diferença de maiúscula e minúscula)

caractere = input("Digite a letra:   ")
if caractere == "a" or caractere =="e" or caractere == "i" or caractere == "o" or caractere == "u" :
	print ("Vogal")
else: 
	print ("Consoante")