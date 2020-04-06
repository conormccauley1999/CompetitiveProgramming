class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for s in strs:
            ss = tuple(sorted(s))
            if ss not in ans:
                ans[ss] = []
            ans[ss].append(s)
        r = []
        for k in ans:
            r.append(ans[k])
        return r
