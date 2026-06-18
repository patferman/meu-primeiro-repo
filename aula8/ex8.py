#Verifique se dois números são iguais e se ambos são maiores que 10 usando expressão condicional.
numero1 = float(input('digite o numero 1:   '))
numero2 = float(input('digite o numero 2:   '))
iguais = numero1==numero2
ambos_maiores = numero1>=10 and numero2>=10
print ("Os dois numeros são iguais?" , iguais)
print("Ambos são maiores que 10?" , ambos_maiores)
