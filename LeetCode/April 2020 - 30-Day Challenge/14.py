def sl(s, d):
    d %= len(s)
    if d == 0:
        return s
    return s[d:] + s[:d]

def sr(s, d):
    d %= len(s)
    if d == 0:
        return s
    return s[-d:] + s[:len(s)-d]

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        for op in shift:
            s = sl(s, op[1]) if op[0] == 0 else sr(s, op[1])
        return s
