from TrianguloLados import *

def desvendarLados():
    if ladoX == ladoY and ladoX == ladoZ:
        print('É um Triângulo Equilátero, pois tem todos os lados iguais.')
    elif ladoX == ladoY or ladoX == ladoZ or ladoY == ladoZ:
        print('É um Triângulo Isósceles, pois tem dois lados iguais')
    else:
        print('É um Triângulo Escaleno, pois todos seus lados são diferentes')

desvendarLados()