# Problem 81

with open("../files/81.txt") as f:
    rawM = f.readlines()
rawM = [x.strip() for x in rawM]

M = []

for row in rawM:
    M.append(row.split(","))

S = len(M)

for i in range(0, S):
    for j in range(0, S):
        M[i][j] = int(M[i][j])

for i in range(0, S):
    for j in range(0, S):
        if i > 0 and j > 0:
            M[i][j] += M[i - 1][j] if M[i - 1][j] < M[i][j - 1] else M[i][j - 1]
        elif i == 0 and j > 0:
            M[i][j] += M[i][j - 1]
        elif i > 0 and j == 0:
            M[i][j] += M[i - 1][j]

print M[S - 1][S - 1]
