# Problem 584

"""

E(n, k, d)
- (1) E(3, 1, 10)  = 5.78688636
- (2) E(3, 7, 100) = 8.48967364

(1) Generate all distinct (k + 1) day sequences s. t. the sum of values in each sequence is less than n.
(2) Generate the transition matrix for all sequences to every other sequence.

"""


def gen_seqs(n, k):
	global seq_index, index_seq, seq_trans
	seqs = [set() for _ in range(n)]
	base = tuple([0] * (k + 1))
	seqs[0].add(base)
	i = 0
	seq_index[i] = base
	index_seq[base] = i
	for count in range(1, n):
		for seq in seqs[count - 1]:
			seq_trans[index_seq[seq]] = set()
			for day in range(0, k + 1):
				new = list(seq)
				new[day] += 1
				tuple_new = tuple(new)
				if tuple_new not in seqs[count]:
					i += 1
					seq_index[i] = tuple_new
					index_seq[tuple_new] = i
				seq_trans[index_seq[seq]].add(index_seq[tuple_new])
				seqs[count].add(tuple_new)
	return i + 1


n, k, d = 3, 1, 10
#mx = (n - 1) * (d // (k + 1))

seq_index, index_seq, seq_trans = {}, {}, {}
seq_count = gen_seqs(n, k)

trans_mat = [[0] * seq_count for _ in range(seq_count)]
trans_prob = 1.0 / (k + 1)
for start in seq_trans:
	for end in seq_trans[start]:
		trans_mat[start][end] = trans_prob
 