using System;

class PE117 {

	private static long[] cache;

	public static void Main(string[] args) {

		int n = 50;
		cache = new long[n];
		for (int i = 0; i < n; i++) cache[i] = -1;
		long r = Solve(n, 0);
		Console.WriteLine(r);
	}

	private static long Solve(int n, int i) {
		
		if (i == n) return 1;
		if (cache[i] != -1) return cache[i];

		long r = 0;

		// Grey cell
		r += Solve(n, i + 1);
		
		// Coloured tiles
		if (i + 2 <= n) r += Solve(n, i + 2);
		if (i + 3 <= n) r += Solve(n, i + 3);
		if (i + 4 <= n) r += Solve(n, i + 4);

		cache[i] = r;
		return r;
		
	}

}
