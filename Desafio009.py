# Este programa irá ler um valor inteiro e retornar sua tabuada
n = int(input('Quer ver a tabuada de qual número? '))
for cont in range(11):
    print('{} x {} = {}'.format(n, cont, (n*cont)))
