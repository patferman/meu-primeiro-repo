#Dada uma nota de 0 a 10, verifique se o aluno foi aprovado usando uma expressão condicional. A aprovação requer uma nota maior ou igual a 6.
nota = float(input('Digite a nota do aluno: '))
aprovado = (nota >= 6)  
print(f'O aluno foi aprovado? {aprovado}')
