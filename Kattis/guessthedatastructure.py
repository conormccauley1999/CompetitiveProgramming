from collections import deque
import heapq as pq

def f(n):
    s, q, p = [], deque([]), []
    pos = [True, True, True]
    for _ in range(n):
        x, y = map(int, input().split())
        if x == 1:
            s.append(y)
            q.append(y)
            pq.heappush(p, -y)
        else:
            if len(s) == 0:
                pos[0] = False
            else:
                vs = s.pop()
                if vs != y:
                    pos[0] = False
            if len(q) == 0:
                pos[1] = False
            else:
                vq = q.popleft()
                if vq != y:
                    pos[1] = False
            if len(p) == 0:
                pos[2] = False
            else:
                vp = -pq.heappop(p)
                if vp != y:
                    pos[2] = False
    c = pos.count(True)
    if c == 0:
        print("impossible")
    elif c > 1:
        print("not sure")
    else:
        if pos[0]:
            print("stack")
        elif pos[1]:
            print("queue")
        else:
            print("priority queue")

while True:
    try:
        n = int(input())
    except:
        break
    f(n)
