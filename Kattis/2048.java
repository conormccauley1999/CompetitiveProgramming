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

		int w = 4;
		int[][] g = new int[w][w];
		int[][] h = new int[w][w];

		for (int y = 0; y < w; y++)
			for (int x = 0; x < w; x++)
				g[y][x] = r.ni();

		int d = r.ni();

		// left
		if (d == 0) {
			for (int y = 0; y < w; y++) {
				for (int x = 0; x < w - 1; x++) {
					if (g[y][x] != 0) {
						h[y][x] = g[y][x];
						continue;
					}
					int i = x + 1;
					while (i < w) {
						if (g[y][i] != 0) {
							h[y][x] = g[y][i];
							h[y][i] = 0;
							g[y][x] = g[y][i];
							g[y][i] = 0;
							break;
						}
						i++;
					}
				}
				h[y][3] = g[y][3];
			}			
			for (int y = 0; y < w; y++) {
				for (int x = 1; x < w; x++) {
					if (h[y][x] != h[y][x - 1]) continue;
					h[y][x - 1] *= 2;
					for (int i = x + 1; i < w; i++) {
						h[y][i - 1] = h[y][i];
					}
					h[y][3] = 0;
				}
			}
		}

		// right
		if (d == 2) {
			for (int y = 0; y < w; y++) {
				for (int x = w - 1; x >= 0; x--) {
					if (g[y][x] != 0) {
						h[y][x] = g[y][x];
						continue;
					}
					int i = x - 1;
					while (i >= 0) {
						if (g[y][i] != 0) {
							h[y][x] = g[y][i];
							h[y][i] = 0;
							g[y][x] = g[y][i];
							g[y][i] = 0;
							break;
						}
						i--;
					}
				}
				h[y][0] = g[y][0];
			}
			for (int y = 0; y < w; y++) {
				for (int x = 2; x >= 0; x--) {
					if (h[y][x] != h[y][x + 1]) continue;
					h[y][x + 1] *= 2;
					for (int i = x - 1; i >= 0; i--) {
						h[y][i + 1] = h[y][i];
					}
					h[y][0] = 0;
				}
			}
		}

		// up
		if (d == 1) {
			for (int x = 0; x < w; x++) {
				for (int y = 0; y < w - 1; y++) {
					if (g[y][x] != 0) {
						h[y][x] = g[y][x];
						continue;
					}
					int i = y + 1;
					while (i < w) {
						if (g[i][x] != 0) {
							h[y][x] = g[i][x];
							h[i][x] = 0;
							g[y][x] = g[i][x];
							g[i][x] = 0;
							break;
						}
						i++;
					}
				}
				h[3][x] = g[3][x];
			}
			for (int x = 0; x < w; x++) {
				for (int y = 1; y < w; y++) {
					if (h[y][x] != h[y - 1][x]) continue;
					h[y - 1][x] *= 2;
					for (int i = y + 1; i < w; i++) {
						h[i - 1][x] = h[i][x];
					}
					h[3][x] = 0;
				}
			}
		}

		// down
		if (d == 3) {
			for (int x = 0; x < w; x++) {
				for (int y = w - 1; y >= 0; y--) {
					if (g[y][x] != 0) {
						h[y][x] = g[y][x];
						continue;
					}
					int i = y - 1;
					while (i >= 0) {
						if (g[i][x] != 0) {
							h[y][x] = g[i][x];
							h[i][x] = 0;
							g[y][x] = g[i][x];
							g[i][x] = 0;
							break;
						}
						i--;
					}
				}
				h[0][x] = g[0][x];
			}
			for (int x = 0; x < w; x++) {
				for (int y = 2; y >= 0; y--) {
					if (h[y][x] != h[y + 1][x]) continue;
					h[y + 1][x] *= 2;
					for (int i = y - 1; i >= 0; i--) {
						h[i + 1][x] = h[i][x];
					}
					h[0][x] = 0;
				}
			}
		}

		for (int y = 0; y < w; y++) {
			for (int x = 0; x < w; x++)
				System.out.print(String.valueOf(h[y][x]) + " ");
			System.out.print('\n');
		}

	}

}
