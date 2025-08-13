import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime, timedelta
from bcb import Expectativas

# Configuração da página
st.set_page_config(page_title='Hedge Cambial')

# Título do Dashboard
st.markdown('<span style="color:gold; font-size: 48px">&#9733;</span> <span style="font-size: 48px; font-weight: bold">Hedge Cambial</span>', unsafe_allow_html=True)

# Descrição e Explicação
st.write('''Este dashboard ajuda importadores e exportadores na definição de políticas de hedge cambial usando 
         futuros/termo de dólar. Abaixo, três figuras: 1. Resultado do hedge. 2. Comportamento da taxa de câmbio 
         nos últimos dois anos. 3. Comportamento da mediana das previsões da taxa de câmbio para final do ano 
         corrente segundo Boletim Focus-Bacen. 4. Comportamento da mediana das previsões da taxa de câmbio para 
         final do ano seguinte segundo Boletim Focus-Bacen.''')


st.sidebar.markdown("""
    Prof. Vinicio Almeida
    vinicio.almeida@ufrn.br
                    
    https://sites.google.com/view/vinicioalmeida/                
    """)
st.sidebar.markdown('---')

# Seleção do tipo de análise
tipo_analise = st.sidebar.selectbox('Selecione o Tipo de Análise', ('Exportação', 'Importação'))

# Inputs do Usuário
st.sidebar.header('Parâmetros do Hedge')

if tipo_analise == 'Exportação':
    valor_exportacao = st.sidebar.number_input('Valor da Exportação (em USD)', min_value=0.0, value=100000.0)
    taxa_cambio_atual = st.sidebar.number_input('Taxa de Câmbio Atual (USD/BRL)', min_value=0.0, value=5.25)
    contrato_futuro = st.sidebar.number_input('Taxa do Contrato Futuro (USD/BRL)', min_value=0.0, value=5.30)
    percentual_hedge = st.sidebar.slider('Percentual da Exportação a Ser Hedgeado (%)', min_value=0, max_value=100, value=50)
    
    if valor_exportacao > 0 and taxa_cambio_atual > 0 and contrato_futuro > 0:
        valor_hedgeado = valor_exportacao * (percentual_hedge / 100)
        valor_nao_hedgeado = valor_exportacao - valor_hedgeado

        recebimento_com_hedge = valor_hedgeado * contrato_futuro + valor_nao_hedgeado * taxa_cambio_atual
        recebimento_sem_hedge = valor_exportacao * taxa_cambio_atual

        st.sidebar.subheader('Resultado do Hedge')
        st.sidebar.write(f'Valor Recebido com Hedge: R$ {recebimento_com_hedge:.2f}')
        st.sidebar.write(f'Valor Recebido sem Hedge: R$ {recebimento_sem_hedge:.2f}')

        # Gráfico de Resultado do Hedge
        valores = np.linspace(3.5, 7.0, 100)
        recebimento_hedge_var = valor_hedgeado * contrato_futuro + valor_nao_hedgeado * valores
        recebimento_sem_hedge = valor_exportacao * valores

        fig, ax = plt.subplots()
        ax.plot(valores, recebimento_sem_hedge, label='Recebimento sem Hedge')
        ax.plot(valores, recebimento_hedge_var, label=f'Recebimento com Hedge ({percentual_hedge}%)', linestyle='--')
        ax.axhline(0, color='gray', linewidth=0.5, linestyle='--')
        ax.axvline(taxa_cambio_atual, color='red', linewidth=0.5, linestyle='--', label='Taxa Atual')
        ax.set_title('Payoff da Estratégia')
        ax.set_xlabel('Taxa de Câmbio (USD/BRL)')
        ax.set_ylabel('Recebimento (R$)')
        ax.legend()
        st.pyplot(fig)
    
    else:
        st.sidebar.warning('Insira o valor de exportação, a taxa de câmbio atual e a taxa do contrato futuro.')

elif tipo_analise == 'Importação':
    valor_importacao = st.sidebar.number_input('Valor da Importação (em USD)', min_value=0.0, value=100000.0)
    taxa_cambio_atual = st.sidebar.number_input('Taxa de Câmbio Atual (USD/BRL)', min_value=0.0, value=5.25)
    contrato_futuro = st.sidebar.number_input('Taxa do Contrato Futuro (USD/BRL)', min_value=0.0, value=5.30)
    percentual_hedge = st.sidebar.slider('Percentual da Importação a Ser Hedgeado (%)', min_value=0, max_value=100, value=50)
    
    if valor_importacao > 0 and taxa_cambio_atual > 0 and contrato_futuro > 0:
        valor_hedgeado = valor_importacao * (percentual_hedge / 100)
        valor_nao_hedgeado = valor_importacao - valor_hedgeado

        custo_com_hedge = valor_hedgeado * contrato_futuro + valor_nao_hedgeado * taxa_cambio_atual
        custo_sem_hedge = valor_importacao * taxa_cambio_atual

        st.sidebar.subheader('Resultado do Hedge')
        st.sidebar.write(f'Custo com Hedge: R$ {custo_com_hedge:.2f}')
        st.sidebar.write(f'Custo sem Hedge: R$ {custo_sem_hedge:.2f}')

        # Gráfico de Resultado do Hedge
        valores = np.linspace(3.5, 7.0, 100)
        custo_hedge_var = valor_hedgeado * contrato_futuro + valor_nao_hedgeado * valores
        custo_sem_hedge = valor_importacao * valores

        fig, ax = plt.subplots()
        ax.plot(valores, custo_sem_hedge, label='Custo sem Hedge')
        ax.plot(valores, custo_hedge_var, label=f'Custo com Hedge ({percentual_hedge}%)', linestyle='--')
        ax.axhline(0, color='gray', linewidth=0.5, linestyle='--')
        ax.axvline(taxa_cambio_atual, color='red', linewidth=0.5, linestyle='--', label='Taxa Atual')
        ax.set_title('Payoff da Estratégia')
        ax.set_xlabel('Taxa de Câmbio (USD/BRL)')
        ax.set_ylabel('Custo (R$)')
        ax.legend()
        st.pyplot(fig)
    
    else:
        st.sidebar.warning('Insira o valor de importação, a taxa de câmbio atual e a taxa do contrato futuro.')

## Histórico da taxa de câmbio
ticker = "BRL=X"
# Defina o período desejado para o gráfico.
end_date = datetime.today().strftime('%Y-%m-%d')
start_date = (datetime.today() - timedelta(days=2*365)).strftime('%Y-%m-%d')
# Obtém os dados históricos usando yfinance.
data = yf.download(ticker, start=start_date, end=end_date)
# Crie o gráfico da evolução da taxa de câmbio.
fig, ax = plt.subplots()
ax.plot(data['Close'])
ax.set_title('Evolução da Taxa de Câmbio Real/Dólar')
ax.set_xlabel('Data')
ax.set_ylabel('Taxa de Câmbio')
ax.legend()
ax.tick_params(axis='x', labelsize=8)
st.pyplot(fig)

## Histórico das previsões divulgadas no Focus-BCB
em = Expectativas()
ep = em.get_endpoint("ExpectativasMercadoAnuais")

def get_previsoes(indicador, ano):
    previsoes = (ep.query()
                 .filter(ep.Indicador == f"{indicador}")
                 .filter(ep.Data >= f'{ano-1}-01-01')
                 .filter(ep.DataReferencia == ano)
                 .select(ep.Data, ep.Mediana)
                 .orderby(ep.Data.desc())  # Corrigido para 'orderby'
                 .limit(1000)  # Limitar as últimas 252 previsões
                 .collect())
    return previsoes

# Obter as previsões
previsoes = get_previsoes('Câmbio', 2024)

# Se previsoes é um DataFrame
datas = previsoes['Data']
medianas = previsoes['Mediana']

# Reverter a lista para ordem cronológica
datas = datas[::-1]
medianas = medianas[::-1]

# Criar o gráfico
fig, ax = plt.subplots()
ax.plot(datas, medianas)
ax.set_title('Mediana das Previsões de Câmbio para Final de 2024')
ax.set_xlabel('Data')
ax.set_ylabel('Mediana (R$)')
ax.legend()
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig)


## E 2025
# Obter as previsões
previsoes = get_previsoes('Câmbio', 2025)

# Se previsoes é um DataFrame
datas = previsoes['Data']
medianas = previsoes['Mediana']

# Reverter a lista para ordem cronológica
datas = datas[::-1]
medianas = medianas[::-1]

# Criar o gráfico
fig, ax = plt.subplots()
ax.plot(datas, medianas)
ax.set_title('Mediana das Previsões de Câmbio para Final de 2025')
ax.set_xlabel('Data')
ax.set_ylabel('Mediana (R$)')
ax.legend()
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig)