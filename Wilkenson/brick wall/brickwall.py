def brick_wall(N, c1, c2, c3, top_row):
    bricks_total = sum(top_row)
    connection = set()
    c = top_row[0]
    connection.add(c)

    for i in range(1, len(top_row) - 1):
        connection.add(c + top_row[i])
        c = c + top_row[i]

    if solve(top_row, -1, N, c1, c2, c3, bricks_total, connection, 0, {}):
        return "YES"
    return "NO"


def solve(top_row, i, N, c1, c2, c3, brck_amt, connection, wall, dp):
    key = (i, c1, c2, c3, wall)
    if key in dp:
        return dp[key]

    if wall == brck_amt:
        return True
    if wall > brck_amt:
        return False
    if wall in connection:
        return False

    for _ in range(N):
        if c1 > 0:
            if solve(top_row, i + 1, N, c1 - 1,
                     c2, c3, brck_amt, connection, wall + 1, dp):
                dp[key] = True
                return True
        if c3 > 0:
            if solve(top_row, i + 1, N, c1, c2,
                     c3 - 1, brck_amt, connection, wall + 3, dp):
                dp[key] = True
                return True
        if c2 > 0:
            if solve(top_row, i + 1, N, c1,
                     c2 - 1, c3, brck_amt, connection, wall + 2, dp):
                dp[key] = True
                return True
    dp[key] = False
    return False


N, c1, c2, c3 = map(int, input().split())
top_row = list(map(int, input().split()))
print(brick_wall(N, c1, c2, c3, top_row))
