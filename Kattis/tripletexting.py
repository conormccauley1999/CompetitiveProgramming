s = input()
l = len(s) // 3
s1, s2, s3 = s[:l], s[l:l*2], s[l*2:]
r = ''
for i in range(l):
    x = (s1[i], s2[i], s3[i])
    r += max(set(x), key=x.count)
print(r)
