mensagem = input('Digite algo: ')

print(f'\nTipo primitivo: {type(mensagem)}')
print(f'Só tem espaço? {mensagem.isspace()}')
print(f'É um número? {mensagem.isnumeric()}')
print(f'É alfabético? {mensagem.isalpha()}')
print(f'É alfanumérico? {mensagem.isalnum()}')
print(f'Todas letras estão maiúsculas? {mensagem.isupper()}')
print(f'Todas letras estão minúsculas? {mensagem.islower()}')
print(f'Está no formato capitalizado? {mensagem.istitle()}')
