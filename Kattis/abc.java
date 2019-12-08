import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.Math;
import java.util.Arrays;
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

		int[] n = new int[3];
		for (int i = 0; i < 3; i++)
			n[i] = r.ni();

		Arrays.sort(n);
		String s = r.n();

		for (int i = 0; i < 3; i++) {
			if (s.charAt(i) == 'A')
				System.out.print(n[0] + " ");
			else if (s.charAt(i) == 'B')
				System.out.print(n[1] + " ");
			else
				System.out.print(n[2] + " ");
		}


	}

}
