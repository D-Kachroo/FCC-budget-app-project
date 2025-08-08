# FCC Budget App Project – By: David Kachroo

This public repository contains my solution for the **"Build a Budget App"** project from the **freeCodeCamp Scientific Computing with Python** certification.

## Project Overview
The `Category` class simulates budget categories (e.g., Food, Clothing, Entertainment) with deposit, withdrawal, transfer, and balance tracking. Each category maintains a ledger of transactions and supports detailed string formatting for display.

Additionally, the `create_spend_chart` function generates a **text-based bar chart** showing the percentage of total spending per category.

### Features:
- **Category Class**:
  - Track deposits and withdrawals with optional descriptions.
  - Enforce fund checks before withdrawals or transfers.
  - Transfer funds between categories.
  - Retrieve current balance.
  - String output showing a formatted ledger and total.
- **Spending Chart**:
  - Calculates spending percentage per category based on withdrawals.
  - Rounds down to the nearest 10%.
  - Displays vertical labels for category names.
  - Matches freeCodeCamp’s exact output formatting requirements.

### Example Usage:
```python
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing = Category("Clothing")
food.transfer(50, clothing)

print(food)
print(create_spend_chart([food, clothing]))