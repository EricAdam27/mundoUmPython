numeroDigitado = int(input('Digite um número para ver sua tabuada: '))

contador = 1

while contador < 11:
    print(f'{numeroDigitado} x {contador:2} = {numeroDigitado*contador}')
    contador = contador+1
