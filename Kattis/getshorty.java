// Fails: Time Limit Exceeded

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.StringTokenizer;

class Solution {

	static class Reader {

		BufferedReader br;
		StringTokenizer st;

		public Reader() {
			br = new BufferedReader(new InputStreamReader(System.in));
		}

		String next() {
			while (st == null || !st.hasMoreElements()) {
				try { st = new StringTokenizer(br.readLine()); }
				catch (IOException e) { e.printStackTrace(); }
			}
			return st.nextToken();
		}

		int ni() { return Integer.parseInt(next()); }
		long nl() { return Long.parseLong(next()); }
		double nd() { return Double.parseDouble(next()); }
		
		String n() {
			String str = "";
			try { str = br.readLine(); }
			catch (IOException e) { e.printStackTrace(); }
			return str;
		}

	}

	public static void main(String[] args) {

		Reader r = new Reader();

		while (true) {

			int n = r.ni();
			int m = r.ni();
			if ((n | m) == 0) break;

			double[][] g = new double[n][n];
			for (int i = 0; i < n; i++)
				for (int j = 0; j < n; j++)
					g[i][j] = Double.MIN_VALUE;

			for (int i = 0; i < m; i++) {
				int u = r.ni();
				int v = r.ni();
				double w = r.nd();
				g[u][v] = w;
				g[v][u] = w;
			}

			double d = dijk(g, n);
			if (d == 1.0) System.out.println("1.0000");
			else System.out.println(String.format("%.4g", d));

		}

	}

	static double dijk(double[][] g, int n) {
		
		int s = 0;

		double[] d = new double[n];
		d[s] = 1.0;

		PriorityQueue<Pair> q = new PriorityQueue<Pair>(Collections.reverseOrder());

		for (int i = 0; i < n; i++) {
			if (i != s) d[i] = Double.MIN_VALUE;
			q.add(new Pair(i, d[i]));
		}

		while (!q.isEmpty()) {
			int v = q.poll().v;
			for (int u = 0; u < n; u++) {
				if (d[v] == Double.MIN_VALUE || g[v][u] == Double.MIN_VALUE) continue;
				double a = d[v] * g[v][u];
				if (a > d[u]) {
					q.remove(new Pair(u, d[u]));
					d[u] = a;
					q.add(new Pair(u, a));
				}
			}
		}

		return d[n - 1];

	}

	static class Pair implements Comparable<Pair> {

		public int v;
		public double d;

		public Pair(int v, double d) {
			this.v = v;
			this.d = d;
		}

		@Override
		public int compareTo(Pair p) {
			if (d > p.d) return 1;
			if (d < p.d) return -1;
			return 0;
		}

	}

}
