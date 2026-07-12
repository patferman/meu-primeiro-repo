#Escreva um programa que simule uma calculadora simples. O programa deve receber dois números e uma operação (+, -, *, /). O resultado da operação deve ser exibido.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Solicita a operação
operacao = input("Digite a operação (+, -, *, /): ")

# Verifica qual operação foi escolhida
if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: divisão por zero!"
else:
    resultado = "Operação inválida!"

# Exibe o resultado
print("Resultado:", resultado)
