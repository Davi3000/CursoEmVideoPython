'''Escreva um programa que pergunte o salário de
 um funcionário e calcule o valor do seu aumento
 Para salários superiores a R$1.250,00, calcule um  aumento de 10%
 Para os inferiores ou iguais, o aumento é de 15%'''
sal = float(input('Qual o seu salário atual? R$'))
if sal <= 1250:
    aumento = sal*15/100
    novoSal = sal + aumento
    print('Seu novo salário é de R${:.2f}'.format(novoSal))
else:
    aumento = sal*10/100
    novoSal = sal + aumento
    print('Seu novo salário é de R${:.2f}'.format(novoSal))
