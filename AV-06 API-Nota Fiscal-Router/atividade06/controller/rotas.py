from flask import request

from atividade06 import app
from atividade06.controller import objeto_json, response, select_objeto
from atividade06.model import bd_cl, its, bd_notaf, bd_pdt
from atividade06.model.cliente import Cliente
from atividade06.model.itemnotafiscal import ItemNotaFiscal
from atividade06.model.notafiscal import NotaFiscal
from atividade06.model.produto import Produto

# Rotas Cliente

@app.route('/clientes', methods=["GET"])
def ler_clientes():
    cls_json = objeto_json(bd_cl)

    return response(200, 'clientes', cls_json, 'Todos os clientes')


@app.route('/cliente/<int:id_cl>', methods=["GET"])
def ler_cliente(id_cl):
    try:
        cliente = select_objeto(bd_cl, id_cl)
        cl_json = objeto_json(cliente)

        return response(200, 'cliente', cl_json, 'Cliente foi selecionado')
    except Exception as e:
        print(e)
        return response(400, 'cliente', {}, 'ERRO: ID inválido')


@app.route('/cliente', methods=["POST"])
def criar_cliente():
    try:
        body = request.json

        cl = Cliente(bd_cl[-1].get_id() + 1, body['nome'], body['codigo'], body['cpf'], 'pessoa fisica')
        bd_cl.append(cl)
        cl_json = objeto_json(cl)

        return response(201, 'cliente', cl_json, 'Cliente foi criado')
    except Exception as e:
        print(e)
        return response(400, 'cliente', {}, 'Cliente não foi criado')


@app.route('/cliente/<int:id_cl>', methods=["PUT"])
def atualizar_cliente(id_cl):
    try:
        body = request.json
        cliente = select_objeto(bd_cl, id_cl)

        cliente.set_nome(body['nome'])
        cliente.set_codigo(body['codigo'])
        cliente.set_cnpjcpf(body['cpf'])

        cliente_json = objeto_json(cliente)
        return response(200, 'cliente', cliente_json, 'Cliente foi atualizado')
    except Exception as e:
        print(e)
        return response(400, 'cliente', {}, 'Cliente não foi atualizado')


@app.route('/cliente/<int:id_cliente>', methods=["DELETE"])
def deletar_cliente(id_cliente):
    try:
        cliente = select_objeto(bd_cl, id_cliente)
        bd_cl.remove(cliente)

        cliente_json = objeto_json(cliente)
        return response(200, 'cliente', cliente_json, 'Cliente foi deletado')
    except Exception as e:
        print(e)
        return response(400, 'cliente', {}, 'Cliente não foi deletado')

# Rotas Produtos

@app.route('/produtos', methods=["GET"])
def ler_produtos():
    protudos_json = objeto_json(bd_pdt)

    return response(200, 'produtos', protudos_json, 'Todos os produtos')


@app.route('/produto/<int:id_pdt>', methods=["GET"])
def ler_produto(id_pdt):
    try:
        produto = select_objeto(bd_pdt, id_pdt)
        produto_json = objeto_json(produto)

        return response(200, 'produto', produto_json, 'Produto foi selecionado')
    except Exception as e:
        print(e)
        return response(400, 'produto', {}, 'ERRO: ID inválido')


@app.route('/produto', methods=["POST"])
def criar_produto():
    try:
        body = request.json

        produto = Produto(bd_pdt[-1].get_id() + 1, body['codigo'], body['descricao'], body['valor-unitario'])
        bd_pdt.append(produto)
        produto_json = objeto_json(produto)

        return response(201, 'produto', produto_json, 'Produto foi criado')
    except Exception as e:
        print(e)
        return response(400, 'produto', {}, 'Produto não foi criado')


@app.route('/produto/<int:id_pdt>', methods=["PUT"])
def atualizar_produto(id_pdt):
    try:
        body = request.json
        produto = select_objeto(bd_pdt, id_pdt)

        produto.set_codigo(body['codigo'])
        produto.set_descricao(body['descricao'])
        produto.set_valor_unitario(body['valor-unitario'])

        produto_json = objeto_json(produto)
        return response(200, 'produto', produto_json, 'Produto foi atualizado')
    except Exception as e:
        print(e)
        return response(400, 'produto', {}, 'Produto não foi atualizado')


@app.route('/produto/<int:id_pdt>', methods=["DELETE"])
def deletar_produto(id_pdt):
    try:
        produto = select_objeto(bd_pdt, id_pdt)
        bd_pdt.remove(produto)

        produto_json = objeto_json(produto)
        return response(200, 'produto', produto_json, 'Produto foi apagado')
    except Exception as e:
        print(e)
        return response(400, 'produto', {}, 'Produto não foi apagado')

# Rotas Notas

@app.route('/notasfiscais', methods=["GET"])
def ler_notas():
    notas_json = objeto_json(bd_notaf)

    return response(200, 'notas', notas_json, 'Todos as notas')


@app.route('/notafiscal/<int:id_nota>', methods=["GET"])
def ler_nota(id_nota):
    try:
        notaf = select_objeto(bd_notaf, id_nota)
        nota_json = objeto_json(notaf)

        return response(200, 'nota', nota_json, 'Nota foi selecionada')
    except Exception as e:
        print(e)
        return response(400, 'nota', {}, 'ERRO: ID inválido')


@app.route('/notafiscal', methods=["POST"])
def criar_nota():
    try:
        body = request.json

        cliente = select_objeto(bd_cl, body['cliente'])
        nota = NotaFiscal(bd_notaf[-1].get_id() + 1, body['codigo'], cliente)
        bd_notaf.append(nota)

        nota_json = objeto_json(nota)
        return response(201, 'nota', nota_json, 'Nota foi criada')
    except Exception as e:
        print(e)
        return response(400, 'nota', {}, 'Nota não foi criada')


@app.route('/notafiscal/<int:id_nota>', methods=["PUT"])
def atualizar_nota(id_nota):
    try:
        body = request.json
        nota = select_objeto(bd_notaf, id_nota)
        cliente = select_objeto(bd_cl, body['cliente'])
        nota.set_codigo(body['codigo'])
        nota.setCliente(cliente)

        nota_json = objeto_json(nota)
        return response(200, 'nota', nota_json, 'Nota foi atualizada')
    except Exception as e:
        print(e)
        return response(400, 'nota', {}, 'Nota não foi atualizada')


@app.route('/notafiscal/<int:id_nota>', methods=["DELETE"])
def deletar_nota(id_nota):
    try:
        nota = select_objeto(bd_notaf, id_nota)
        bd_notaf.remove(nota)

        nota_json = objeto_json(nota)
        return response(200, 'nota', nota_json, 'Nota apagada')
    except Exception as e:
        print(e)
        return response(400, 'nota', {}, 'Nota não apagada')


@app.route('/calculanf/<int:id_nota>', methods=["GET"])
def calcular_nota(id_nota):
    try:
        nota = select_objeto(bd_notaf, id_nota)
        nota.calcularNotaFiscal()

        nota_json = objeto_json(nota)
        return response(200, 'nota', nota_json, 'Nota calculou')

    except Exception as e:
        print(e)
        return response(400, 'nota', {}, 'Nota não calculou')


@app.route('/imprimenf/<int:id_nota>', methods=["GET"])
def imprimir_nota(id_nota):
    try:
        nota = select_objeto(bd_notaf, id_nota)
        impresso = nota.imprimirNotaFiscal()

        return response(200, 'nota', impresso, 'Nota imprimiu')

    except Exception as e:
        print(e)
        return response(400, 'nota', {}, 'Nota não imprimiu')

# Rotas Itens

@app.route('/itensnf/<int:id_nota>', methods=["GET"])
def ler_itens(id_nota):
    try:
        itens_nota = select_objeto(bd_notaf, id_nota).get_itens()
        itens_json = objeto_json(itens_nota)

        return response(200, 'itens', itens_json, 'Todos os itens da nota')
    except Exception as e:
        print(e)
        return response(400, 'itens', {}, 'ID inválido')


@app.route('/itemnf/<int:id_item>', methods=["GET"])
def ler_item(id_item):
    try:
        item = select_objeto(its, id_item)
        item_json = objeto_json(item)

        return response(200, 'itens', item_json, 'Itens da nota')
    except Exception as e:
        print(e)
        return response(400, 'itens', {}, 'ID inválido')


@app.route('/itemnf', methods=["POST"])
def criar_item():
    try:
        body = request.json
        produto = select_objeto(bd_pdt, body['produto'])
        item = ItemNotaFiscal(its[-1].get_id() + 1, body['sequencial'], body['quantidade'], produto)
        its.append(item)
        item_json = objeto_json(item)

        return response(201, 'item', item_json, 'Item criado')
    except Exception as e:
        print(e)
        return response(400, 'item', {}, 'Item não criado')


@app.route('/itemnf/<int:id_item>', methods=["PUT"])
def atualizar_item(id_item):
    try:
        body = request.json
        item = select_objeto(its, id_item)

        item.set_sequencial(body['sequencial'])
        item.set_quantidade(body['quantidade'])

        item_json = objeto_json(item)
        return response(200, 'item', item_json, 'Item atualizado')
    except Exception as e:
        print(e)
        return response(400, 'item', {}, 'Item não atualizado')


@app.route('/itemnf/<int:id_item>', methods=["DELETE"])
def deletar_item(id_item):
    try:
        item = select_objeto(its, id_item)
        its.remove(item)

        item_json = objeto_json(item)
        return response(200, 'item', item_json, 'Item deletado')
    except Exception as e:
        print(e)
        return response(400, 'item', {}, 'Item não deletado')