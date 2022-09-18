m = float(input('Digite o valor em metros: '))

km = m*0.001
hm = m*0.01
dam = m*0.1
dm = m*10
cm = m*100
mm = m*1000

print(f'\nA medida de {m:.2f}m corresponde a:')
print(f'{km:.3f}km')
print(f'{hm:.3f}hm')
print(f'{dam:.3f}dam')
print(f'{dm:.2f}dm')
print(f'{cm:.2f}cm')
print(f'{mm:.2f}mm')
