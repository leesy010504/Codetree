N = int(input())

dp = [-1] * (N + 1)

def fibbo(N):
    if N <= 0:
        return 0
    
    if N <= 2:
        return 1

    if dp[N] != -1:
        return dp[N]

    else:
        dp[N] = fibbo(N - 1) + fibbo(N - 2)
    
    return dp[N]

print(fibbo(N))