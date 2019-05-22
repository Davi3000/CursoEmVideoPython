# Este programa irá ler um valor x, e retornar quanto uma pessoa pode comprar de dólares
real = float(input('Quantos reais você têm? '))
dolar = real/3.27
print('Com R${:.2f} você pode comprar U${:.2f}'.format(real, dolar))
