D = {}
while True:
    try:
        e, f = input().split()
        D[f] = e
    except:
        break
while True:
    try:
        i = input()
        print('eh' if i not in D else D[i])
    except:
        break
