class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0] * n for i in range(m)]
        
        def print_dp():
            print('---')
            for r in dp:
                print(r)
            
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                print(f'r:{r}, c:{c}')
                if r == m-1 and c == n-1:
                    dp[r][c] = 1
                    print_dp()
                    continue
                
                right = dp[r][c+1] if c + 1 < n else 0
                bot = dp[r+1][c] if r+1 < m else 0 
                
                dp[r][c] = right + bot
                print_dp()
        
        return dp[0][0]

sol = Solution()
u = sol.uniquePaths(4, 5)
print(u)