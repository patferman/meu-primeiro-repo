#Considerando idade e renda. Crie uma expressão booleana para verificar se a pessoa pode solicitar um empréstimo, considerando que ela deve ser maior de idade e ter renda de pelo menos R$ 2000,00.

idade = int(input('Digite a idade da pessoa: '))
renda = float(input('Digite a renda da pessoa: '))
pode_solicitar = (idade >= 18) and (renda >= 2000)
print(f'A pessoa pode solicitar um empréstimo? {pode_solicitar}')
