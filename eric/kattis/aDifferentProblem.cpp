# include <bits/stdc++.h>
using namespace std;

long long num1; // between 0 and 10^15 💀
long long num2;

int main() {
	while (scanf("%lld %lld", &num1, &num2) == 2) {
		cout << abs(num1 - num2) << endl;
	}
}