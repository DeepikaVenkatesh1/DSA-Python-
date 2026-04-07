# Session 2 - Permutations
# LeetCode #46
# Topic - Backtracking
# Day 17

class Solution:
    def permute(self, nums: list) -> list:
        result = []

        def backtrack(current, remaining):
            if not remaining:           # no more elements!
                result.append(current[:])
                return

            for i in range(len(remaining)):
                current.append(remaining[i])
                backtrack(current,
                         remaining[:i] + remaining[i+1:])
                current.pop()           # backtrack!

        backtrack([], nums)
        return result

# Testing
sol = Solution()
print(sol.permute([1,2,3]))
# [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print(sol.permute([0,1]))
# [[0,1],[1,0]]


    