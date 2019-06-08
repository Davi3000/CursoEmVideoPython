print('Esse programa irá ler o preço de um produto\n e em seguida retornar seu valor com 5% de deesconto')
produto = float(input('Qual o preço do produto? '))
produtoDesconto = produto*5/100
valorNovo = produto - produtoDesconto
print('O produto que custava R${:.2f}, com o desconto de 5%, passou a custar R${:.2f}'.format(produto, valorNovo))
