from atividade06.model.cliente import Cliente
from atividade06.model.produto import Produto
from atividade06.model.notafiscal import NotaFiscal
from atividade06.model.itemnotafiscal import ItemNotaFiscal

# Banco de Dados Clientes
cl1 = Cliente(1, "Bruno Silveira", 100, '678.427.155-64', 'pessoa fisica')
cl2 = Cliente(2, "Israel Leite", 200, '084.878.884-29', 'pessoa fisica')
cl3 = Cliente(3, "Beatriz Vidal", 300, '037.557.794-71', 'pessoa fisica')

bd_cl = [cl1, cl2, cl3]

# Banco de Dados Produtos
pdt1 = Produto(1, 100, 'Macarrão Espaguete c/ Ovos Divina Mesa 500g', 3.2)
pdt2 = Produto(2, 200, 'Cuscuz Farinha De Milho Flocão Maratá 500G', 8.9)
pdt3 = Produto(3, 300, 'Biscoito Bauducco Maizena 170g', 2.3)

bd_pdt = [pdt1, pdt2, pdt3]

# Banco de Dados Notas Fiscais
notaf1 = NotaFiscal(1, 100, cl1)
notaf2 = NotaFiscal(2, 200, cl2)
notaf3 = NotaFiscal(3, 300, cl3)

bd_notaf = [notaf1, notaf2, notaf3]

# Banco de Dados Itens Nota Fiscal
it1 = ItemNotaFiscal(1, 1, 6, pdt1)
it2 = ItemNotaFiscal(2, 1, 8, pdt2)

it3 = ItemNotaFiscal(2, 1, 8, pdt2)
it4 = ItemNotaFiscal(3, 2, 5, pdt3)

it5 = ItemNotaFiscal(4, 1, 10, pdt1)
it6 = ItemNotaFiscal(5, 2, 4, pdt3)

its = [it1, it2, it3, it4, it5, it6]

# Adicionando os Produtos as Notas
notaf1.adicionarItem(it1)

notaf2.adicionarItem(it3)
notaf2.adicionarItem(it4)

notaf3.adicionarItem(it5)
notaf3.adicionarItem(it6)