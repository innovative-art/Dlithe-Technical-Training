def max_stolen_value(val):
    n = len(val)
    if n == 0:
        return 0
    if n == 1:
        return val[0]
    
    dp = [0] * n
    dp[0] = val[0]
    dp[1] = max(val[0], val[1])

    for i in range(2, n):
        dp[i] = max(val[i] + dp[i-2], dp[i-1])

    return dp[-1]

# Taking user input
val = list(map(int, input("Enter house values separated by space: ").split()))
print("Maximum stolen value:", max_stolen_value(val))
