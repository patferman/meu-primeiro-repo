#Escreva um programa que simule uma calculadora simples. O programa deve receber dois números e uma operação (+, -, *, /). O resultado da operação deve ser exibido.
numero1 = float(input("numero 1:  "))
numero2 = float(input("numero 2:  "))
operacao = input(" Digitar a operação: ")
if operacao == "+":
    print (numero1 + numero2)
elif operacao == '-':
    print (numero1 - numero2)
elif operacao == '*':
    print (numero1 * numero2)
elif operacao == '/':
    print (numero1 /numero2)
else:
    print("operação inválida")   
