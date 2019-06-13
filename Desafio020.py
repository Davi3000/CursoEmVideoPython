'''Faça um programa que leia o nome
dos quatro alunos e mostre a ordem sorteada'''
from random import shuffle
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno:')
n4 = input('Quarto aluno: ')
listas = [n1, n2, n3, n4]
shuffle(listas)
print('A ordem de apresentação de trabalhos é:\n{}'.format(listas))
