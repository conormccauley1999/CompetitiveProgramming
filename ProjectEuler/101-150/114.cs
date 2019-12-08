// Problem 114

using System;

class PE114 {

	private const int ROW_LEN = 50;
	private const int MIN_BLOCK_LEN = 3;

	private static long[] cache;

	public static void Main(string[] args) {
		cache = new long[ROW_LEN];
		for (int i = 0; i < ROW_LEN; i++) cache[i] = -1;
		Console.WriteLine(Solve(0));
	}

	private static long Solve(int i) {
		
		if (i == ROW_LEN) return 1;
		if (cache[i] != -1) return cache[i];

		long r = 0;

		// Grey cell
		r += Solve(i + 1);

		// Red blocks
		for (int j = MIN_BLOCK_LEN; i + j <= ROW_LEN; j++) {
			int k = i + j;
			r += Solve(k == ROW_LEN ? k : k + 1); // Add grey cell if there's space
		}
		
		cache[i] = r;
		return r;
		
	}

}
