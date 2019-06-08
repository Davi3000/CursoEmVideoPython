print('Este programa irá ler o salário de um funcionário\n  e em seguida retornar seu novo salário\n com 15% de aumento')
salario = float(input('Digite o seu salário atual: R$'))
novo = salario + (salario*15/100)
print('Seu novo salário é de R${:.2f}'.format(novo))
