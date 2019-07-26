'''Desenvolva um programa que leia o comprimento de
três retas e diga ao usuário se elas podem ou não
formar um trângulo.'''
print('-=-'*20)
print('ANALISADOR DE TRIÂNGULOS')
print('-=-'*20)
r1 = float(input('1º segmento: '))
r2 = float(input('2º segmento: '))
r3 = float(input('3º segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1+ r2:
    print('Os seguimentos digitados formam um triângulo.')
else:
    print('Os seguimentos digitados não formam um triângulo.')
