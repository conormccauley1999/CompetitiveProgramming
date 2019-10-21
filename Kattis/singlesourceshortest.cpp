#include<bits/stdc++.h>
using namespace std;
#define INF 0x3F3F3F3F

typedef pair<int, int> ip;

class Graph {
public:

	int n;
	list<ip> *a;

	Graph(int n) {
		this-> n = n;
		a = new list<ip> [n];
	}

	void addEdge(int u, int v, int w) {
		a[u].push_back(make_pair(v, w));
		//a[v].push_back(make_pair(u, w));
	}

	vector<int> shortestPath(int s) {

		vector<int> d(n, INF);
		d[s] = 0;

		priority_queue< ip, vector<ip>, greater<ip> > q;
		q.push(make_pair(0, s));
		
		while (!q.empty()) {

			int u = q.top().second;
			q.pop();

			list<ip>::iterator i;
			for (i = a[u].begin(); i != a[u].end(); ++i) {

				int v = (*i).first;
				int w = (*i).second;

				if (d[u] + w < d[v]) {
					d[v] = d[u] + w;
					q.push(make_pair(d[v], v));
				}

			}

		}

		return d;

	}

};

int main() {

	while (true) {

		int n, m, q, s;
		cin >> n >> m >> q >> s;
		if ((n | m | q | s) == 0) break;

		Graph g(n);

		for (int i = 0; i < m; i++) {
			int u, v, w;
			cin >> u >> v >> w;
			g.addEdge(u, v, w);
		}

		vector<int> d = g.shortestPath(s);

		for (int i = 0; i < q; i++) {
			int x;
			cin >> x;
			if (d[x] == INF)
				cout << "Impossible" << endl;
			else
				cout << d[x] << endl;
		}
	
	}

}
