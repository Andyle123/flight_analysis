import numpy as np
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('flights.csv')
print(f"Origin data shape: {df.shape}")

sfo_flights = df[(df['dest'] == 'SFO') &
                (df['origin'].isin(['JFK', 'LGA', 'EWR']))].dropna(subset=['air_time'])
print(f"SFO flights data shape: {sfo_flights.shape}")

air_time = sfo_flights['air_time']
mu, sigma = air_time.mean(), air_time.std()

print(f"mu = {mu:.2f}, sigma = {sigma:.1f}")

plt.figure(figsize=(12, 6))
sns.histplot(air_time, kde=False, stat='density', bins=20)
x = np.linspace(air_time.min(), air_time.max(), 100)
plt.plot(x, stats.norm.pdf(x, mu, sigma), 'r-', lw=2)
plt.title('Flight Time Distribution (NYC to SFO)')
plt.xlabel('Air Time (minutes)')
plt.ylabel('Density')

ci = stats.norm.interval(0.95, loc=mu, scale=sigma)
print(f"95% доверительный интервал: {ci[0]:.1f} - {ci[1]:.1f} minutes")

plt.figure(figsize=(12, 6))
stats.probplot(air_time, plot=plt)
plt.title('Q-Q Plot for Normality Check')
plt.show()





























