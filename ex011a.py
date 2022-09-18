largura = float(input('Largura: '))
altura = float(input('Altura: '))

area = largura*altura

qtdTinta = area/2

print(f'Sua parede tem a dimensão {largura:.2f}x{altura:.2f} e sua áerea é de {area:.2f}m².')
print(f'Para pintar essa parede, você irá precisar de {qtdTinta:.2f}l de tinta.')
