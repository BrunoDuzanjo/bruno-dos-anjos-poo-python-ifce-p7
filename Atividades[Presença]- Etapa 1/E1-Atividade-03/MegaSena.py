import random

def repetido():
    if len(sorteadoLista) != len(set(sorteadoLista)):
        sorteadoLista2 = set(sorteadoLista)

sorteadoLista = []
sorteadoLista2 = []

while len(sorteadoLista2) < 6:
    sorteado = random.randrange(1,61)
    sorteadoLista.append(sorteado)
    repetido()
    sorteadoLista2 = set(sorteadoLista)

print(sorted(sorteadoLista2))