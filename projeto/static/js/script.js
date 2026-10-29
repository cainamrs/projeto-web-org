const CHAVE_CARRINHO = 'carrinho';

function lerCarrinho() {
    return JSON.parse(localStorage.getItem(CHAVE_CARRINHO)) || [];
}

function salvarCarrinho(itens) {
    localStorage.setItem(CHAVE_CARRINHO, JSON.stringify(itens));
}

function formatarPreco(valor) {
    return 'R$ ' + valor.toFixed(2).replace('.', ',');
}

function atualizarContador() {
    const contador = document.getElementById('contador-carrinho');
    if (!contador) return;
    const total = lerCarrinho().reduce((soma, item) => soma + item.quantidade, 0);
    contador.textContent = total;
}

function renderizarCarrinho() {
    const lista = document.getElementById('lista-carrinho');
    if (!lista) return;

    const itens = lerCarrinho();
    const vazio = document.getElementById('carrinho-vazio');
    const totalEl = document.getElementById('total-carrinho');

    lista.innerHTML = '';
    let total = 0;

    itens.forEach((item, indice) => {
        total += item.preco * item.quantidade;

        const li = document.createElement('li');
        li.textContent = `${item.nome} (${item.tamanho}) x${item.quantidade}`;

        const botao = document.createElement('button');
        botao.textContent = 'Remover';
        botao.addEventListener('click', () => {
            const atual = lerCarrinho();
            atual.splice(indice, 1);
            salvarCarrinho(atual);
            renderizarCarrinho();
            atualizarContador();
        });

        li.appendChild(botao);
        lista.appendChild(li);
    });

    if (vazio) vazio.style.display = itens.length ? 'none' : 'block';
    if (totalEl) totalEl.textContent = formatarPreco(total);
}

document.addEventListener('DOMContentLoaded', () => {
    atualizarContador();

    const botaoAdicionar = document.getElementById('btn-adicionar');
    if (botaoAdicionar) {
        botaoAdicionar.addEventListener('click', () => {
            const tamanho = document.getElementById('tamanho').value;
            const id = Number(botaoAdicionar.dataset.id);
            const nome = botaoAdicionar.dataset.nome;
            const preco = Number(botaoAdicionar.dataset.preco);

            const itens = lerCarrinho();
            const existente = itens.find(i => i.id === id && i.tamanho === tamanho);

            if (existente) {
                existente.quantidade += 1;
            } else {
                itens.push({ id, nome, preco, tamanho, quantidade: 1 });
            }

            salvarCarrinho(itens);
            atualizarContador();

            const mensagem = document.getElementById('mensagem-carrinho');
            if (mensagem) mensagem.textContent = 'Produto adicionado à sacola!';
        });
    }

    renderizarCarrinho();

    const botaoLimpar = document.getElementById('btn-limpar');
    if (botaoLimpar) {
        botaoLimpar.addEventListener('click', () => {
            salvarCarrinho([]);
            renderizarCarrinho();
            atualizarContador();
        });
    }

    const formCadastro = document.getElementById('form-cadastro');
    if (formCadastro) {
        formCadastro.addEventListener('submit', (evento) => {
            evento.preventDefault();
            const nome = formCadastro.nome.value.trim();
            const ano = formCadastro.ano.value.trim();
            if (!nome || !ano) return;
            window.location.href = `/cadastro/${encodeURIComponent(nome)}/${ano}`;
        });
    }
});
