def solve(t):
	ss = t.replace("a", "")
	if ss == "": return t
	s = t[:-len(ss)/2]
	if s.replace("a", "") != ss[len(ss)/2:]: return ":("
	else: return s

print solve(raw_input())