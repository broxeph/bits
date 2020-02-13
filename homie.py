"""
This jawn figures out when you can afford a house.

In other news, something something opportunity cost index fund.
"""
balance = 1000
monthly_savings = 2000

for month in range(30 * 12):
    if not month % 12:
        print(f'Year {month // 12}: {balance}')

    balance += monthly_savings
