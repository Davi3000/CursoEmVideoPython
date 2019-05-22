# Este programa irá ler duas notas de um aluno, e retornar a média dele
nome = input('Digite o nome do aluno: ')
nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2
print('A média de {} foi: {}'.format(nome, media))
