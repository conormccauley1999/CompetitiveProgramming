#include <iostream>
#include <string>

using namespace std;

int main() {

	string s, o;
	cin >> s;

	for (auto c : s) {
		if (c == '<') o.pop_back();
		else o.push_back(c);
	}

	cout << o << endl;

}
