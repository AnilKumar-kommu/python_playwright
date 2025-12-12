# break and continue statements in loops in Python
for i in range(10):
    if i == 5:
        print("Breaking the loop at i =", i)
        break  # Exit the loop when i is 5
    if i % 2 == 0:
        print("Continuing at even i =", i)
        continue  # Skip the rest of the loop for even numbers
    print("Current value of i:", i)
# Output:
# Continuing at even i = 0
# Current value of i: 1
# Continuing at even i = 2
# Current value of i: 3
# Continuing at even i = 4
# Breaking the loop at i = 5

# In this example:
# - The loop iterates over numbers from 0 to 9.
# - When `i` is even, the `continue` statement skips the rest of the loop body, so only odd values are printed.
# - When `i` reaches 5, the `break` statement exits the loop entirely.



