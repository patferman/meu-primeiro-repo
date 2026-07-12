#Crie um programa que receba três lados de um triângulo e classifique-o como:

#"Equilátero": todos os lados possuem a mesma medida
#"Isósceles": dois lados iguais
#"Escaleno": três lados diferentes

lado1 = float(input("Lado 1:   "))
lado2 = float(input("Lado 2:   "))
lado3 = float(input("Lado 3:   "))
if lado1 == lado2 == lado3:     
    print ("Triangulo Equilatero")
elif lado1 != lado2 != lado3:
    print ("Triangulo Escaleno")
else:   
    print ("Tringulo Isosceles")