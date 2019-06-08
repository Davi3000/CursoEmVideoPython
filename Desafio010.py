# Este programa irá ler um valor x, e retornar quanto uma pessoa pode comprar de dólares
real = float(input('Quantos reais você têm? '))
dolar = real/3.85
euro = real/4.35
iene = real/0.036
print('Com R${:.2f} você pode comprar:\nU${:.2f}\n€{:.2f} \n¥{:.2f}'.format(real, dolar, euro, iene))
