import pandas as pd
import matplotlib.pyplot as plt



pd.to_datetime('2018-01-15 3:45pm')
opsd_daily = pd.read_csv('opsd_germany_daily.csv', index_col=0, parse_dates=True)
print(opsd_daily.shape)

print(opsd_daily.head(3))
# Add columns with year, month, and weekday name
opsd_daily['Year'] = opsd_daily.index.year
opsd_daily['Month'] = opsd_daily.index.month
"""add column weekday   dayofweek  0,1,2,3,4,5,6"""
opsd_daily['Weekday'] = opsd_daily.index.dayofweek
# Display a random sampling of 5 rows
print(opsd_daily.sample(5, random_state=0))
print(opsd_daily.head(3))


""""We can also select a slice of days, such as '2014-01-20':'2014-01-22'. 
As with regular label-based indexing with loc, the slice is inclusive of both endpoints."
"""
print(opsd_daily.loc['2014-01-20':'2014-01-22'])

# opsd_daily['Consumption'].plot(linewidth=0.5);
cols_plot = ['Consumption', 'Solar', 'Wind']
axes = opsd_daily[cols_plot].plot(marker='.', alpha=0.5, linestyle='None', figsize=(11, 9), subplots=True)
for ax in axes:
    ax.set_ylabel('Daily Totals (GWh)')
plt.show()
