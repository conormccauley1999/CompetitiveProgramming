# Please try to ignore how awful this code is

from math import sqrt, floor, ceil

def isAnagram(a, b):
	return "".join(sorted(a)) == "".join(sorted(b))


def getAnagramPairs(words):
	anagramPairs = set()
	for i in range(0, len(words)):
		for j in range(i + 1, len(words)):
			if (isAnagram(words[i], words[j])):
				anagramPairs.add((words[i], words[j]))
	return anagramPairs


def fingerprint(x):
	r = 0
	while x > 0:
		r += 10 ** (x % 10)
		x /= 10
	return r


def fastNumberAnagram(a, b):
	return fingerprint(a) == fingerprint(b)

_numAnagramPairsOfLen = {}
def getNumberAnagramPairs(n):
	if n in _numAnagramPairsOfLen: return _numAnagramPairsOfLen[n]
	squares = getSquaresOfLen(n)
	anagramPairs = set()
	for i in range(0, len(squares)):
		if n == 9:
			I_a = (squares[i] // (10 ** 8))
			N_a = (squares[i] // (10 ** 7)) % 10
			T_a = (squares[i] // (10 ** 6)) % 10
			R_a = (squares[i] // (10 ** 5)) % 10
		for j in range(i + 1, len(squares)):
			if n == 9:
				if squares[j] % 10 != N_a: continue
				if (squares[j] // 100) % 10 != I_a: continue
				if (squares[j] // 1000) % 10 != T_a: continue
				if squares[j] // (10 ** 8) != R_a: continue
			if (fastNumberAnagram(squares[i], squares[j])):
				anagramPairs.add((squares[i], squares[j]))
	_numAnagramPairsOfLen[n] = anagramPairs
	return anagramPairs


_squaresOfLen = {}
def getSquaresOfLen(n):
	if n in _squaresOfLen: return _squaresOfLen[n]
	squares = []
	start, end = int(ceil(sqrt(10 ** (n - 1)))), int(floor(sqrt(10 ** n)))
	for i in range(start, end + 1):
		squares.append(i * i)
	_squaresOfLen[n] = squares
	return squares


def pairsMap(wordPair, numberPair):
	strNumA, strNumB = str(numberPair[0]), str(numberPair[1])
	mapA, mapB = {}, {}
	numsUsed = set()
	for i in range(0, len(wordPair[0])):
		if strNumA[i] in numsUsed:
			return False
		numsUsed.add(strNumA[i])
		if wordPair[0][i] in mapA: return False
		mapA[wordPair[0][i]] = strNumA[i]
		if wordPair[1][i] in mapB: return False
		mapB[wordPair[1][i]] = strNumB[i]
	if len(numsUsed) != len(strNumA): return False
	return mapA == mapB


def getMaxSquare(wordPair):
	numberPairs = getNumberAnagramPairs(len(wordPair[0]))
	maxSquare = 0
	for numberPair in numberPairs:
		if pairsMap(wordPair, numberPair):
			maxNum = max(numberPair)
			maxSquare = maxNum if maxNum > maxSquare else maxSquare
	return maxSquare


def main():
	words = open("../files/98.txt", "r").read().replace("\"", "").split(",")
	anagramPairs = getAnagramPairs(words)
	return max([getMaxSquare(anagramPair) for anagramPair in anagramPairs])


print main()
