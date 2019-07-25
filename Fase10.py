nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
media = (nota1 + nota2)/2
if media >= 6.0:
    print('Sua média foi boa, parabéns. {:.1f}'.format(media))
else:
    print('Sua média não foi boa, estude mais. {:.1f}'.format(media))
