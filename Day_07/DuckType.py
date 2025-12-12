
"""
Duck typing is a concept in Python (and some other dynamically typed languages) where the type or class
of an object is less important than the methods and properties it defines. In simple terms, Python cares what an object can do,
not what it is.
"""


# Key Idea: You don’t need explicit inheritance or type checks; as long as the object supports the required operations, it will work.

# Different payment classes
class PayPal:
    def pay(self, amount):
        print(f"Paid ${amount} using PayPal.")

class Stripe:
    def pay(self, amount):
        print(f"Paid ${amount} using Stripe.")

class BankTransfer:
    def pay(self, amount):
        print(f"Paid ${amount} using Bank Transfer.")

# Function that uses duck typing
def process_payment(payment_gateway, amount):
    # No type checking, just call the pay() method
    payment_gateway.pay(amount)

# Using different payment gateways
process_payment(PayPal(), 100)       # Paid $100 using PayPal.
process_payment(Stripe(), 200)       # Paid $200 using Stripe.
process_payment(BankTransfer(), 300) # Paid $300 using Bank Transfer.

"""
 ✅ Explanation:
 We don’t care if the object is PayPal, Stripe, or BankTransfer.
 We just call pay(amount) on it.
 If the object has a pay method, it works. If not, Python will raise an AttributeError.
"""