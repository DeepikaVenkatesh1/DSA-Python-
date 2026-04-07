class Solution:
    def combinationSum(self,
                       candidates: list,
                       target: int) -> list:
        result = []

        def backtrack(start, current, remaining):
            if remaining == 0:          # found combination!
                result.append(current[:])
                return
            if remaining < 0:           # exceeded target!
                return

            for i in range(start, len(candidates)):
                current.append(candidates[i])
                backtrack(i,            # i not i+1 (reuse!)
                         current,
                         remaining - candidates[i])
                current.pop()           # backtrack!

        backtrack(0, [], target)
        return result


sol = Solution()
print(sol.combinationSum([2,3,6,7], 7))

print(sol.combinationSum([2,3], 6))

print(sol.combinationSum([2], 1))
