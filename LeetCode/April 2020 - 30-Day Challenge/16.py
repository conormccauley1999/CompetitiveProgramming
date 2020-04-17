class Solution:
    def checkValidString(self, s: str) -> bool:
        mn, mx = 0, 0
        for c in s:
            if c == '(':
                mn += 1
                mx += 1
            elif c == ')':
                mn -= 1
                mx -= 1
            else:
                mn -= 1
                mx += 1
            if mx < 0: break
            mn = max(mn, 0)
        return mn == 0
