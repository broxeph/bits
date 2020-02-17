"""
This jawn figures out when you can afford a house.

In other news, something something opportunity cost index fund.
"""
COLUMN_WIDTH = 10
YEARS = 10
balance = 1000
monthly_savings = 2000

print(f"Starting balance: {balance:,}")
print(f"Monthly savings: {monthly_savings:,}\n")

print("Year".ljust(COLUMN_WIDTH) + "Balance".ljust(COLUMN_WIDTH))
for month in range(YEARS * 12):
    if not month % 12:
        print(str(month // 12).ljust(COLUMN_WIDTH) + f"{balance:,}".ljust(COLUMN_WIDTH))

    balance += monthly_savings
