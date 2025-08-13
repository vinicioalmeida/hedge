# BCB - Focus

from bcb import Expectativas
import matplotlib.pyplot as plt

em = Expectativas()
em.describe()
ep = em.get_endpoint("ExpectativasMercadoAnuais")

def get_previsoes(indicador, ano):
    return (ep.query()
    .filter(ep.Indicador == f"{indicador}")
    .filter(ep.Data >= f'{ano}-01-01')
    .filter(ep.DataReferencia == ano)
    .select(ep.Data, ep.Mediana)
    .collect()
    )

get_previsoes('Câmbio', 2024)

# Alternativa
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
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(datas, medianas, label='Mediana das Previsões de Câmbio')
ax.set_title('Mediana das Previsões de Câmbio')
ax.set_xlabel('Data')
ax.set_ylabel('Mediana (R$)')
ax.legend()
plt.xticks(rotation=45)
plt.tight_layout()

# Exibir o gráfico
plt.show()
