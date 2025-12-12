# ==============================
# Bank Account Management System
# Demonstrates multiple magic methods in Python
# ==============================

class BankAccount:
    # __init__ is called when a new account is created
    def __init__(self, account_number, owner, balance=0):
        """
        Real-life use: Initialize a new bank account with account number, owner name, and balance.
        """
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    # __str__ is called when print() is used on the object
    def __str__(self):
        """
        Real-life use: Display a friendly message when printing account details.
        """
        return f"BankAccount({self.account_number}) - Owner: {self.owner}, Balance: ${self.balance}"

    # __repr__ is useful for debugging and developer-friendly representation
    def __repr__(self):
        """
        Real-life use: Logs or debugging.
        """
        return f"BankAccount('{self.account_number}', '{self.owner}', {self.balance})"

    # __add__ allows adding balances of two accounts
    def __add__(self, other):
        """
        Real-life use: Merge two accounts or calculate total balance easily.
        """
        if isinstance(other, BankAccount):
            return self.balance + other.balance
        return NotImplemented

    # __eq__ allows comparison of account balances using '=='
    def __eq__(self, other):
        """
        Real-life use: Check if two accounts have the same balance.
        """
        if isinstance(other, BankAccount):
            return self.balance == other.balance
        return NotImplemented

    # __lt__ allows comparison using '<' operator
    def __lt__(self, other):
        """
        Real-life use: Compare account balances for ranking or sorting.
        """
        if isinstance(other, BankAccount):
            return self.balance < other.balance
        return NotImplemented

    # __len__ allows using len() to get the number of transactions (simulated here)
    def __len__(self):
        """
        Real-life use: Get number of transactions for an account.
        """
        return len(getattr(self, 'transactions', []))

    # __getitem__ allows index-based access to transactions
    def __getitem__(self, index):
        """
        Real-life use: Access individual transactions by index.
        """
        return self.transactions[index]

    # __call__ allows treating the object like a function to get account summary
    def __call__(self):
        """
        Real-life use: Quickly get account summary using a callable object.
        """
        return f"Account Summary -> {self}"

    # Context manager to simulate safe access to account (like a database connection)
    def __enter__(self):
        """
        Real-life use: Begin secure transaction/session.
        """
        print(f"Accessing account {self.account_number} safely...")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Real-life use: End transaction/session, close safely.
        """
        print(f"Exiting account {self.account_number}. Session closed.")

    # Adding a method to simulate transactions
    def add_transaction(self, amount):
        if not hasattr(self, 'transactions'):
            self.transactions = []
        self.transactions.append(amount)
        self.balance += amount
        print(f"Transaction of ${amount} completed. New balance: ${self.balance}")


# ==============================
# Example Usage
# ==============================

# Creating bank accounts
acc1 = BankAccount("A001", "Alice", 1000)
acc2 = BankAccount("B001", "Bob", 2000)

# Printing accounts (calls __str__)
print(acc1)  # BankAccount(A001) - Owner: Alice, Balance: $1000
print(acc2)  # BankAccount(B001) - Owner: Bob, Balance: $2000

# Merging balances (calls __add__)
total_balance = acc1 + acc2
print(f"Total Balance of both accounts: ${total_balance}")  # 3000

# Comparing balances (calls __eq__ and __lt__)
print(acc1 == acc2)  # False
print(acc1 < acc2)   # True

# Adding transactions
acc1.add_transaction(500)
acc1.add_transaction(-200)

# Using len() (calls __len__)
print(f"Number of transactions for {acc1.owner}: {len(acc1)}")  # 2

# Access transactions by index (calls __getitem__)
print(f"First transaction: ${acc1[0]}")  # 500

# Using callable object (calls __call__)
print(acc1())  # Account Summary -> BankAccount(A001) - Owner: Alice, Balance: $1300

# Using context manager (calls __enter__ and __exit__)
with acc2 as account:
    ac=account.add_transaction(1000)
print(ac)