// Problem 94

using System;

class PE094 {

	private const long MAX_PERIMETER = 1000000000;

	public static void Main(string[] args) {

		long result = 0;
		long maxSmallSide = (MAX_PERIMETER - 1) / 3;
		
		for (long smallSide = 3; smallSide <= maxSmallSide; smallSide += 2) {
			if (IsAET(smallSide, smallSide + 1))
				result += (3 * smallSide) + 1;
			if (IsAET(smallSide, smallSide - 1))
				result += (3 * smallSide) - 1;
		}
		
		Console.WriteLine(result);

	}

	private static bool IsAET(long a, long b) {

		long a2 = a * a;
		long b2 = b * b;
		
		return (b2 % 4 == 0) && IsSquare((4 * a2) - b2);

	}

	
	private static bool IsSquare(long n) {
		if (n == 0) return false;
		long root = (long) Math.Round(Math.Sqrt(n));
		return (root * root) == n;
	}

}
