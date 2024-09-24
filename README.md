# Relatório do Código de Simulação da Loja de Informática

## 1. Objetivo do Código
O código simula o funcionamento de uma loja de informática, gerenciando o estoque de produtos e permitindo que clientes façam pedidos. Ele inclui um sistema automático de reabastecimento quando o estoque está baixo ou zerado.

## 2. Estrutura Geral
O código é composto por três classes principais e uma interface de interação com o usuário:

1. **Classe `Estoque`**: Gerencia o inventário de um item específico.
2. **Classe `ItemAgente`**: Interage com o estoque, processa pedidos e gerencia a reposição dos itens.
3. **Classe `ClienteAgente`**: Representa um cliente que faz pedidos de produtos.
4. **Interface de Interação**: Um loop que simula a interação com clientes, permitindo pedidos e verificando o estoque em tempo real.

## 3. Regras Implementadas

### 3.1. Regras de Estoque
- **Limite de Reabastecimento**: Cada item possui um limite mínimo de estoque, definido como 5 unidades. Quando a quantidade cai abaixo desse valor, o reabastecimento é iniciado.
- **Reposição Automática**: Se um item está fora de estoque ou abaixo do limite, o método `iniciar_reabastecimento()` é acionado, marcando o item como em reabastecimento.
- **Conclusão do Reabastecimento**: Quando o reabastecimento é necessário, o método `concluir_reabastecimento()` adiciona uma quantidade especificada ao estoque e marca o item como disponível novamente.

### 3.2. Regras de Pedidos
- **Processamento de Pedido**: A classe `ItemAgente` verifica se há estoque suficiente para atender um pedido. Se sim, a quantidade solicitada é deduzida do estoque.
- **Pedido Parcialmente Atendido**: Se o estoque for insuficiente para atender ao pedido, a reposição é acionada, e o sistema aguarda a conclusão do reabastecimento antes de processar novamente o pedido.
- **Simulação de Tempo**: O código utiliza `time.sleep()` para simular o tempo de reabastecimento.

### 3.3. Regras de Interação com o Cliente
- **Nome do Cliente**: O cliente insere seu nome, e é criada uma instância de `ClienteAgente`.
- **Escolha de Produto**: O cliente escolhe um produto e a quantidade desejada. Se o produto não estiver disponível, uma mensagem é exibida.
- **Verificação de Estoque Pós-Pedido**: Após cada pedido, o estoque é verificado para iniciar o reabastecimento, se necessário.

## 4. Simulação da Loja
1. **Inicialização do Estoque**: Todos os produtos têm sua quantidade inicial definida aleatoriamente entre 0 e 15 unidades.
2. **Verificação Inicial**: Antes de abrir a loja, o estoque é verificado para iniciar reabastecimentos, se necessário.
3. **Interação Contínua**: O cliente pode fazer múltiplos pedidos até decidir sair. Os pedidos são processados em tempo real e o estoque é atualizado conforme necessário.
4. **Encerramento da Loja**: Ao encerrar a simulação, todos os produtos são verificados novamente para atualizar seus estoques.

## 5. Potenciais Melhorias
- **Simulação Mais Realista**: Adicionar tempos de reabastecimento variáveis e simular atrasos de entrega.
- **Gestão Avançada de Estoque**: Implementar um sistema para prever demanda e ajustar o limite de reabastecimento dinamicamente.
- **Interface Gráfica**: Criar uma interface gráfica para facilitar a interação e a visualização do estoque.

## 6. Conclusão
O código fornece uma simulação básica de uma loja com gerenciamento de estoque e interação com clientes. Ele é útil para testar lógica de inventário e automatização de processos de reabastecimento, com regras claras para pedidos e controle de produtos.

---
