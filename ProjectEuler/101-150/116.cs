// Problem 116

using System;

class PE116 {

	private static long[] cache;

	public static void Main(string[] args) {

		int n = 50;
		long r = 0;

		foreach (int m in new int[3] {2, 3, 4}) {
			cache = new long[n];
			for (int i = 0; i < n; i++) cache[i] = -1;
			r += Solve(n, m, 0);
		}
		
		Console.WriteLine(r - 3);
	}

	private static long Solve(int n, int m, int i) {
		
		if (i == n) return 1;
		if (cache[i] != -1) return cache[i];

		long r = 0;

		// Grey cell
		r += Solve(n, m, i + 1);
		
		// Coloured tile
		if (i + m <= n) r += Solve(n, m, i + m);

		cache[i] = r;
		return r;
		
	}

}
