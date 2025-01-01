import matplotlib.pyplot as plt
import numpy as np

# Hourly

hours = np.arange(24)
total_trades = [
    110722, 109597, 105102, 95940, 87911, 79910, 78257, 82415, 85590, 75501,
    70617, 76537, 90573, 97019, 105960, 112885, 114045, 122667, 126354, 129177,
    130450, 130294, 124859, 115254
]

money_moved = [
    167322.85, 168023.12, 183600.78, 179344.17, 218432.74, 165634.11, 151524.64,
    141952.03, 124852.56, 121369.10, 92261.61, 92705.57, 95569.87, 93101.67, 154081.92,
    161281.31, 144468.86, 158073.49, 156794.35, 187635.39, 192911.56, 177146.64,
    193904.16, 194297.24
]


plt.figure(figsize=(10, 6))
plt.plot(hours, total_trades, label='Total Trades', marker='o')
plt.plot(hours, money_moved, label='Money Moved', marker='o')

plt.xlabel('Hour of the Day')
plt.ylabel('Trade Count')
plt.title('Total Trades and Money Moved by Hour of the Day')
plt.xticks(hours)
plt.legend()

plt.savefig('Hourly.png')

# Weekly

hours = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
total_trades = [397266, 352726, 352134, 349130, 329902, 341741, 370280]
money_moved = [509982.40, 461864.41, 456240.22, 431593.36, 411712.97, 396818.95, 444006.50]

plt.figure(figsize=(10, 6))
plt.plot(hours, total_trades, label='Total Trades', marker='o')
plt.plot(hours, money_moved, label='Money Moved', marker='o')

plt.xlabel('Day of the Week')
plt.ylabel('Trade Count')
plt.title('Total Trades and Money Moved by Day of the Week')
plt.xticks(hours)
plt.legend()

plt.savefig('Daily.png')

# Monthly

months = ['2023-01', '2023-02', '2023-03', '2023-04', '2023-05', '2023-06', '2023-07', '2023-08', '2023-09', '2023-10', '2023-11', '2023-12']
total_trades = [271404, 193665, 222917, 185720, 219461, 185709, 209809, 231064, 188742, 185537, 195958, 203193]
money_moved = [292793.48, 193129.92, 259635.81, 253606.95, 232034.37, 172846.79, 291856.94, 381505.07, 224038.00, 260495.24, 217322.43, 332953.81]

plt.figure(figsize=(10, 6))
plt.plot(months, total_trades, label='Total Trades')
plt.plot(months, money_moved, label='Money Moved', alpha=0.7)

plt.xlabel('Month')
plt.ylabel('Trade Count')
plt.title('Total Trades and Money Moved by Month')
plt.xticks(months)
plt.legend()

plt.savefig('Monthly.png')