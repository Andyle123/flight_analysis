import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('flights.csv')
print(f"shape of df: {df.shape}")

ny_flights = df[df['origin'].isin(['JFK', 'LGA', 'EWR'])]
print(f"flights from NY: {ny_flights.shape[0]}")

top_dests = ny_flights['dest'].value_counts().nlargest(10).index

clean_df = ny_flights.dropna(subset=['arr_delay'])
print(clean_df.shape[0], ny_flights.shape[0], clean_df.shape[0] / ny_flights.shape[0])

delay_probs = (clean_df[clean_df['dest'].isin(top_dests)]
               .groupby('dest')['arr_delay']
               .apply(lambda x: (x > 0).mean())
               .reindex(top_dests))

plt.figure(figsize=(12, 6))
delay_probs.plot(kind='bar', color='skyblue')
plt.title('Arrival Delay Probability by Destination (Top 10 from NYC)')
plt.xlabel('Destination Airport')
plt.ylabel('Delay Probability')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

max_delay = delay_probs.idxmax()
min_delay = delay_probs.idxmin()
print(f"Аэропорты с наивысшей вероятностью задержек: {max_delay} ({delay_probs[max_delay]:.2%})")
print(f"Аэропорты с наименьшей вероятностью задержек рейсов: {min_delay} ({delay_probs[min_delay]:.2%})")





























