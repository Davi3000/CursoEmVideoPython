'''Faça um programa que leia três números
e mostre qual é o menor e qual é o maior.'''
n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))
if (n1 > n2)and(n1 > n3)and(n2 > n3):
    maior = n1
    menor = n3
elif (n1 > n2)and(n1 > n3)and(n3 > n2):
    maior = n1
    menor = n2
elif (n2 > n1)and(n2 > n3)and(n1 > n3):
    maior = n2
    menor = n3
elif (n2 > n1)and(n2 > n3)and(n3 > n1):
    maior = n2
    menor = n1
elif (n3 > n1)and(n3 > n2)and(n2 > n1):
    maior = n3
    menor = n1
elif (n3 > n1)and(n3 > n2)and(n1 > n2):
    maior = n3
    menor = n2
print('O maior número digitado foi {}, e o menor, {}'.format(maior, menor))
