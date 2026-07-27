def find_paths(m, n, N, row, col):

    dp = [[0] * n for _ in range(m)]
    dp[row][col] = 1

    count = 0

    MOD = 1000000007

    for step in range(N):

        temp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):

                if dp[i][j] > 0:

                    for x, y in [(1,0),(-1,0),(0,1),(0,-1)]:

                        ni = i + x
                        nj = j + y

                        if 0 <= ni < m and 0 <= nj < n:
                            temp[ni][nj] = (temp[ni][nj] + dp[i][j]) % MOD
                        else:
                            count = (count + dp[i][j]) % MOD

        dp = temp

    return count


print(find_paths(2, 2, 2, 0, 0))
print(find_paths(1, 3, 3, 0, 1))