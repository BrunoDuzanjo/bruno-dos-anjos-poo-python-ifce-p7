from folhaPagamento import FolhaPagamento
from movimentoFolha import MovimentoFolha
from colaborador import Colaborador
from tipoMovimento import TipoMovimento


# Primeira Questão
FP = FolhaPagamento(9, 0, 0, 2019)

# Segunda Questão
CL01 = Colaborador(100, "Manoel Claudino", "Av 13 de Maio 2081", "88671020", "Benfica", "60020-060", "124543556-89",4500.00)
CL02 = Colaborador(200, "Carmelina da Silva", "Avenida dos Expedicionários 1200", "3035-1280", "Aeroporto", "60530-020","301789435-54", 2500.00)
CL03 = Colaborador(300, "Gurmelina Castro Saraiva", "Av João Pessoa 1020", "3235-1089", "Damas", "60330-090", "350245632-76", 3000.00)

# Terceira Questão
MF01 = MovimentoFolha(CL01, "Gratificacao", 4500.00, TipoMovimento.P)
MF02 = MovimentoFolha(CL01, "Plano Saúde", 1000.00, TipoMovimento.P)
MF03 = MovimentoFolha(CL01, "Pensão", 600.00, TipoMovimento.D)
MF04 = MovimentoFolha(CL02, "Gratificacao", 2500.00, TipoMovimento.P)
MF05 = MovimentoFolha(CL02, "Plano Saúde", 1000.00, TipoMovimento.P)
MF06 = MovimentoFolha(CL02, "Faltas", 600.00, TipoMovimento.D)
MF07 = MovimentoFolha(CL03, "Gratificacao", 4500.00, TipoMovimento.P)
MF08 = MovimentoFolha(CL03, "Plano Saúde", 1000.00, TipoMovimento.P)
MF09 = MovimentoFolha(CL03, "Pensão", 600.00, TipoMovimento.D)

# Sexta Questão
FP.InserirMovimentos(MF01)
FP.InserirMovimentos(MF02)
FP.InserirMovimentos(MF03)
FP.InserirMovimentos(MF04)
FP.InserirMovimentos(MF05)
FP.InserirMovimentos(MF06)
FP.InserirMovimentos(MF07)
FP.InserirMovimentos(MF08)
FP.InserirMovimentos(MF09)

# Sétima Questão
CL01.InserirMovimentosColaborador(MF01)
CL01.InserirMovimentosColaborador(MF02)
CL01.InserirMovimentosColaborador(MF03)
CL02.InserirMovimentosColaborador(MF04)
CL02.InserirMovimentosColaborador(MF05)
CL02.InserirMovimentosColaborador(MF06)
CL03.InserirMovimentosColaborador(MF07)
CL03.InserirMovimentosColaborador(MF08)
CL03.InserirMovimentosColaborador(MF09)

FP.InserirColaboradores(CL01)
FP.InserirColaboradores(CL02)
FP.InserirColaboradores(CL03)

FP.calcularFolha()
CL01.calcularSalario()
CL02.calcularSalario()
CL03.calcularSalario()