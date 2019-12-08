n = int(raw_input())
k = map(int, raw_input().split())
print -sum(x for x in k if x < 0)
