from datetime import datetime

from flask import Flask, render_template, abort

app = Flask(__name__)

PRODUTOS = [
    {'id': 1, 'nome': 'Camiseta Básica Preta', 'categoria': 'Camisetas', 'preco': 79.90,
     'descricao': 'Camiseta de algodão 100%, com corte reto e caimento confortável. '
                  'Peça coringa que combina com quase tudo, do café da manhã à noite na cidade.',
     'cuidados': 'Lavar do avesso, em água fria. Não usar alvejante. Secar à sombra.',
     'tamanhos': ['P', 'M', 'G', 'GG'], 'imagem': 'camiseta-preta.svg'},
    {'id': 2, 'nome': 'Jaqueta Jeans Azul', 'categoria': 'Jaquetas', 'preco': 219.90,
     'descricao': 'Jaqueta jeans com lavagem clara, bolsos frontais e botões de metal. '
                  'Ganha personalidade sobre uma camiseta lisa ou um vestido.',
     'cuidados': 'Lavar em água fria com cores parecidas. Passar do avesso.',
     'tamanhos': ['P', 'M', 'G'], 'imagem': 'jaqueta-jeans.svg'},
    {'id': 3, 'nome': 'Calça Chino Bege', 'categoria': 'Calças', 'preco': 159.90,
     'descricao': 'Calça chino em sarja leve, com cintura alta e caimento reto. '
                  'Funciona no escritório e também em passeios de fim de semana.',
     'cuidados': 'Lavar em máquina no ciclo delicado. Passar em temperatura média.',
     'tamanhos': ['38', '40', '42', '44'], 'imagem': 'calca-chino.svg'},
    {'id': 4, 'nome': 'Moletom Oversized Cinza', 'categoria': 'Moletons', 'preco': 189.90,
     'descricao': 'Moletom de modelagem ampla, com capuz forrado e bolso canguru. '
                  'Pensado para o frio e para aquele dia de descanso.',
     'cuidados': 'Lavar do avesso. Não secar na máquina em temperatura alta.',
     'tamanhos': ['P', 'M', 'G', 'GG'], 'imagem': 'moletom-cinza.svg'},
    {'id': 5, 'nome': 'Vestido Midi Floral', 'categoria': 'Vestidos', 'preco': 249.90,
     'descricao': 'Vestido midi com estampa floral em tecido leve e alças ajustáveis. '
                  'Fluido no movimento, ideal para dias quentes e encontros especiais.',
     'cuidados': 'Lavar à mão ou no ciclo delicado. Secar à sombra.',
     'tamanhos': ['P', 'M', 'G'], 'imagem': 'vestido-floral.svg'},
    {'id': 6, 'nome': 'Tênis Branco Casual', 'categoria': 'Calçados', 'preco': 299.90,
     'descricao': 'Tênis de couro sintético com solado de borracha e design minimalista. '
                  'Confortável para longas caminhadas e combina com qualquer look.',
     'cuidados': 'Limpar com pano úmido e sabão neutro. Secar naturalmente.',
     'tamanhos': ['37', '38', '39', '40', '41', '42'], 'imagem': 'tenis-branco.svg'},
]


def buscar_produto(produto_id):
    for produto in PRODUTOS:
        if produto['id'] == produto_id:
            return produto
    return None


@app.route('/')
def inicio():
    return render_template('index.html', produtos=PRODUTOS)


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


@app.route('/produto/<int:produto_id>')
def produto(produto_id):
    item = buscar_produto(produto_id)
    if item is None:
        abort(404)
    return render_template('produto.html', produto=item)


@app.route('/carrinho')
def carrinho():
    return render_template('carrinho.html')


@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', erro=None)


@app.route('/cadastro/<nome>/<int:ano>')
def cadastro_resultado(nome, ano):
    ano_atual = datetime.now().year

    if ano > ano_atual:
        return render_template(
            'cadastro.html',
            erro='O ano de nascimento não pode ser maior que o ano atual.'
        ), 400

    idade = ano_atual - ano
    maior_de_idade = idade >= 18

    return render_template(
        'resultado.html',
        nome=nome,
        ano_nascimento=ano,
        idade=idade,
        maior_de_idade=maior_de_idade,
    )


@app.errorhandler(404)
def pagina_nao_encontrada(erro):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
