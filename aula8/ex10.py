#Dado um número, use expressão condicional para averiguar se o número é múltiplo de 3 e 5 ao mesmo tempo.
numero = float(input('digite o numero:  '))

pergunta = (numero%3 ==0) and (numero%5 == 0)
print(f'O número é múltiplo de 3 e 5 ao mesmo tempo? {pergunta}')
