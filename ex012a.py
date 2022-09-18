valorProduto = float(input('Digite o valor do produto: R$ '))

novoValor = valorProduto-valorProduto*5/100

print(f'O produto que custava R$ {valorProduto:.2f}, com desconto de 5% vai custar R$ {novoValor:.2f}')
