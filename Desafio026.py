'''Crie um programa que leia uma frase e
mostre quantas vezes aparece a letra "A", em que posição
aparece a primeira e última vez'''
frase = str(input('Digite um frase qualquer: '))
fraseUpper = frase.upper()
fraseUpper = fraseUpper.strip()
print("""Depois de analisar a frase '{}', foi descoberto as seguites informações:
A letra 'A' aparece {} vezes 
A primeira vez na {}ª posição
 E na última vez na {}ª posição""".format(frase, fraseUpper.count('A'), fraseUpper.find('A')+1, fraseUpper.rfind('A')+1 ))
