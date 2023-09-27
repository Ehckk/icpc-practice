# include <bits/stdc++.h>
using namespace std;

int n, total;
int brick_counts[3];
int bricks[100];
set creases = set<int>();

bool brickwall(int current) {
    if (current == 0) return true;
    if (current < 0) return false;
    if (creases.find(current) != creases.end()) return false;

    for (int size = 3; size > 0; size--) {
        if (brick_counts[size - 1] == 0) continue;

        brick_counts[size - 1] -= 1;
        if (brickwall(current - size)) return true;
        brick_counts[size - 1] += 1;
    }
    return false;
}

int main() {
    scanf("%d", &n);
    for (int i = 0; i < 3; i++) {
        cin >> brick_counts[i];
    }
    for (int i = 0; i < n; i++) {
        cin >> bricks[i];
        total += bricks[i];
        if (i + 1 < n) creases.emplace(total);
    }

    string result = brickwall(total) ? "YES" : "NO";
    cout << result << endl;    
}
// Result: TLE at 109