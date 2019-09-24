using System;

class PE093 {

	public static void Main(string[] args) {

		int max = 0;
		int str = 0;
		
		for (int a = 1; a <= 9; a++) {
			for (int b = a + 1; b <= 9; b++) {
				for (int c = b + 1; c <= 9; c++) {
					for (int d = c + 1; d <= 9; d++) {
						int result = Solve(new int[4] {a, b, c, d});
						if (result > max) {
							max = result;
							str = (a * 1000) + (b * 100) + (c * 10) + d;
						}
					}
				}
			}
		}

		Console.WriteLine(max);
		Console.WriteLine(str);

	}

	private static int Solve(int[] digits) {

		bool[] found = new bool[3024];
		int[][] orderings = GetOrderings(digits);

		for (int op1 = 0; op1 < 4; op1++) {
			for (int op2 = 0; op2 < 4; op2++) {
				for (int op3 = 0; op3 < 4; op3++) {
					foreach (int[] ordering in orderings) {
						SolveForOrdering(op1, op2, op3, ordering, found);
					}
				}
			}
		}

		for (int i = 0; i < found.Length; i++) {
			if (!found[i]) return i;
		}

		return found.Length;

	}

	private static int[][] GetOrderings(int[] digits) {

		return new int[24][] {

			new int[4] { digits[0], digits[1], digits[2], digits[3] },
			new int[4] { digits[0], digits[1], digits[3], digits[2] },
			new int[4] { digits[0], digits[2], digits[1], digits[3] },
			new int[4] { digits[0], digits[2], digits[3], digits[1] },
			new int[4] { digits[0], digits[3], digits[1], digits[2] },
			new int[4] { digits[0], digits[3], digits[2], digits[1] },

			new int[4] { digits[1], digits[0], digits[2], digits[3] },
			new int[4] { digits[1], digits[0], digits[3], digits[2] },
			new int[4] { digits[1], digits[2], digits[0], digits[3] },
			new int[4] { digits[1], digits[2], digits[3], digits[0] },
			new int[4] { digits[1], digits[3], digits[0], digits[2] },
			new int[4] { digits[1], digits[3], digits[2], digits[0] },

			new int[4] { digits[2], digits[0], digits[1], digits[3] },
			new int[4] { digits[2], digits[0], digits[3], digits[1] },
			new int[4] { digits[2], digits[1], digits[0], digits[3] },
			new int[4] { digits[2], digits[1], digits[3], digits[0] },
			new int[4] { digits[2], digits[3], digits[0], digits[1] },
			new int[4] { digits[2], digits[3], digits[1], digits[0] },

			new int[4] { digits[3], digits[0], digits[1], digits[2] },
			new int[4] { digits[3], digits[0], digits[2], digits[1] },
			new int[4] { digits[3], digits[1], digits[0], digits[2] },
			new int[4] { digits[3], digits[1], digits[2], digits[0] },
			new int[4] { digits[3], digits[2], digits[0], digits[1] },
			new int[4] { digits[3], digits[2], digits[1], digits[0] }

		};

	}

	private static void SolveForOrdering(int op1, int op2, int op3, int[] digits, bool[] found) {

		double result = (double) digits[0];
		result = EvalOp(op1, result, (double) digits[1]);
		result = EvalOp(op2, result, (double) digits[2]);
		result = EvalOp(op3, result, (double) digits[3]);

		if (result > 0 && result % 1 == 0)
			found[Convert.ToInt32(result) - 1] = true;

		double resultA = EvalOp(op1, (double) digits[0], (double) digits[1]);double resultB = EvalOp(op3, (double) digits[2], (double) digits[3]);
		result = EvalOp(op2, resultA, resultB);
		
		if (result > 0 && result % 1 == 0)
			found[Convert.ToInt32(result) - 1] = true;
				
	}

	private static double EvalOp(int op, double x, double y) {
		if (op == 0) return x + y;
		if (op == 1) return x - y;
		if (op == 2) return x * y;
		if (op == 3) return x / y;
		return x + y;
	}

}
