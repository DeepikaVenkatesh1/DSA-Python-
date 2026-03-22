class Solution:
    def singleNumber(self,nums:list)->int:
        result = 0
        for num in nums:
            result = result ^ num
        return result
sol=Solution()
print(sol.singleNumber([1,1,2,3,2]))
