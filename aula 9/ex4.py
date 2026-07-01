#Crie um programa que leia a temperatura em graus Celsius e informe se está "Frio" (abaixo de 18°C), "Agradável" (entre 18°C e 26°C) ou "Quente" (acima de 26°C).

Temperatura = float(input('Digite a temperatura:   °C'))
if Temperatura < 18:
	print ("Frio")
elif Temperatura > 26:
	print ("Quente")
else:
	print ("Agradável")