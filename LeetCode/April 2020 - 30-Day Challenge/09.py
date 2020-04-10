class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        a, b = [], []
        s, t = list(S), list(T)
        for i in range(len(s)):
            if s[i] == '#':
                if len(a): a.pop()
            else: a.append(s[i])
        for i in range(len(t)):
            if t[i] == '#':
                if len(b): b.pop()
            else: b.append(t[i])
        return ''.join(a) == ''.join(b)
