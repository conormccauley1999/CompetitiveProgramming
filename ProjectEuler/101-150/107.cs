using System;
using System.IO;

class PE107 {

	private const int SIZE = 40;
	private const int INF = int.MaxValue;

	private static int[] parent = new int[SIZE];

	public static void Main(string[] args) {

		int[,] matrix = new int[SIZE, SIZE];

		var lines = File.ReadAllLines("../files/107.txt");
		
		for (int i = 0; i < SIZE; i++) {
			var vals = lines[i].Split(',');
			for (int j = 0; j < SIZE; j++) {
				matrix[i, j] = (vals[j] == "-") ? INF : int.Parse(vals[j]);
			}
		}

		int w1 = Weight(matrix);
		int w2 = Kruskal(matrix);

		Console.WriteLine(w1 - w2);

	}

	private static int Weight(int[,] matrix) {

		int result = 0;

		for (int i = 0; i < SIZE; i++) {
			for (int j = i; j < SIZE; j++) {
				result += (matrix[i, j] == INF) ? 0 : matrix[i, j];
			}
		}

		return result;
	}

	private static int Kruskal(int[,] matrix) {

		int result = 0;

		for (int i = 0; i < SIZE; i++)
			parent[i] = i;
		
		int edgeCount = 0;
		while (edgeCount < (SIZE - 1)) {

			int min = INF, a = -1, b = -1;

			for (int i = 0; i < SIZE; i++) {
				for (int j = 0; j < SIZE; j++) {
					if (find(i) != find(j) && matrix[i, j] < min) {
						min = matrix[i, j];
						a = i;
						b = j;
					}
				}
			}

			union(a, b);
			edgeCount++;
			result += min;

		}

		return result;

	}

	private static void union(int i, int j) {
		int a = find(i);
		int b = find(j);
		parent[a] = b;
	}

	private static int find(int i) {
		while (parent[i] != i) {
			i = parent[i];
		}
		return i;
	}

}
