from tipoMovimento import TipoMovimento
from movimentoFolha import MovimentoFolha


class Colaborador:
    def __init__(self, codigo, nome, endereco, telefone, bairro, cep, cpf, salarioatual):
        self.codigo = codigo
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.bairro = bairro
        self.cep = cep
        self.cpf = cpf
        self.salarioAtual = salarioatual
        self.movimentos = []

    # Quinta Questão
    def InserirMovimentosColaborador(self, movimento):
        if type(movimento) == MovimentoFolha:
            self.movimentos.append(movimento)

    # Nona Questão
    def calcularSalario(self):
        totalProventos = 0.0
        totalDescontos = 0.0

        for movimento in self.movimentos:
            if movimento.tipoMovimento == TipoMovimento.P:
                totalProventos += movimento.valor
            elif movimento.tipoMovimento == TipoMovimento.D:
                totalDescontos += movimento.valor

        valorLiquido = (self.salarioAtual + totalProventos) - totalDescontos

        print('\nCodigo: {} '
              '\nNome: {}'
              '\nSalário: {} '
              '\nTotal Proventos: {} '
              '\nTotal Descontos: {} '
              '\nValor Liquido a Receber: {}'.format(self.codigo,
                                                     self.nome,
                                                     self.salarioAtual,
                                                     totalProventos,
                                                     totalDescontos,
                                                     valorLiquido))