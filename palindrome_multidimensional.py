class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        palindrome = [[False] * n for _ in range(n)]
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                if s[i] == s[i + length - 1] and (length <= 2 or palindrome[i + 1][i + length - 2]):
                    palindrome[i][i + length - 1] = True
        total = 0
        for i in range(len(palindrome)):
            total += palindrome[i].count(True)
        return total
    
sol = Solution()
print(sol.countSubstrings("AAA")
)