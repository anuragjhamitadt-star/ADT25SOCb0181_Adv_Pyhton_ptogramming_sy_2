def longest_common_subsequence(X, Y):
    m = len(X)
    n = len(Y)


    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]


    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])


    i = m
    j = n
    lcs = []

    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    lcs.reverse()

    return "".join(lcs), dp[m][n]


seq1 = input("Enter the first sequence: ")
seq2 = input("Enter the second sequence: ")

lcs, length = longest_common_subsequence(seq1, seq2)

print("\nLongest Common Subsequence:", lcs)
print("Length of LCS:", length)