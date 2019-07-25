'''Desenvolva um programa que pergunte a distância
de uma viagem em KM.
Calcule o preço da passagem, cobrando R$0,50 por KM para
viagens de até 200KM e R$0,45 para viagens mais longas.'''
distancia = float(input('Quantos KM de distância têm seu destino? '))
if distancia > 200:
    passagem = distancia * 0.45
    print('O valor da passagem é R${:.2f}'.format(passagem))
else:
    passagem = distancia * 0.50
    print('O valor da passagem é R${:.2f}'.format(passagem))
