'''Crie um programa que leia o nome de uma
Cidade e diga se ela começa com a palavra "Santo"'''
cidade = str(input('Digite o nome de uma cidade: '))
analise = cidade.split()
analise = 'Santo' in analise[0]
print('{} começa com a palavra "Santo"? {}'.format(cidade, analise))
