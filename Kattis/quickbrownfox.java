import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.Math;
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

		String a = "abcdefghijklmnopqrstuvwxyz";
		Reader r = new Reader();

		int n = r.ni();
		
		for (int i = 0; i < n; i++) {

			String s = r.n().toLowerCase();
			ArrayList<Character> m = new ArrayList<Character>();

			for (int j = 0; j < 26; j++)
				if (s.indexOf(a.charAt(j)) == -1) m.add(a.charAt(j));

			if (m.isEmpty())
				System.out.println("pangram");
			else {
				System.out.print("missing ");
				for (char c : m) System.out.print(c);
				System.out.print('\n');
			}

		}

	}

}
