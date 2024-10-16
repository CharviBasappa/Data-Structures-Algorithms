def coin_change(coins, m, V):
    dp = [float('inf')] * (V + 1)
    dp[0] = 0

    for i in range(1, V + 1):
        for j in range(m):
            if coins[j] <= i:
                sub_res = dp[i - coins[j]]
                if sub_res != float('inf') and sub_res + 1 < dp[i]:
                    dp[i] = sub_res + 1

    return dp[V]

# Example usage
coins = [1, 2, 3]
m = len(coins)
V = 5
print("Minimum coins required:", coin_change(coins, m, V))
