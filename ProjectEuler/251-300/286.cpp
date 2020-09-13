// Problem 256

#include <bits/stdc++.h>
using namespace std;

const int SHOTS = 50;

double prob(double q) {

	double probs[SHOTS];
	for (int i = 1; i <= SHOTS; i++)
		probs[i] = i / q;
	
	double dp[SHOTS + 1][SHOTS + 1];
	dp[1][0] = probs[1];
	dp[1][1] = 1.0 - probs[1];
	for (int i = 2; i <= SHOTS; i++) {
		dp[i][0] = dp[i - 1][0] * probs[i];
		for (int j = 1; j <= SHOTS; j++) {
			dp[i][j] = (dp[i - 1][j] * probs[i]) + (dp[i - 1][j - 1] * (1.0 - probs[i]));
		}
	}

	return fabs(dp[50][20] - 0.02);

}

int main() {

	double q = 52.5;
	double e = 1e-12;
	double s = 0.01;
	double m = 0.99;

	while (true) {

		double p = prob(q);

		if (p < e) {
			printf("%.10f\n", q);
			return 0;
		}

		double x = prob(q + s);
		double y = prob(q - s);
		
		if (x < y) q += s;
		else q -= s;
		
		s *= m;
		
	}
	
}
