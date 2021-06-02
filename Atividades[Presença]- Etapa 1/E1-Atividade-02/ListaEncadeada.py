import random

lista = ['rap', 'reggae', 'samba', 'blues']

lista.insert(0, 'pop')
lista.insert(1, 'rock')
lista.insert(0, 'metal')
listaEnc = sorted(lista)

print(f'\nPossuo {len(listaEnc)} gêneros musicais na minha playlist.')
print(f'{listaEnc}\n')

aula = list(range(1, 4))
random.shuffle(aula)
for x in aula:
    print(f'O gênero {listaEnc[x]} foi retirado.')
    listaEnc.pop(x)

print(f'\nEntão sobraram {len(listaEnc)} gêneros na playlist.')
print(f'{listaEnc}')