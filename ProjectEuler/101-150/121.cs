// Problem 121

using System;

class PE121 {

	public const long MAX_DEPTH = 15;
	public const long BLUES_NEEDED = 8;

	public static long blueWins = 0;
	public static long totalGames = 0;

	public static void Main (string[] args) {

		PTree(0, 0, 1);
		totalGames = Factorial(MAX_DEPTH + 1);
		Console.WriteLine(totalGames / blueWins);

	}

	private static void PTree(long depth, long blues, long num) {
		
		if (depth < MAX_DEPTH) {
			PTree(depth + 1, blues + 1, num);
			PTree(depth + 1, blues, num * (depth + 1));
		}
		else if (blues >= BLUES_NEEDED) {
			blueWins += num;
		}

	}

	private static long Factorial(long n) {
		long f = n;
		while (--n > 0) { f *= n; }
		return f;
	}

}
