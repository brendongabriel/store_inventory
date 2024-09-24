# Classe Estoque:
# A classe gerencia o inventário de um item na loja, verificando níveis de estoque e controlando o reabastecimento.

# Atributos:
# nome (str): Nome do item.
# quantidade (int): Quantidade atual no estoque.
# limite_reabastecimento (int): Quantidade mínima antes de reabastecer.
# reabastecendo (bool): Indica se o item está sendo reabastecido.

# Métodos:
# init(nome, quantidade, limite_reabastecimento): Inicializa o item no estoque.
# verificar_estoque(): Verifica o estoque e inicia o reabastecimento se necessário.
# iniciar_reabastecimento(): Marca o item como em reabastecimento.
# concluir_reabastecimento(quantidade_reabastecida): Atualiza o estoque com a nova quantidade.

import random
import time

class Estoque:
    def __init__(self, nome, quantidade, limite_reabastecimento):
        self.nome = nome
        self.quantidade = quantidade
        self.limite_reabastecimento = limite_reabastecimento
        self.reabastecendo = False

    def verificar_estoque(self):
        if self.quantidade <= 0:
            print(f"Item {self.nome} fora de estoque, venda bloqueada.")
            self.iniciar_reabastecimento()
        elif self.quantidade < self.limite_reabastecimento and not self.reabastecendo:
            print(f"Estoque de {self.nome} está baixo, iniciando reabastecimento...")
            self.iniciar_reabastecimento()
        else:
            print(f"Estoque de {self.nome} disponível para venda.")

    def iniciar_reabastecimento(self):
        self.reabastecendo = True
        # Simula tempo de reposição
        print(f"Reabastecendo {self.nome}...")

    def concluir_reabastecimento(self, quantidade_reabastecida):
        self.quantidade += quantidade_reabastecida
        self.reabastecendo = False
        print(f"Reabastecimento de {self.nome} concluído. Novo estoque: {self.quantidade} unidades.")

# Classe ItemAgente
# A classe controla a interação entre o sistema de estoque e os pedidos, gerenciando a disponibilidade de itens e o reabastecimento automático.

# Atributos:
# estoque (Estoque): Instância da classe Estoque responsável pelo controle de inventário.

# Métodos:
# init(nome, quantidade, limite_reabastecimento): Inicializa um item com seu respectivo estoque.
# processar_pedido(quantidade_pedido): Processa um pedido de itens, verificando o estoque. Se o estoque for insuficiente, aciona o reabastecimento e aguarda sua conclusão.
# interagir(): Verifica o estado do estoque e, se estiver em reabastecimento, conclui-o automaticamente após uma espera.

class ItemAgente:
    def __init__(self, nome, quantidade, limite_reabastecimento):
        self.estoque = Estoque(nome, quantidade, limite_reabastecimento)

    def processar_pedido(self, quantidade_pedido):
        if self.estoque.quantidade >= quantidade_pedido:
            self.estoque.quantidade -= quantidade_pedido
            print(f"Pedido de {quantidade_pedido} unidades de {self.estoque.nome} processado.")
        else:
            print(f"Não há estoque suficiente de {self.estoque.nome} para o pedido. Esse pedido ira levar um tempo.")
            self.estoque.verificar_estoque()
            if self.estoque.reabastecendo:
                print("Aguardando o reabastecimento ser concluído...")
                time.sleep(5)
                self.estoque.concluir_reabastecimento(quantidade_pedido)
                self.processar_pedido(quantidade_pedido)

    def interagir(self):
        self.estoque.verificar_estoque()
        if self.estoque.reabastecendo:
            time.sleep(1)
            self.estoque.concluir_reabastecimento(15 - self.estoque.quantidade)

# Classe ClienteAgente
# A classe representa um cliente que faz pedidos de itens no sistema.

# Atributos:
# nome (str): Nome do cliente.

# Métodos:
# init(nome): Inicializa o cliente com seu nome.
# fazer_pedido(item, quantidade): O cliente faz um pedido de uma quantidade específica de um item, iniciando o processo de verificação e processamento do pedido.

class ClienteAgente:
    def __init__(self, nome):
        self.nome = nome

    def fazer_pedido(self, item, quantidade):
        print(f"{self.nome} está fazendo um pedido de {quantidade} unidades de {item.estoque.nome}.")
        item.processar_pedido(quantidade)

# Cenário da Loja
# Cria um cenário inicial para a loja, onde diferentes produtos são armazenados e gerenciados com base em seu estoque.

# Estrutura: produtos: Dicionário que armazena os itens da loja, onde as chaves são os nomes dos produtos e os valores são instâncias da classe ItemAgente.

# Produtos Iniciais:
# Cada produto recebe um nome, uma quantidade aleatória de estoque (entre 0 e 15 unidades), e um limite de reabastecimento definido como 5 unidades. Os produtos incluídos são:
# Teclado, Mouse, Monitor, HD Externo, Processador, Placa Mãe, Memória RAM, SSD 500GB
# Uso de random.randint(0, 15):
# A função random.randint(0, 15) garante que o estoque inicial de cada item seja atribuído de forma aleatória, simulando uma variação realista de quantidades disponíveis no início.

produtos = {
  "Teclado": ItemAgente("Teclado", random.randint(0, 15), 5),
  "Mouse": ItemAgente("Mouse", random.randint(0, 15), 5),
  "Monitor": ItemAgente("Monitor", random.randint(0, 15), 5),
  "HD Externo": ItemAgente("HD Externo", random.randint(0, 15), 5),
  "Processador": ItemAgente("Processador", random.randint(0, 15), 5),
  "Placa Mãe": ItemAgente("Placa Mãe", random.randint(0, 15), 5),
  "Memória RAM": ItemAgente("Memória RAM", random.randint(0, 15), 5),
  "SSD 500GB": ItemAgente("SSD 500GB", random.randint(0, 15), 5)
}

# Verificando o estoque antes de abrir a loja
for produto in produtos.values():
    produto.interagir()

# Sistema de interação com o Usuário
print("\n--- Estoque Inicial ---")

while True:
        print("\n--- Simulação da Loja de Informática ---\n")
        nome_cliente = input("Digite o nome do cliente (ou 'sair' para encerrar): ")
        if nome_cliente.lower() == 'sair':
            break
        cliente = ClienteAgente(nome_cliente)

        while True:
            print("\nProdutos disponíveis:")
            for produto in produtos:
                print(produto)
            produto_escolhido = input("Escolha um produto para fazer o pedido (ou 'voltar' para o menu anterior): ")
            if produto_escolhido.lower() == 'voltar':
                break
            elif produto_escolhido not in produtos:
                print("Produto inválido. Tente novamente.")
                continue

            quantidade = int(input(f"Digite a quantidade de {produto_escolhido} que deseja pedir: "))
            cliente.fazer_pedido(produtos[produto_escolhido], quantidade)

            # Verificar estoque e reabastecer se necessário
            produtos[produto_escolhido].interagir()

        print("\n--- Fim da Interação ---\n")

# Quando fechar a loja, verificar o estoque
for produto in produtos.values():
    produto.interagir()
