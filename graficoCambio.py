# Gráfico da evolução do câmbio

import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Defina o ticker para o par de moedas desejado, por exemplo, BRL=X para a taxa de câmbio BRL/USD.
ticker = "BRL=X"

# Defina o período desejado para o gráfico.
end_date = datetime.today().strftime('%Y-%m-%d')
start_date = (datetime.today() - timedelta(days=2*365)).strftime('%Y-%m-%d')

# Obtém os dados históricos usando yfinance.
data = yf.download(ticker, start=start_date, end=end_date)

# Crie o gráfico da evolução da taxa de câmbio.
plt.figure(figsize=(10, 6))
plt.plot(data['Close'], label='Taxa de Câmbio (BRL/USD)')
plt.title('Evolução da Taxa de Câmbio Real/Dólar')
plt.xlabel('Data')
plt.ylabel('Taxa de Câmbio')
plt.legend()
plt.show()

# Exporte o gráfico como uma imagem (por exemplo, PNG).
plt.savefig('taxa_cambio.png')


