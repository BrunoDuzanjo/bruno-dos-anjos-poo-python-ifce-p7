pilha = []
print(f'\nPossuímos um total de {len(pilha)} livros na pilha.\n')

for x in range(1, 16):
    print(f'Livro de número {x} é colocado na pilha')
    pilha.insert(0, x)

print(f'\nNo momento possuímos {len(pilha)} livros na pilha.')
print(f'{pilha}\n')

for x in range(15, 8, -1):
    print(f'Livro de número {x} foi lido')
    pilha.pop(0)

print(f'\nAgora temos {len(pilha)} livros na pilha.')
print(f'{pilha}\n')
print(f'Não deixe eles só empilhados, depois leia-os!\n')