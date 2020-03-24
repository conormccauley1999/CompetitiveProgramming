def R(n):
    ts = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    os = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    return ts[n // 10] + os[n % 10]

ns, rs = {}, {}
for n in range(1, 100):
    r = R(n)
    ns[r], rs[n] = n, R(n)

r = input()
s = sorted(r)
v = ns[r]
for m in range(1, n):
    if s == sorted(rs[m]):
        v = rs[m]
        break
print(v)

