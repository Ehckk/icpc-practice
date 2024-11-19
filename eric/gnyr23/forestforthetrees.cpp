#include <bits/stdc++.h>
using namespace std;

enum direction { R = 'R', U = 'U', L = 'L', D = 'D' };
typedef pair<int, int> p;
int n_t;
int n_s;
int r_max;
set<p> trees;
vector<p> sensors;
p found;
p *is_found = &found;

p adj(p o_p, direction d) {
    int x = o_p.first;
    int y = o_p.second;
    p n_p;
    switch (d) {
        case R:
            n_p.first = x;
            n_p.second = y;
            break;
        case U:
            n_p.first = y;
            n_p.second = -1 * x;
            break;
        case L:
            n_p.first = -1 * x;
            n_p.second = -1 * y;
            break;
        case D:
            n_p.first = -1 * y;
            n_p.second = x;
            break;
    }
    return n_p;
}

bool check(p pos, p t, direction d) {
    set<p> mapped;
    mapped.insert(t);
    for (int i = 1; i < sizeof sensors; i++) {
        p a = adj(sensors[i], d);
        p target = pair(pos.first + a.first, pos.second + a.second); // position to check
        if (trees.find(target) != trees.end()) { // no t at pos
            return false;
        }
        mapped.insert(target);
    }
    if (mapped.size() != n_s) { // not all sensors mapped
        return false;
    }
    vector<p> unmapped;
    set_difference(trees.begin(), trees.end(),
                   mapped.begin(), mapped.end(),
                   inserter(unmapped, unmapped.begin()));
    for (p &o_t: unmapped) {
        int m_dist = abs(o_t.first - pos.first) + abs(o_t.second - pos.second);
        if (m_dist > r_max) {
            continue;
        }
        return false;
    }
    return true;
}

int main() {
    int x, y;
    scanf("%d %d %d\n", &n_t, &n_s, &r_max);
    for (int i = 0; i < n_t; i++) {
        int t_x, t_y;
        scanf("%d %d\n", &x, &y);
        trees.insert(pair(t_x, t_y));
    }
    for (int i = 0; i < n_s; i++) {
        scanf("%d %d\n", &x, &y);
        sensors[i] = pair(x, y);
    }
    for (char d : {'R', 'U', 'L', 'D' }) {
        for (auto& t : trees) {
            p a = adj(sensors[0], (direction)(d)); // x = t_x + s_x
            p pos = pair(t.first - a.first, t.second - a.second); // position to check
            if (trees.find(pos) != trees.end()) {
                continue;
            }
            if (!check(pos, t, (direction)d)) {
                continue;
            }
            if (is_found) {
                cout << "Ambiguous" << endl;
            }
            found = pos;
        }
    }
    if (!is_found) {
        cout << "Impossible" << endl;
    }
    cout << found.first << " " << found.second << endl;
}

