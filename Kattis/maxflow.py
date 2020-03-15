from collections import defaultdict

def bfs(s, t, p, n, G):
	v = [False] * n
	q = []
	q.append(s)
	v[s] = True
	while q:
		u = q.pop()
		for i, x in enumerate(G[u]):
			if not v[i] and x > 0:
				q.append(i)
				v[i] = True
				p[i] = u
	return v[t]

n, m, s, t = map(int, input().split())
G = []
for _ in range(n):
	G.append([0] * n)
for _ in range(m):
	u, v, c = map(int, input().split())
	G[u][v] = c

p = [-1] * n
mx = 0
while bfs(s, t, p, n, G):
	f = float("Inf")
	x = t
	while x != s:
		f = min(f, G[p[x]][x])
		x = p[x]
	mx += f
	v = t
	while v != s:
		u = p[v]
		G[u][v] -= f
		G[v][u] += f
		v = p[v]
print(G)
