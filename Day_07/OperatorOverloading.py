class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    # Overload '+' operator to add balances of two accounts
    def __add__(self, other):
        if isinstance(other, BankAccount):
            return self.balance + other.balance
        raise TypeError("Operand must be a BankAccount object")

    # Overload '==' operator to compare balances
    def __eq__(self, other):
        if isinstance(other, BankAccount):
            return self.balance == other.balance
        return False

    # Overload '<' operator to compare balances
    def __lt__(self, other):
        if isinstance(other, BankAccount):
            return self.balance < other.balance
        return False

    # Human-readable representation
    def __str__(self):
        return f"Account {self.account_number}: Balance = ${self.balance}"

# Example usage
acc1 = BankAccount("A101", 5000)
acc2 = BankAccount("A102", 3000)
acc3 = BankAccount("A103", 5000)

# Adding balances
total_balance = acc1 + acc2
print("Total Balance:", total_balance)  # Output: Total Balance: 8000

# Comparing balances
print(acc1 == acc3)  # Output: True
print(acc2 < acc1)   # Output: True

# Printing account info
print(acc1)          # Output: Account A101: Balance = $5000
