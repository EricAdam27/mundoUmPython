diasAlugados = int(input('Quantos dias alugados? '))
kmRodados = int(input('Quantos Km rodados? '))

valorDiaria = 60.0
valorKm = 0.15

total = (diasAlugados*valorDiaria)+(kmRodados*valorKm)

print(f'O total a pagar é R$ {total:.2f}')
