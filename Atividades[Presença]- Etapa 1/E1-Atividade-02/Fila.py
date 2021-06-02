fila = []
print(f'\nA lotérica está fechada com {len(fila)} pessoas na fila.\n')

for x in range (1, 7):
    print(f'Apareceu a {x}a pessoa na fila da Lotérica.')
    fila.append(x)
    
print(f'\nPossuímos {len(fila)} pessoas na fila da lotérica.')
print(f'{fila}\n')

print(f'A lotérica abriu, pessoas estao pagando as contas.\n')
for x in range (1, 5):
    print(f'A {x}a pessoa pagou sua conta.')
    fila.pop(0)

print(f'\nAgora possuímos {len(fila)} pessoas na fila da lotérica.')
print(f'{fila}\n')

for x in range (5, 7):
    y = x - 4
    print(f'A {x}a pessoa passou para frente e esta em {y}o na fila')
    fila.append(y)
    
for x in range (1, 3):
    fila.pop(0)

print(f'\nFila atual da lotérica:')
print(f'{fila}')