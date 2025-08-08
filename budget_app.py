class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            desc = item["description"][:23]
            amt = f"{item['amount']:.2f}"
            items += f"{desc:<23}{amt:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    title = "Percentage spent by category\n"
    spent = []
    for category in categories:
        total_spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                total_spent += abs(item["amount"])
        spent.append(total_spent)
    total = sum(spent)
    percentages = [int((s / total) * 10) * 10 for s in spent]

    chart = ""
    for i in range(100, -1, -10):
        chart += f"{i:>3}|"
        for p in percentages:
            chart += " o " if p >= i else "   "
        chart += " \n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len = max(len(c.name) for c in categories)
    for i in range(max_len):
        chart += "     "
        for c in categories:
            if i < len(c.name):
                chart += f"{c.name[i]}  "
            else:
                chart += "   "
        chart += "\n"

    return title + chart.rstrip("\n")