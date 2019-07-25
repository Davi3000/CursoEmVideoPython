'''Escreva um programa que faça o pc "pensar" em
um número entre 0 a 5 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo pc  '''
from random import randint
numero = randint(0,5)
chute = int(input('Qual número entre 0 e 5 eu escolhi? '))
if chute == numero:
    print('PARABÉNS! VOCÊ ACERTOU!')
else:
    print('Que pena, parece que eu venci.')
