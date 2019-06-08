km = float(input('Quantos Km foram rodados? '))
dias = int(input('Quantos dias o carro ficou alugado? '))
carro = 60
print('O total a pagar é R${:.2f}'.format(carro*dias+km*0.15))
