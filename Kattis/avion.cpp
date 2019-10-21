#include <bits/stdc++.h>
#define vpi vector< pair<int, int> >
#define pi pair<int, int>
#define pb push_back
#define mp make_pair
#define f first
#define s second
using namespace std;

int main() {

	string s[5];

	for (int i = 0; i < 5; i++)
		getline(cin, s[i]);

	int c = 0;
	for (int i = 0; i < 5; i++) {
		if (s[i].find("FBI") != string::npos) {
			cout << i + 1 << " ";
			c++;
		}
	}
	
	if (c == 0) cout << "HE GOT AWAY!";
	
	cout << endl;

}
