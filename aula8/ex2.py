#Use uma expressão condicional para verificar se um número é positivo e maior que 100 ou negativo.
numero = int(input("Digite um número: "))
resultado = (numero > 100) or (numero < 0)
print(resultado)