class Solution:
    def jumpGame(self,nums:list)->bool:
        max_reach = 0

        for i in range(len(nums)):
            if i >max_reach:
                return False
            max_reach=max(max_reach,i+nums[i])
        return True
sol=Solution()
print(sol.jumpGame([1,2,3,4]))
print(sol.jumpGame([3,2,1,0,4]))