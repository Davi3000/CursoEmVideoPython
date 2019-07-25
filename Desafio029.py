'''Escreva um programa que leia a velocidade de um carro
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
que ele foi multado.
A multa vai custar R$7.00 por cada Km acima do limite'''
velocidade = float(input('Qual a velocidade seu carro estava quando passou aqui? '))
multa = 7.00
if velocidade > 80:
    kmAcimaDoLimite = velocidade - 80
    multa = multa * kmAcimaDoLimite
    print('Sua multa é de R${:.2f}'.format(multa))
