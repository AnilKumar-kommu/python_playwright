
"""
Method overloading is the ability of a class to have multiple methods
with the same name but different parameters (number or type of parameters).
"""

"""
Important Note: Python does not support traditional method overloading like Java or C++.
In Python, if you define multiple methods with the same name, the last one overwrites the previous ones.
"""



class Invoice:
    # Method to calculate total charges
    def calculate_total(self, base_amount, discount=0, tax=0):
        """
        Calculates total invoice amount based on base, discount, and tax.
        Arguments:
        - base_amount (float): Base price of the booking
        - discount (float, optional): Discount amount to apply
        - tax (float, optional): Tax amount to apply
        """
        total = base_amount - discount + tax
        return total

# Usage
invoice = Invoice()

# Only base amount
print("Total 1:", invoice.calculate_total(1000))  # Total 1: 1000

# Base amount + discount
print("Total 2:", invoice.calculate_total(1000, discount=100))  # Total 2: 900

# Base amount + discount + tax
print("Total 3:", invoice.calculate_total(1000, discount=100, tax=50))  # Total 3: 950
