using System;

class PE115 {

	private static long[] cache;

	public static void Main(string[] args) {
		
		int m = 50;
		int n = m;
		
		while (true) {

			cache = new long[n];
			for (int i = 0; i < n; i++) cache[i] = -1;

			long v = Solve(m, n, 0);
			if (v > 1000000) break;

			n++;

		}
		
		Console.WriteLine(n);

	}

	private static long Solve(int m, int n, int i) {
		
		if (i == n) return 1;
		if (cache[i] != -1) return cache[i];

		long r = 0;

		// Grey cell
		r += Solve(m, n, i + 1);

		// Red blocks
		for (int j = m; i + j <= n; j++) {
			int k = i + j;
			r += Solve(m, n, k == n ? k : k + 1); // Add grey cell if there's space
		}
		
		cache[i] = r;
		return r;
		
	}

}
