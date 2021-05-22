from tipoMovimento import TipoMovimento
from colaborador import Colaborador
from movimentoFolha import MovimentoFolha


class FolhaPagamento:
    def __init__(self, mes, totaldescontos, totalproventos, ano):
        self.mes = mes
        self.totalDescontos = totaldescontos
        self.totalProventos = totalproventos
        self.ano = ano
        self.movimentos = []
        self.colaboradores = []

    def InserirColaboradores(self, colaborador: Colaborador):
        self.colaboradores.append(colaborador)

    # Quarta Questão
    def InserirMovimentos(self, movimento):
        if type(movimento) == MovimentoFolha:
            self.movimentos.append(movimento)

    # Oitava Questão
    def calcularFolha(self):
        for movimento in self.movimentos:
            if movimento.tipoMovimento == TipoMovimento.P:
                self.totalProventos += movimento.valor
            elif movimento.tipoMovimento == TipoMovimento.D:
                self.totalDescontos += movimento.valor

        totalSalarios = 0
        for colaborador in self.colaboradores:
            totalSalarios += colaborador.salarioAtual

        totalPagamento = (totalSalarios + self.totalProventos) - self.totalDescontos
        print('\nTotal de Salários = {} '
              '\nTotal de Proventos = {}'
              '\nTotal de Descontos = {} '
              '\nTotal a Pagar = {}'.format(totalSalarios, self.totalProventos, self.totalDescontos, totalPagamento))