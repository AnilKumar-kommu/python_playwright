from functools import reduce

# Sample cruise booking data
bookings = [
    {"name": "Alice", "age": 25, "cabin": "Premium", "price": 2000},
    {"name": "Bob", "age": 17, "cabin": "Standard", "price": 1000},
    {"name": "Charlie", "age": 30, "cabin": "Premium", "price": 2500},
    {"name": "David", "age": 16, "cabin": "Standard", "price": 900},
]

# -------- Higher-Order Function 1: Filter --------
def filter_bookings(condition_func, bookings_list):
    """Filters bookings based on a condition function"""
    return list(filter(condition_func, bookings_list))

# Example condition: Only adults
adult_bookings = filter_bookings(lambda b: b["age"] >= 18, bookings)
print("Adult Bookings:", adult_bookings)

# Example condition: Only Premium cabins
premium_bookings = filter_bookings(lambda b: b["cabin"] == "Premium", bookings)
print("Premium Bookings:", premium_bookings)


# -------- Higher-Order Function 2: Apply Discount --------
def apply_discount(discount_func, bookings_list):
    """Applies a discount function to each booking"""
    return list(map(discount_func, bookings_list))

# Example discount: 10% off for premium cabins
discounted_bookings = apply_discount(
    lambda b: {**b, "price": b["price"] * 0.9} if b["cabin"] == "Premium" else b,
    bookings
)
print("Discounted Bookings:", discounted_bookings)


# -------- Higher-Order Function 3: Calculate Total Revenue --------
def calculate_total(reduce_func, bookings_list):
    """Calculates total revenue using a reduce function"""
    return reduce(reduce_func, [b["price"] for b in bookings_list], 0)

total_revenue = calculate_total(lambda x, y: x + y, bookings)
print("Total Revenue:", total_revenue)
