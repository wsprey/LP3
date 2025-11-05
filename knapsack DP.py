def knapsack_dp(weights, values, capacity):
    n = len(weights)
    # Create a DP table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Fill the table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]

# User input
n = int(input("Enter the number of items: "))
weights = []
values = []

for i in range(n):
    weight = int(input(f"Enter weight of item {i+1}: "))
    value = int(input(f"Enter value of item {i+1}: "))
    weights.append(weight)
    values.append(value)

capacity = int(input("Enter the knapsack capacity: "))

print("Maximum value:", knapsack_dp(weights, values, capacity))
