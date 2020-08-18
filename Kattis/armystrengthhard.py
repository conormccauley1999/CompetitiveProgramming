t = int(input())
for _ in range(t):
    input()
    ng, nm = map(int, input().split())
    vg = max(map(int, input().split()))
    vm = max(map(int, input().split()))
    if vm > vg:
        print("MechaGodzilla")
    else:
        print("Godzilla")
