# Gestão de Contas - Organização Fonte de Dados
# TABELAS PLANEJADAS
1. Despesas Recentes
    * Data Pagamento (Faturamento) - Data limite para pagamento da despesa.
    * Data (Data Compra) - Data em que a despesa foi contratada/comprada.
    * Categoria - Categoria para segmentar as despesas baseado no tipo de produto ou serviço.
    * Descrição - Mensagem ou texto para identificar a despesa.
    * Valor
    * Metodo Pagamento (Operação) - Para identificar qual metódo de pagamento foi utilizado para pagar a despesa.
    * Pagador Efetivo (Responsavel) - Responsavél por gerar o dinheiro para o pagamento daquela despesa.
    * Situação - Status atual da Despesa (paga/em aberto/vencida)

2. Extratos Contas Bancárias
    * Data - Data da movimentação bancária
    * Valor
    * Descrição - Mensagem ou texto para identificar a movimentação da conta: conta de destino, produto ou serviço adquirido.
    * Categoria - Categoria para segmentar as movimentações baseado no tipo de produto ou serviço.
    * Metodo Pagamento - Para identificar qual metódo de pagamento foi utilizado para pagar a despesa. 
    * Movimentação - Define se é uma movimentação de entrada (receita) ou saída (Despesa) da conta bancária.
    * Conta - (Conta + Instituição Bancária) 

3. Fatura de Cartões
    * Mes Fechamento Fatura
    * Data Despesa
    * Valor
    * Descrição
    * Categoria
    * Cartão (Conta + Cartão de Crédito)

    Nesse caso o Metodo de Pagamento sempre será cartão de crédito, e também a movimentação sempre é de saída tendo em vista que é um gasto do cartão de crédito.

4. Historico Despesas
    * Data
    * Valor
    * Descrição
    * Metodo de Pagamento
    * Categoria
    * Origem Despesa = Fatura Cartão Crédito ou Movimentação na Conta

# INFORMAÇÕES GERADAS ABA DASHBOARDS

## 1.0 DESPESAS PENDENTES
* Situação, Metódo de Pagamento, Valor.
* Cálculo: Saldo Líquido, Total Despesas, Dinheiro Guardado/Investido, Saldo em Conta, Despesas Em Aberto, Despesas Pendentes.
* Tabela com todas despesas pendentes.
* Ranking de categorias por despesas.

## 2.0 CONTAS BANCÁRIAS
* Saldo em Conta.
* Tabela com últimas transações.
* Categorias que mais movimentaram valores.
* Ganhos em investimentos.
* Total Investido.
* Principais Receitas.
* Principais Despesas.

## 3.0 FATURAS CARTÕES
1. FATURA ATUAL
    * Tabela com todos os gasotos.
    * Total Fatura.
    * Ranking de Categorias Despesas.

2. HISTÓRICO DE FATURAS
    * Gráfico com variação de total das faturas.
    * Gráfico de Responsavel por gastos.
    * Gráfico de Categorias das Despesas.

## HISTÓRICO DESPESAS
* Histórico Mensal de Despesas.
* Total de Despesas Pagas.
* Principais Responsaveis pelas Despesas.
* Principais Categorias das Despesas.


# Fluxo de utilização do site
1. Usuário cadastra cada nova despesa em Despesa Pendente.
2. Após pagar ele enquadra essa despesa em alguma fatura ou em uma movimentação de conta.
3. Após isso o site gera os relatórios e as páginas de gastos.