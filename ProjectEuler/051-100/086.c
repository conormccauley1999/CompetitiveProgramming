// Problem 86

#include <stdio.h>
#include <math.h>

int calc(int m) {

	int t = 0;
	int w2 = m * m;

	for (int h = 1; h <= m; h++) {
		for (int d = h; d <= m; d++) {
			double v = sqrt((double) (w2 + (h + d) * (h + d)));
			if (v == (int) v) t++;
		}
	}

	return t;

}

int main() {

	int v = 0;
	int m = 0;

	while (v <= 1000000) {
		v += calc(++m);
		printf("%d %d\n", m, v);
	}

	printf("%d\n", m);
	return 0;

}
