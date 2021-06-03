class Triangulos:
    def __init__(self, ladoX, ladoY, ladoZ):
        self.ladoX = ladoX
        self.ladoY = ladoY
        self.ladoZ = ladoZ

    def comporTriangulo(self):
        if self.ladoX <= 0 or self.ladoY <= 0 or self.ladoZ <= 0:
            return False

        soma1 = self.ladoX + self.ladoY
        soma2 = self.ladoX + self.ladoZ
        soma3 = self.ladoY + self.ladoZ

        if self.ladoX >= soma3 or self.ladoY >= soma2 or self.ladoZ >= soma1:
            return f'Não se é capaz formar um triângulo com os lados concedidos.'
        else:
            return f'Um triângulo pode ser formado com os lados concedidos'


triangulo1 = Triangulos(int(input('Escreva em centímetros o 1º lado do Triangulo: ')), int(input('Digite em centímetros o 2º lado do Triangulo: ')), int(input('Digite em centímetros o 3º lado do Triangulo: ')))
print(triangulo1.comporTriangulo())