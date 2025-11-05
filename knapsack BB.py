def knapsack_bb(i, profit, weight, capacity, items, n, maxProfit):
    if weight > capacity:
        return maxProfit
    if i == n:
        return max(maxProfit, profit)

    # Calculate optimistic bound
    totweight = weight
    bound = profit
    for j in range(i, n):
        if totweight + items[j][1] <= capacity:
            totweight += items[j][1]
            bound += items[j][0]
        else:
            bound += (capacity - totweight) * items[j][0] / items[j][1]
            break
    if bound <= maxProfit:
        return maxProfit

    # Branch: take or skip current item
    maxProfit = knapsack_bb(i+1, profit + items[i][0], weight + items[i][1], capacity, items, n, maxProfit)
    maxProfit = knapsack_bb(i+1, profit, weight, capacity, items, n, maxProfit)
    return maxProfit

# User input
n = int(input("Enter number of items: "))
values = [int(input(f"Value of item {i+1}: ")) for i in range(n)]
weights = [int(input(f"Weight of item {i+1}: ")) for i in range(n)]
capacity = int(input("Enter knapsack capacity: "))

# Sort items by value/weight ratio
items = sorted(zip(values, weights), key=lambda x: x[0]/x[1], reverse=True)

print("Maximum value:", knapsack_bb(0, 0, 0, capacity, items, n, 0))
