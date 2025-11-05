# Fibonacci Series: Recursive and Non-Recursive (Iterative)
# With user input and series display

# Recursive function to get nth Fibonacci number
def fib_recursive(n):
    if n <= 1:
        return n
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)

# Non-recursive (iterative) function to get nth Fibonacci number
def fib_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# ---- Main Program ----
n = int(input("Enter the number of elements: "))

# Recursive Fibonacci series
recursive_series = [fib_recursive(i) for i in range(n)]
print("\nUsing Recursive Method:")
print("Fibonacci Series:", recursive_series)
print(f"Fibonacci({n}) =", fib_recursive(n - 1))

# Iterative Fibonacci series
iterative_series = []
a, b = 0, 1
for i in range(n):
    iterative_series.append(a)
    a, b = b, a + b

print("\nUsing Non-Recursive (Iterative) Method:")
print("Fibonacci Series:", iterative_series)
print(f"Fibonacci({n}) =", fib_iterative(n - 1))

# ---- Time and Space Complexity ----
print("\n--- Complexity Analysis ---")
print("Recursive Approach:")
print("  • Time Complexity  : O(2^n)")
print("  • Space Complexity : O(n) (recursion stack)")

print("Iterative Approach:")
print("  • Time Complexity  : O(n)")
print("  • Space Complexity : O(1)")
