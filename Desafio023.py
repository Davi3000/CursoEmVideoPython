'''Faça um programa que leia um número de 0 a 9999
e mostre na tela cada um dos dígitos separados.'''
numero = input('Digite um número: ')
unidade = numero[3]
dezena = numero[2]
centena = numero[1]
milhar = numero[0]
print("""O número {} têm: 
Unidades:{}
Dezenas:{}
Centenas:{}
Milhars:{}""".format(numero, unidade, dezena, centena, milhar))
