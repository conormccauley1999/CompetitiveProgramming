while True:
    try:
        n = int(input())
        print(1 if n == 1 else 2*n - 2)
    except:
        break
