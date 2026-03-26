from typing import List
class Solution():
    def maxSumArray(self,nums:List[int],k:int)->float:
        window_sum=sum(nums[:k])
        max_sum=window_sum

        for i in range(k,len(nums)):
            window_sum+=nums[i]-nums[i-k]
            max_sum = max(max_sum,window_sum)

        return max_sum/k
sol=Solution()
print(sol.maxSumArray([1,2,3,4,5],3))