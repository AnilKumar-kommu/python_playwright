#tuple in python
# tuple methods in python
# tuple used in python give me real time examples also with hints and comments
#tuple rules in python
# 1. Tuples are immutable, meaning once created, their elements cannot be changed.
# 2. Tuples can contain elements of different data types.
# 3. Tuples support indexing and slicing, similar to lists.
# 4. Tuples can be nested, meaning a tuple can contain other tuples as elements.
# 5. Tuples can be created with or without parentheses, but using parentheses is a common practice.
# 6. Tuples can be unpacked into individual variables.
# 7. Tuples can be used as keys in dictionaries because they are hashable.

#what are the differences between list and tuple in python
# 1. Mutability: Lists are mutable (can be changed), while tuples are immutable (cannot be changed).
# 2. Syntax: Lists are defined using square brackets [], while tuples are defined using parentheses ().
# 3. Performance: Tuples are generally faster than lists for certain operations due to their immutability.
# 4. Use Cases: Lists are used for collections of items that may change, while tuples are used for fixed collections of items.
# 5. Methods: Lists have more built-in methods for modification (like append, remove), while tuples have fewer methods (like count, index).
# 6. Memory Usage: Tuples typically use less memory than lists due to their immutability.
# 7. Hash ability: Tuples can be used as keys in dictionaries, while lists cannot.

# why the tuple consept coming into the picture in python
# Tuples were introduced in Python to provide a way to group related data together in an immutable structure. The concept of tuples brings several advantages to the table:
# 1. Immutability: Tuples are immutable, meaning their contents cannot be changed after creation. This immutability is useful for ensuring data integrity, as it prevents accidental modifications to the data.
# 2. Performance: Tuples are generally more memory-efficient and faster than lists for certain operations due to their immutability. This makes them suitable for scenarios where performance is critical.
# 3. Data Integrity: Since tuples cannot be modified, they are ideal for representing fixed collections of data, such as coordinates, RGB color values, or configuration settings.
# 4. Hash ability: Tuples can be used as keys in dictionaries and elements in sets because they are hashable. This allows for more complex data structures and relationships.
# 5. Clarity and Intent: Using tuples can signal to other developers that the data is not meant to be changed, enhancing code readability and intent.
# 6. Multiple Return Values: Tuples are commonly used to return multiple values from functions, providing a convenient way to group related results.

# what are the real time application of tuple in python
# 1. Storing Coordinates: Tuples are often used to represent geographical coordinates (latitude and longitude) because these values are fixed and should not change.
# 2. RGB Color Values: Tuples are used to store RGB color values in graphics programming, as the color components (red, green, blue) are constant.
# 3. Configuration Settings: Tuples can hold configuration settings for applications, such as database connection parameters (host, port, username, password).
# 4. Function Return Values: Tuples are commonly used to return multiple values from functions, allowing for easy unpacking of results.
# 5. Dictionary Keys: Tuples can serve as keys in dictionaries, enabling the use of composite keys made up of multiple values.
# 6. Immutable Data Structures: Tuples are used in scenarios where data integrity is crucial, such as in financial applications where transaction records should not be altered.
# 7. Data Analysis: Tuples can be used to store fixed sets of data points in data analysis tasks, such as time series data or statistical measurements.
# 8. Web Development: Tuples can be used to store session data or user information in web applications, where the data should remain unchanged during a session.
# 9. Automation Testing: Tuples can be used to store test case parameters and expected results in automation testing frameworks.
# 10. Financial Calculations: Tuples can be used to represent financial transactions, where each transaction consists of fixed attributes like transaction ID, date, amount, and status.






# Example of tuple usage in Python
# Creating a tuple
person = ("Alice", 30, "Engineer")
print(person)  # ('Alice', 30, 'Engineer')

# Accessing elements
print(person[0])  # 'Alice'
print(person[-1])  # 'Engineer'
# Slicing a tuple
print(person[0:2])  # ('Alice', 30)
# Unpacking a tuple
name, age, profession = person
print(name)       # 'Alice'
print(age)        # 30
print(profession) # 'Engineer'
# Tuple length
print(len(person))  # 3
# Iterating through a tuple
for item in person:
    print(item)
# Output:
# Alice
# 30
# Engineer
# Checking membership
print("Alice" in person)  # True
print("Doctor" not in person)  # True
# Tuple concatenation
person2 = ("Bob", 25, "Designer")
combined = person + person2
print(combined)  # ('Alice', 30, 'Engineer', 'Bob', 25, 'Designer')
# Tuple repetition
repeated = person * 2
print(repeated)  # ('Alice', 30, 'Engineer', 'Alice', 30, 'Engineer')
# Real-time example: Storing coordinates
coordinates = (40.7128, -74.0060)  # Latitude and Longitude
print(f"Coordinates: {coordinates}")  # (40.7128, -74.0060)
latitude, longitude = coordinates
print(f"Latitude: {latitude}, Longitude: {longitude}")  # Latitude: 40.7128, Longitude: -74.0060

# Tuple methods
sample_tuple = (1, 2, 3, 2, 4, 2)
# count() method
count_of_twos = sample_tuple.count(2)
print(f"Count of 2 in sample_tuple: {count_of_twos}")  # 3
# index() method
index_of_three = sample_tuple.index(3)
print(f"Index of 3 in sample_tuple: {index_of_three}")  # 2
# Real-time example: Storing RGB color values
rgb_color = (255, 0, 0)  # Red color
print(f"RGB Color: {rgb_color}")  # (255, 0, 0)
r, g, b = rgb_color
print(f"Red: {r}, Green: {g}, Blue: {b}")  # Red: 255, Green: 0, Blue: 0
# Real-time example: Using tuples as dictionary keys
location_data = {(40.7128, -74.0060): "New York",
                 (34.0522, -118.2437): "Los Angeles",
                 (41.8781, -87.6298): "Chicago"}
print(location_data)
# Output: {(40.7128, -74.006): 'New York', (34.0522, -118.2437): 'Los Angeles', (41.8781, -87.6298): 'Chicago'}
# Accessing city names using coordinates
ny_city = location_data[(40.7128, -74.0060)]
print(f"City at (40.7128, -74.0060): {ny_city}")  # City at (40.7128, -74.0060): New York
# Real-time example: Storing immutable configuration settings
config_settings = ("localhost", 8080, True)  # (host, port, debug_mode)
host, port, debug_mode = config_settings
print(f"Host: {host}, Port: {port}, Debug Mode: {debug_mode}")
# Output: Host: localhost, Port: 8080, Debug Mode: True

# Real-time example: mostly used in real time automation testing
def get_user_info():
    # Simulating fetching user info from a database
    return ("JohnDoe", "test","@example.com", 28)
username, password,email, age = get_user_info()
print(f"Username: {username}, Password: {password}, Email: {email}, Age: {age}")
# Output: Username: JohnDoe, Password: test, Email: @example.com, Age: 28
# Real-time example: mostly used in real time data analysis
data_point = (2024, "June", 15, 75.5)  # (year, month, day, temperature)
year, month, day, temperature = data_point
print(f"Date: {year}-{month}-{day}, Temperature: {temperature}°F")
# Output: Date: 2024-June-15, Temperature: 75.5°F

# Real-time example: Using tuples in real-time web automation testing

def fetch_product_details():
    # Simulating fetching product details from a web page
    return ("Laptop", "Electronics", 999.99, 10)
product_name, category, price, stock = fetch_product_details()
print(f"Product: {product_name}, Category: {category}, Price: ${price}, Stock: {stock}")
# Output: Product: Laptop, Category: Electronics, Price: $999.99, Stock: 10
# Real-time example: Using tuples in real-time financial calculations
def get_transaction():
    # Simulating fetching a financial transaction
    return ("TXN12345", "2024-06-01", 250.75, "Completed")
transaction_id, date, amount, status = get_transaction()
print(f"Transaction ID: {transaction_id}, Date: {date}, Amount: ${amount}, Status: {status}")
# Output: Transaction ID: TXN12345, Date: 2024-06-01, Amount: $250.75, Status: Completed









