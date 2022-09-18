nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1+nota2)/2

print(f'\nA média entre {nota1} e {nota2} é {media:.1f}')

if media >= 6.0:
    print('Aprovado!')
elif media >= 5.0:
    print('Recuperação!')
else:
    print('Reprovado!')
