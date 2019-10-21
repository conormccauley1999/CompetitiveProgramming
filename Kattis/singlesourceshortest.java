// Fails: Time Limit Exceeded

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
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
			int q = r.ni();
			int s = r.ni();
			if ((n | m | q | s) == 0) break;

			int[][] g = new int[n][n];
			for (int i = 0; i < n; i++)
				for (int j = 0; j < n; j++)
					g[i][j] = Integer.MAX_VALUE;

			for (int i = 0; i < m; i++) {
				int u = r.ni();
				int v = r.ni();
				int w = r.ni();
				g[u][v] = w;
			}

			int[] dist = dijk(g, n, s);

			for (int i = 0; i < q; i++) {
				int d = r.ni();
				System.out.println(dist[d] == Integer.MAX_VALUE ? "Impossible" : dist[d]);
			}

			System.out.println();

		}

	}

	static int[] dijk(int[][] g, int n, int s) {

		int[] d = new int[n];
		d[s] = 0;

		PriorityQueue<Pair> q = new PriorityQueue<Pair>();

		for (int i = 0; i < n; i++) {
			if (i != s) d[i] = Integer.MAX_VALUE;
			q.add(new Pair(i, d[i]));
		}

		while (!q.isEmpty()) {
			int v = q.poll().v;
			for (int u = 0; u < n; u++) {
				if (d[v] == Integer.MAX_VALUE || g[v][u] == Integer.MAX_VALUE) continue;
				int a = d[v] + g[v][u];
				if (a < d[u]) {
					q.remove(new Pair(u, d[u]));
					d[u] = a;
					q.add(new Pair(u, a));
				}
			}
		}

		return d;

	}

	static class Pair implements Comparable<Pair> {

		public int v, d;

		public Pair(int v, int d) {
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
