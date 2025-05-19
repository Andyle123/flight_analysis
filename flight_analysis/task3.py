from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('flights.csv')

jfk_flights = df[df['origin'] == 'JFK'].dropna(subset=['dep_time', 'dep_delay'])

jfk_flights['hour'] = (jfk_flights['dep_time'] // 100).clip(0, 23)

hour_counts = jfk_flights['hour'].value_counts().sort_index()

plt.figure(figsize=(12, 6))
hour_counts.plot(kind='bar', color='teal')
plt.title('Departure Distribution at JFK by Hour')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Flights')
plt.xticks(range(0, 24), rotation=0)
plt.show()

peak_hours = hour_counts.nlargest(2).index.sort_values()

morning = jfk_flights[jfk_flights['hour'] == peak_hours[0]]['dep_delay']
afternoon = jfk_flights[jfk_flights['hour'] == peak_hours[1]]['dep_delay']

t_stat, p_value = stats.ttest_ind(morning, afternoon, equal_var=False)
print(f"пиковые часы {peak_hours[0]}时 vs {peak_hours[1]}时")
print(f"средняя задержка: {morning.mean():.1f} vs {afternoon.mean():.1f} 分钟")
print(f"p-значение независимого t-критерия Стьюдента: {p_value:.4f}")




























