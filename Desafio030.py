'''Crie um programa que leia um número inteiro qualquer
e mostre na tela se ele é ímpar ou par'''
numero =  int(input('Digite um número inteiro qualquer:'))
if numero % 2 == 0:
    print('{} é um número PAR'.format(numero))
else:
    print('{} é um número ÍMPAR'.format(numero))
