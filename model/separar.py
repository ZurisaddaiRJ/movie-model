import pandas as pd

data = pd.read_csv('data/movie_success_rate.csv')

# Guardar el 100% de los datos
data.to_csv('data/movie_success_rate_100.csv', index=False)

# Guardar el 50% de los datos
half_size = int(len(data) / 2)
half_data = data.iloc[:half_size]
half_data.to_csv('data/movie_success_rate_50.csv', index=False)

# Guardar el 20% de los datos
twenty_percent_size = int(len(data) * 0.25)
twenty_percent_data = data.iloc[:twenty_percent_size]
twenty_percent_data.to_csv('data/movie_success_rate_25.csv', index=False)