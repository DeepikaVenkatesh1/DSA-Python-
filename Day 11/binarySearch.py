class Solution:
    def binarySearch(self,nums:list,target:int)->int:
        left = 0
        right =len(nums)-1

        while left <= right:
            mid=(left+right)//2
            
            if nums[mid]==target:
                return target
            
            elif nums[mid]<target:
                left = mid + 1
            
            else:
                right = mid - 1
        return -1
sol=Solution()
print(sol.binarySearch([1,2,3,4,5],1))