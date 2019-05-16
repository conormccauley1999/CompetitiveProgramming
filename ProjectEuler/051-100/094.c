// Problem 94

#include <stdio.h>
#include <math.h>

int calcAdd(long x) {
	double r = 0.25 * (x + 1) * sqrt((double) (3 * x * x) - (2 * x) - 1);
	return (r == (long) r);
}

int calcSub(long x) {
	double r = 0.25 * (x - 1) * sqrt((double) (3 * x * x) + (2 * x) - 1);
	return (r == (long) r);
}

int main() {

	long s = 0;

	for (long x = 5; x <= 333333333; x++) {
		if (calcAdd(x)) {
			//printf("%ld %ld %ld\n", x, x, x + 1);
			s += (3 * x) + 1;
		}
		if (x != 1 && calcSub(x)) {
			//printf("%ld %ld %ld\n", x, x, x - 1);
			s += (3 * x) - 1;
		}
	}

	printf("%ld\n", s);
	return 0;

}
