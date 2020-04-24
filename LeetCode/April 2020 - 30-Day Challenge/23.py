class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        a = bin(m)[2:].zfill(32)
        b = bin(n)[2:].zfill(32)
        p = ''
        for i in range(32):
            if a[i] != b[i]:
                break
            p += a[i]
        r = 32 - len(p)
        return int(p + ('0' * r), 2)
