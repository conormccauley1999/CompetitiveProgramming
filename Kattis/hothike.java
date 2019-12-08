import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
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
		int[] t = new int[n];
		for (int i = 0; i < n; i++)
			t[i] = r.ni();

		int m = Integer.MAX_VALUE;
		int mi = 0;
		for (int i = 0; i < n - 2; i++) {
			int x = Math.max(t[i], t[i + 2]);
			if (x < m) {
				m = x;
				mi = i + 1;
			}
		}

		System.out.println(mi + " " + m);

	}

}
