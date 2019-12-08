import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
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

		ArrayList<Point> ps = new ArrayList<Point>();

		for (int i = 0; i < 8; i++) {
			String s = r.n();
			for (int j = 0; j < 8; j++) {
				if (s.charAt(j) == '*') ps.add(new Point(j, i));
			}
		}

		System.out.println(solve(ps) ? "valid" : "invalid");

	}

	static boolean solve(ArrayList<Point> ps) {

		if (ps.size() != 8) return false;

		for (int i = 0; i < 8; i++) {
			Point p = ps.get(i);
			for (int j = i + 1; j < 8; j++) {
				Point q = ps.get(j);
				if (p.x == q.x || p.y == q.y) return false;
				int dx = Math.abs(p.x - q.x);
				int dy = Math.abs(p.y - q.y);
				if (dy % dx == 0 && dy / dx == 1) return false;
			}
		}

		return true;

	}

	static class Point {
		int x, y;
		public Point(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}

}
