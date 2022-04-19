class Cliente(object):
    def __init__(self,nome,cpf=0):
        self.nome = nome
        self.cpf = cpf

    def set_nome(self,nomeNovo):
        self.nome = nomeNovo

    def get_nome(self):
     return self.nome

    def set_cpf(self,cpfNovo):
        self.cpf = cpfNovo

    def get_cpf(self):
        return self.cpf

    def __str__(self):
        dados = f'Cpf: {self.cpf}, Nome: {self.nome}'
        return dados

# ====================================================================================================================

class Produto(object):
    def __init__(self, identificador, nomeProduto, preco):
        self.identificador = identificador
        self.nomeProduto = nomeProduto
        self.preco = preco

    def __str__(self):
        dados = f'Numero do Produto: {self.identificador}, Produtos: {self.nomeProduto}, preco: {self.preco}'
        return dados



    def mostrar_produtos_quantidade(self):
        print('funfou')

    def mostrar_produtos_preco(self):
        total = self.preco
        return total
# ====================================================================================================================

class Carrinho(object):
    def __init__(self, numeroPedido, objeto_cliente):
        self.numeroPedido = numeroPedido
        self.cliente = objeto_cliente
        self.produtos = list()

    def mostra_produto(self):
        print('---------')
        if(len(self.produtos) <= 0):
            print('Carrinho Vazio')
        else:
            for produtos in self.produtos:
                print(produtos)
            print('Quantidade de itens total:', len(self.produtos))
        print('---------')

    def mostra_valor_produtos(self):
        print('---------')
        total = 0
        for produtos in self.produtos:
            total += Produto.mostrar_produtos_preco(produtos)
        print('valor total:', total)
        print('---------')

    def insere_produto(self,produto):
        self.produtos.append(produto)

    def __str__(self):
        dados = f'Numero do Pedido: {self.numeroPedido}, Produtos: '
        return dados

if __name__ == '__main__':
    teste1 = Cliente('jorge', 51)
    print(teste1.get_cpf())
    print(teste1.__str__())
    arroz = Produto(45455,'Arroz',10)
    feijao = Produto(3333,'Feijão',15)
    carrinho1 = Carrinho(12,teste1)

    carrinho1.mostra_produto()

    print(carrinho1.cliente.get_nome())
    print(carrinho1.cliente.__str__())
    carrinho1.insere_produto(arroz)
    carrinho1.insere_produto(feijao)


    print('===================')
    carrinho1.mostra_produto()
    carrinho1.mostra_valor_produtos()
