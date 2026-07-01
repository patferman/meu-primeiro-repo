#Crie um programa que leia um ano e informe se ele é bissexto.

#De 4 em 4 anos é ano bissexto.
#De 100 em 100 anos não é ano bissexto.
#De 400 em 400 anos é ano bissexto.
#Prevalecem as últimas regras sobre as primeiras.
#Exemplos:
#bissextos: 1996, 2000, 2004, 2008...
#não bissextos: 1800, 1900, 1997, 1998, 1999...


ano = int(input("Digite o ano:   "))
if ano % 400 == 0:
    print ("ano bissexto")
elif ano % 100 == 0:
    print('O ano não é bissexto')
elif ano % 4 == 0:
    print ("O ano é bissexto")
else:
    print("o ano não é bissexto")