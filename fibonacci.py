def fibonacci_memo(n, memo):
    """Top-Down Approach using Memoization"""
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


def fibonacci_tabulation(n):
    """Bottom-Up Approach using Tabulation"""
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


def main():
    n = int(input("Enter n: "))

    memo = {}
    result_memo = fibonacci_memo(n, memo)
    result_tab = fibonacci_tabulation(n)

    print("Using Memoization:", result_memo)
    print("Using Tabulation:", result_tab)


if __name__ == "__main__":
    main()
