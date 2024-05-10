class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = [0, 0]
        def find_longest(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1

        for i in range(len(s)):
            longest = ans[1] - ans[0] + 1
            # odd
            odd = find_longest(i, i)
            if odd > longest:
                offset = odd // 2
                ans = [i - offset, i + offset]

            # even
            even = find_longest(i, i + 1)
            if even > longest:
                offset = (even // 2) - 1
                ans = [i - offset, i + 1 + offset]
        l_idx, r_idx = ans
        return s[l_idx:r_idx + 1]
    

sol = Solution()
print(sol.longestPalindrome("ABBAC"))