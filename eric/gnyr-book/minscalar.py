def solve():
	T = int(input().strip())
	for x in range(1, T + 1):
		N = int(input().strip())
		V_1 = list(map(int, input().strip().split()))
		V_1.sort()

		V_2 = list(map(int, input().strip().split()))
		V_2.sort()

		product = 0
		for i in range(N):
			product += V_1[i] * V_2[N - i]

		print(f"Case #{x}: {product}")

solve()