print("Faça um programa que leia a largura e a altura de uma parede em metros\n e calcule a área e a quantidade necessária para pintá-lo\n sabendo que cada litro de tinta pinta uma área de 2m")
larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = larg * alt
litro = area/2
print('Sua parede têm a dimensão de {}x{}, e sua área é de {}m.\nPara pintá-la, você precisará de {}l'.format(larg, alt, area, litro))
