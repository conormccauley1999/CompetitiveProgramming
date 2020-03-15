INF = 10 ** 10
S = int(input())
T = 0
dp = [0] + ([INF] * 2016)
for _ in range(S):
	D, C, F, U = map(int, input().split())
	T += D
	M = ((C + F + U) // 2) + 1
	V = max(M - C, 0)
	if V > U: continue
	i = T
	while i >= D:
		dp[i] = min(dp[i], dp[i - D] + V)
		i -= 1
N = (T // 2) + 1
R = INF
for i in range(N, T + 1):
	R = min(R, dp[i])
print("impossible" if R == INF else R)
