# Top-Down Approach
def top_down(weights, values, n, capacity, dp):
    if n == 0 or capacity == 0:
        return 0

    if dp[n][capacity] != -1:
        return dp[n][capacity]

    if weights[n - 1] > capacity:
        dp[n][capacity] = top_down(weights, values, n - 1, capacity, dp)
    else:
        include = values[n - 1] + top_down(
            weights, values, n - 1,
            capacity - weights[n - 1], dp
        )
        exclude = top_down(weights, values, n - 1, capacity, dp)

        dp[n][capacity] = max(include, exclude)

    return dp[n][capacity]


# Bottom-Up Approach
def bottom_up(weights, values, n, capacity):
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):

            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Main Program
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7

n = len(weights)

# Top-Down
dp = [[-1] * (capacity + 1) for _ in range(n + 1)]
answer1 = top_down(weights, values, n, capacity, dp)

# Bottom-Up
answer2 = bottom_up(weights, values, n, capacity)

print("Maximum value using Top-Down:", answer1)
print("Maximum value using Bottom-Up:", answer2)