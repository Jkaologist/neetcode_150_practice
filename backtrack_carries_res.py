from functools import lru_cache
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        @lru_cache
        def is_palindrome(s):
            return s == s[::-1]

        def backtrack(start = 0, path = [], res = []):
            if start == len(s):
                res.append(path)
                return
            for i in range(start, len(s)):
                if is_palindrome(s[start:i + 1]):
                    backtrack(i + 1, path + [s[start: i + 1]], res)
            return res

        return backtrack()
        