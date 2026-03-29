def isBadVersion(version):
    return version >= 4

class Solution:
    def badversion(self,n:list)->int:
        left = 1
        right = n

        while left < right:
            mid = (left+right)//2
            
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left
    
sol = Solution()
print(sol.badversion(5))
