import statsmodels.api as sm
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('flights.csv')
grouped = df.groupby('dest').agg(
    flight_count=('flight', 'count'),
    time_std=('air_time', 'std'),
    distance=('distance', 'mean')
).dropna().query('flight_count > 30')

X = sm.add_constant(grouped['distance'])
model = sm.OLS(grouped['time_std'], X).fit()

grouped['distance_sq'] = grouped['distance']**2
X_poly = sm.add_constant(grouped[['distance', 'distance_sq']])
model_poly = sm.OLS(grouped['time_std'], X_poly).fit()

distance_range = np.linspace(
    grouped['distance'].min(),
    grouped['distance'].max(),
    100
)

X_linear_pred = sm.add_constant(distance_range)
linear_pred = model.predict(X_linear_pred)

X_poly_pred = sm.add_constant(pd.DataFrame({
    'distance': distance_range,
    'distance_sq': distance_range**2
}))
poly_pred = model_poly.predict(X_poly_pred)

print("коэффициент детерминации R² линейной модели:", model.rsquared)
print("Коэффициент детерминации R² полиномиальной модели:", model_poly.rsquared)

plt.figure(figsize=(12, 6))
plt.scatter(grouped['distance'], grouped['time_std'], alpha=0.6, label='Data Points')

plt.plot(distance_range, linear_pred, color='red', lw=2, label='Linear Model')
plt.plot(distance_range, poly_pred, color='green', lw=2, label='Quadratic Model')

plt.xlabel('Flight Distance (miles)')
plt.ylabel('Air Time Standard Deviation (minutes)')
plt.title('Flight Time Variability vs Distance (Corrected)')
plt.legend()
plt.grid(True)
plt.show()


























