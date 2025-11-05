# Fibonacci Series: Recursive and Non-Recursive (Iterative)
# With user input and series display

# Recursive function to get nth Fibonacci number
def fib_recursive(n):
    if n <= 1:
        return n
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


# Recursive series generator
def fib_series_recursive(n):
    series = []
    for i in range(n):
        series.append(fib_recursive(i))
    return series


# Non-recursive (iterative) function to get nth Fibonacci number
def fib_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# Iterative series generator
def fib_series_iterative(n):
    series = []
    a, b = 0, 1
    for i in range(n):
        series.append(a)
        a, b = b, a + b
    return series


# ---- Main Program ----
n = int(input("Enter the number of elements: "))

# Recursive output
print("\nUsing Recursive Method:")
print("Fibonacci Series:", fib_series_recursive(n))
print(f"Fibonacci({n}) =", fib_recursive(n - 1))

# Iterative output
print("\nUsing Non-Recursive (Iterative) Method:")
print("Fibonacci Series:", fib_series_iterative(n))
print(f"Fibonacci({n}) =", fib_iterative(n - 1))

# ---- Time and Space Complexity ----
print("\n--- Complexity Analysis ---")
print("Recursive Approach:")
print("  • Time Complexity  : O(2^n)")
print("  • Space Complexity : O(n) (recursion stack)")

print("Iterative Approach:")
print("  • Time Complexity  : O(n)")
print("  • Space Complexity : O(1)")
