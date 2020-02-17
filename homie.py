#!/usr/bin/env python3
"""
This jawn figures out when you can afford a house.

In other news, something something opportunity cost index fund.
"""
COLUMN_WIDTH = 10
YEARS = 10
STARTING_BALANCE = 20_000
MONTHLY_SAVINGS = 2_000
HOUSE_PRICE = 500_000
PMI_RATE = 0.03
INDEX_RETURN = 0.09
MORTGAGE_INTEREST = 0.04
MORTGAGE_TERM = 30  # Years
DOWN_PAYMENT_A = 0
DOWN_PAYMENT_B = 20_000

balance_a = STARTING_BALANCE - DOWN_PAYMENT_A
balance_b = STARTING_BALANCE - DOWN_PAYMENT_B

print(f"Starting balance: {STARTING_BALANCE:,}")
print(f"Monthly savings: {MONTHLY_SAVINGS:,}")
print(f"House price: {HOUSE_PRICE:,}")
print(f"PMI rate: {PMI_RATE}")
print(f"Index fund return: {INDEX_RETURN}")
print(f"Mortgage interest: {MORTGAGE_INTEREST}")

print()
print("Year".ljust(7) + f"{DOWN_PAYMENT_A:,} Down".ljust(COLUMN_WIDTH) + f"{DOWN_PAYMENT_B:,} Down".ljust(COLUMN_WIDTH))
for month in range(YEARS * 12):
    if not month % 12:
        print(str(month // 12).ljust(7) + f"{balance_a:,}".ljust(COLUMN_WIDTH) + f"{balance_b:,}".ljust(COLUMN_WIDTH))

    balance_a += MONTHLY_SAVINGS
    balance_b += MONTHLY_SAVINGS
