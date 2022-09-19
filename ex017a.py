import math

catetoOposto = float(input('Comprimento do cateto oposto: '))
catetoAdjacente = float(input('Comprimento do cateto adjacente: '))

hipotenusa = math.hypot(catetoOposto, catetoAdjacente)
# hipotenusa = math.sqrt(pow(catetoOposto, 2)+pow(catetoAdjacente, 2))

print(f'A hipotenusa vai medir {hipotenusa:.2f}')
