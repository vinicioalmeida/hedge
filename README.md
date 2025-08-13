# Hedge Cambial - Dashboard para Análise de Risco Cambial

Um dashboard interativo desenvolvido em Streamlit para auxiliar importadores e exportadores na definição de políticas de hedge cambial utilizando contratos futuros/termo de dólar.

## Descrição

Este aplicativo oferece uma ferramenta prática para análise de estratégias de hedge cambial, permitindo visualizar os impactos financeiros de diferentes cenários de câmbio tanto para operações de exportação quanto de importação. O dashboard fornece análises visuais abrangentes incluindo payoffs de estratégias, histórico cambial e previsões de mercado.

## Funcionalidades

### Análise de Exportação
- Cálculo de recebimentos com e sem hedge
- Visualização do payoff da estratégia de hedge
- Análise de diferentes percentuais de cobertura cambial

### Análise de Importação  
- Cálculo de custos com e sem hedge
- Comparação de cenários de proteção cambial
- Otimização do percentual de hedge

### Dados de Mercado
- Histórico da taxa de câmbio Real/Dólar dos últimos 2 anos
- Previsões do mercado via Boletim Focus do Banco Central
- Evolução das expectativas para o ano corrente e seguinte

## Requisitos

```
streamlit
numpy
matplotlib
yfinance
python-bcb
```

## Instalação

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITORIO]
cd hedge-cambial
```

2. Instale as dependências:
```bash
pip install streamlit numpy matplotlib yfinance python-bcb
```

## Como Usar

1. Execute o aplicativo:
```bash
streamlit run app.py
```

2. Acesse o dashboard no navegador (geralmente `http://localhost:8501`)

3. Configure os parâmetros na barra lateral:
   - Escolha entre análise de Exportação ou Importação
   - Defina o valor da operação em USD
   - Insira a taxa de câmbio atual
   - Configure a taxa do contrato futuro
   - Ajuste o percentual de hedge desejado

4. Analise os resultados nos gráficos gerados automaticamente

## Parâmetros de Entrada

- **Valor da Operação**: Valor em dólares americanos da exportação/importação
- **Taxa de Câmbio Atual**: Taxa spot USD/BRL vigente
- **Taxa do Contrato Futuro**: Taxa do contrato futuro/termo para hedge
- **Percentual de Hedge**: Porcentagem da exposição a ser protegida (0-100%)

## Saídas e Visualizações

1. **Payoff da Estratégia**: Gráfico comparando resultados com e sem hedge
2. **Evolução Cambial**: Histórico de 2 anos da taxa USD/BRL
3. **Previsões Focus-BCB**: Expectativas do mercado para final do ano atual
4. **Previsões Focus-BCB**: Expectativas do mercado para final do próximo ano

## Dados Utilizados

- **Yahoo Finance (yfinance)**: Cotações históricas USD/BRL
- **BCB Expectativas**: Previsões do Boletim Focus do Banco Central do Brasil

## Autor

**Prof. Vinicio Almeida**  
Universidade Federal do Rio Grande do Norte (UFRN)  
Email: vinicio.almeida@ufrn.br  
Site: https://sites.google.com/view/vinicioalmeida/

## Estrutura do Projeto

```
├── app.py                 # Arquivo principal do aplicativo
├── README.md             # Este arquivo
└── requirements.txt      # Dependências do projeto
```

## Observações Técnicas

- O aplicativo utiliza dados em tempo real via APIs públicas
- As previsões Focus-BCB são atualizadas automaticamente
- O período padrão para análise histórica é de 2 anos
- Todas as operações são calculadas considerando USD como moeda base

## Licença

Este projeto é de uso acadêmico e educacional.