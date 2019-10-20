import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.Math;
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

		int n = r.ni();
		Point[] ps = new Point[n];

		for (int i = 0; i < n; i++)
			ps[i] = new Point(r.nd(), r.nd());

		int[] t = naive(n, ps);
		for (int i = 0; i < n; i++)
			System.out.println(t[i]);

	}

	static int[] naive(int n, Point[] ps) {

		int[] t = new int[n];
		boolean[] u = new boolean[n];
		t[0] = 0;
		u[0] = true;

		for (int i = 1; i < n; i++) {

			int b = -1;

			for (int j = 0; j < n; j++) {
				if (!u[j] && (b == -1 || (ps[t[i-1]].dist(ps[j]) < ps[t[i-1]].dist(ps[b]))))
					b = j;
			}

			t[i] = b;
			u[b] = true;
			
		}

		return t;

	}

	static class Point {
		double x, y;
		public Point(double x, double y) {
			this.x = x;
			this.y = y;
		}
		double dist(Point p) {
			return Math.sqrt(Math.pow(x - p.x, 2) + Math.pow(y - p.y, 2));
		}
	}

}
