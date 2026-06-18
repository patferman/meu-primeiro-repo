#Receba dois números e verifique se pelo menos um deles é negativo com expressão condicional.
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))    
tem_negativo = (num1 < 0) or (num2 < 0)
print(f'Pelo menos um dos números é negativo? {tem_negativo}')