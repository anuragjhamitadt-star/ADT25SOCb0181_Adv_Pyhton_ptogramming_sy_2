
def fibonacci_memo(n, dp):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    if dp[n] != -1:
        return dp[n]

    dp[n] = fibonacci_memo(n - 1, dp) + fibonacci_memo(n - 2, dp)
    return dp[n]




def fibonacci_iterative(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1

    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c

    return b


n = int(input("Enter the value of n: "))

dp = [-1] * (n + 1)

print("Fibonacci using Memoization:", fibonacci_memo(n, dp))
print("Fibonacci using Tabulation:", fibonacci_iterative(n))