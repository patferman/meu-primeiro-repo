#Escreva um programa que leia o salário de um funcionário e calcule o valor do imposto de renda a ser pago, considerando:

#Faixa salarial até R$ 2.000,00: isento
#R$ 2.000,01 até R$ 3.500,00: 10%
#Acima de R$ 3.500,00: 20%.

salario = float(input("digite o salário a calcular:R$   "))
if salario < 2000:  
    print("Isento do pagamento de imposto de renda.")
elif salario >= 3500:
    print(f' O imposto de renda é de R${salario * 0.2}')
else:    
    print (f'O imposto de renda é de R${salario * 0.1}')




