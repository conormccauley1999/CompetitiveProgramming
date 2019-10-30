alph = "abcdefghijklmnopqrstuvwxyz"

def getKey(snippet, cipher):
	l = len(snippet)
	key = ""
	for i in range(l):
		si = alph.index(snippet[i])
		ci = alph.index(cipher[i])
		key += alph[((ci + 26) - si) % 26]
	return key

n, m = map(int, raw_input().split())
snippet = raw_input()
cipher = raw_input()
lciph = len(cipher)
plain = snippet[::-1]
lplain = n

while lplain < lciph:
	key = getKey(snippet, cipher[-n:])
	plain += key[::-1]
	cipher = cipher[:-n]
	lplain += n
	snippet = key

print plain[:m][::-1]
