import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
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
		HashMap<Integer, String> h = init();

		int m = r.ni();
		for (int i = 0; i < m; i++) {
			int n = r.ni();
			System.out.println(h.containsKey(n) ? h.get(n) : "no solution");
		}

	}

	static HashMap<Integer, String> init() {

		HashMap<Integer, String> h = new HashMap<Integer, String>();

		int n;
		n = 4 + 4 + 4 + 4; h.putIfAbsent(n, String.format("4 + 4 + 4 + 4 = %d", n));
		n = 4 + 4 + 4 - 4; h.putIfAbsent(n, String.format("4 + 4 + 4 - 4 = %d", n));
		n = 4 + 4 + 4 * 4; h.putIfAbsent(n, String.format("4 + 4 + 4 * 4 = %d", n));
		n = 4 + 4 + 4 / 4; h.putIfAbsent(n, String.format("4 + 4 + 4 / 4 = %d", n));
		n = 4 + 4 - 4 + 4; h.putIfAbsent(n, String.format("4 + 4 - 4 + 4 = %d", n));
		n = 4 + 4 - 4 - 4; h.putIfAbsent(n, String.format("4 + 4 - 4 - 4 = %d", n));
		n = 4 + 4 - 4 * 4; h.putIfAbsent(n, String.format("4 + 4 - 4 * 4 = %d", n));
		n = 4 + 4 - 4 / 4; h.putIfAbsent(n, String.format("4 + 4 - 4 / 4 = %d", n));
		n = 4 + 4 * 4 + 4; h.putIfAbsent(n, String.format("4 + 4 * 4 + 4 = %d", n));
		n = 4 + 4 * 4 - 4; h.putIfAbsent(n, String.format("4 + 4 * 4 - 4 = %d", n));
		n = 4 + 4 * 4 * 4; h.putIfAbsent(n, String.format("4 + 4 * 4 * 4 = %d", n));
		n = 4 + 4 * 4 / 4; h.putIfAbsent(n, String.format("4 + 4 * 4 / 4 = %d", n));
		n = 4 + 4 / 4 + 4; h.putIfAbsent(n, String.format("4 + 4 / 4 + 4 = %d", n));
		n = 4 + 4 / 4 - 4; h.putIfAbsent(n, String.format("4 + 4 / 4 - 4 = %d", n));
		n = 4 + 4 / 4 * 4; h.putIfAbsent(n, String.format("4 + 4 / 4 * 4 = %d", n));
		n = 4 + 4 / 4 / 4; h.putIfAbsent(n, String.format("4 + 4 / 4 / 4 = %d", n));

		n = 4 - 4 + 4 + 4; h.putIfAbsent(n, String.format("4 - 4 + 4 + 4 = %d", n));
		n = 4 - 4 + 4 - 4; h.putIfAbsent(n, String.format("4 - 4 + 4 - 4 = %d", n));
		n = 4 - 4 + 4 * 4; h.putIfAbsent(n, String.format("4 - 4 + 4 * 4 = %d", n));
		n = 4 - 4 + 4 / 4; h.putIfAbsent(n, String.format("4 - 4 + 4 / 4 = %d", n));
		n = 4 - 4 - 4 + 4; h.putIfAbsent(n, String.format("4 - 4 - 4 + 4 = %d", n));
		n = 4 - 4 - 4 - 4; h.putIfAbsent(n, String.format("4 - 4 - 4 - 4 = %d", n));
		n = 4 - 4 - 4 * 4; h.putIfAbsent(n, String.format("4 - 4 - 4 * 4 = %d", n));
		n = 4 - 4 - 4 / 4; h.putIfAbsent(n, String.format("4 - 4 - 4 / 4 = %d", n));
		n = 4 - 4 * 4 + 4; h.putIfAbsent(n, String.format("4 - 4 * 4 + 4 = %d", n));
		n = 4 - 4 * 4 - 4; h.putIfAbsent(n, String.format("4 - 4 * 4 - 4 = %d", n));
		n = 4 - 4 * 4 * 4; h.putIfAbsent(n, String.format("4 - 4 * 4 * 4 = %d", n));
		n = 4 - 4 * 4 / 4; h.putIfAbsent(n, String.format("4 - 4 * 4 / 4 = %d", n));
		n = 4 - 4 / 4 + 4; h.putIfAbsent(n, String.format("4 - 4 / 4 + 4 = %d", n));
		n = 4 - 4 / 4 - 4; h.putIfAbsent(n, String.format("4 - 4 / 4 - 4 = %d", n));
		n = 4 - 4 / 4 * 4; h.putIfAbsent(n, String.format("4 - 4 / 4 * 4 = %d", n));
		n = 4 - 4 / 4 / 4; h.putIfAbsent(n, String.format("4 - 4 / 4 / 4 = %d", n));

		n = 4 * 4 + 4 + 4; h.putIfAbsent(n, String.format("4 * 4 + 4 + 4 = %d", n));
		n = 4 * 4 + 4 - 4; h.putIfAbsent(n, String.format("4 * 4 + 4 - 4 = %d", n));
		n = 4 * 4 + 4 * 4; h.putIfAbsent(n, String.format("4 * 4 + 4 * 4 = %d", n));
		n = 4 * 4 + 4 / 4; h.putIfAbsent(n, String.format("4 * 4 + 4 / 4 = %d", n));
		n = 4 * 4 - 4 + 4; h.putIfAbsent(n, String.format("4 * 4 - 4 + 4 = %d", n));
		n = 4 * 4 - 4 - 4; h.putIfAbsent(n, String.format("4 * 4 - 4 - 4 = %d", n));
		n = 4 * 4 - 4 * 4; h.putIfAbsent(n, String.format("4 * 4 - 4 * 4 = %d", n));
		n = 4 * 4 - 4 / 4; h.putIfAbsent(n, String.format("4 * 4 - 4 / 4 = %d", n));
		n = 4 * 4 * 4 + 4; h.putIfAbsent(n, String.format("4 * 4 * 4 + 4 = %d", n));
		n = 4 * 4 * 4 - 4; h.putIfAbsent(n, String.format("4 * 4 * 4 - 4 = %d", n));
		n = 4 * 4 * 4 * 4; h.putIfAbsent(n, String.format("4 * 4 * 4 * 4 = %d", n));
		n = 4 * 4 * 4 / 4; h.putIfAbsent(n, String.format("4 * 4 * 4 / 4 = %d", n));
		n = 4 * 4 / 4 + 4; h.putIfAbsent(n, String.format("4 * 4 / 4 + 4 = %d", n));
		n = 4 * 4 / 4 - 4; h.putIfAbsent(n, String.format("4 * 4 / 4 - 4 = %d", n));
		n = 4 * 4 / 4 * 4; h.putIfAbsent(n, String.format("4 * 4 / 4 * 4 = %d", n));
		n = 4 * 4 / 4 / 4; h.putIfAbsent(n, String.format("4 * 4 / 4 / 4 = %d", n));

		n = 4 / 4 + 4 + 4; h.putIfAbsent(n, String.format("4 / 4 + 4 + 4 = %d", n));
		n = 4 / 4 + 4 - 4; h.putIfAbsent(n, String.format("4 / 4 + 4 - 4 = %d", n));
		n = 4 / 4 + 4 * 4; h.putIfAbsent(n, String.format("4 / 4 + 4 * 4 = %d", n));
		n = 4 / 4 + 4 / 4; h.putIfAbsent(n, String.format("4 / 4 + 4 / 4 = %d", n));
		n = 4 / 4 - 4 + 4; h.putIfAbsent(n, String.format("4 / 4 - 4 + 4 = %d", n));
		n = 4 / 4 - 4 - 4; h.putIfAbsent(n, String.format("4 / 4 - 4 - 4 = %d", n));
		n = 4 / 4 - 4 * 4; h.putIfAbsent(n, String.format("4 / 4 - 4 * 4 = %d", n));
		n = 4 / 4 - 4 / 4; h.putIfAbsent(n, String.format("4 / 4 - 4 / 4 = %d", n));
		n = 4 / 4 * 4 + 4; h.putIfAbsent(n, String.format("4 / 4 * 4 + 4 = %d", n));
		n = 4 / 4 * 4 - 4; h.putIfAbsent(n, String.format("4 / 4 * 4 - 4 = %d", n));
		n = 4 / 4 * 4 * 4; h.putIfAbsent(n, String.format("4 / 4 * 4 * 4 = %d", n));
		n = 4 / 4 * 4 / 4; h.putIfAbsent(n, String.format("4 / 4 * 4 / 4 = %d", n));
		n = 4 / 4 / 4 + 4; h.putIfAbsent(n, String.format("4 / 4 / 4 + 4 = %d", n));
		n = 4 / 4 / 4 - 4; h.putIfAbsent(n, String.format("4 / 4 / 4 - 4 = %d", n));
		n = 4 / 4 / 4 * 4; h.putIfAbsent(n, String.format("4 / 4 / 4 * 4 = %d", n));
		n = 4 / 4 / 4 / 4; h.putIfAbsent(n, String.format("4 / 4 / 4 / 4 = %d", n));

		return h;

	}

}
