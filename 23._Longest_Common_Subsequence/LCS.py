def lcs(X, Y):
    m = len(X)
    n = len(Y)
    
    # Create a 2D array to store the length of the LCS
    dp = [[None]*(n+1) for _ in range(m+1)]

    # Build the dp array from the bottom up
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # Reconstruct the LCS from the dp array
    index = dp[m][n]
    lcs_str = [""] * (index + 1)
    lcs_str[index] = ""

    i = m
    j = n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            lcs_str[index-1] = X[i-1]
            i -= 1
            j -= 1
            index -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return "".join(lcs_str)

# Get the first sequence from the user
X = input("Enter the first sequence: ")

# Get the second sequence from the user
Y = input("Enter the second sequence: ")

# Perform LCS algorithm
lcs_result = lcs(X, Y)

# Print the LCS
print("The Longest Common Subsequence is:", lcs_result)
