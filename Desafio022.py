'''Crie um programa que leia o nome completo de uma pessoa
e mostre:
-O nome com as letras maiúsculas
-O nome com as letras minúsculas
-Quantas letras têm sem considerar os espaços
-Quantas letras têm o primeiro nome'''
nome = input('Digite seu nome completo: ')
print('Seu nome em letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome em letras minúsculas é {}'.format(nome.lower()))
nomeSemEspaco = nome.split()
nomeSemEspaco = ''.join(nomeSemEspaco)
print('Seu nome completo têm {} letras.'.format(len(nomeSemEspaco)))
nomePrimeiro = nome.split()
nomePrimeiro = nomePrimeiro[0]
print('Seu primeiro nome têm {} letras'.format(len(nomePrimeiro)))
