class Solution:
    def insertElement(self,nums:list,target:int)->int:
        left = 0
        right = len(nums) - 1

        while(left  <= right):
            mid = (left + right)//2

            if nums[mid]==target:
                return mid
            
            elif nums[mid] < target:
                left = mid + 1

            elif nums[mid] > target:
                right = mid - 1

            return left
        
sol =Solution()
print(sol.insertElement([1,2,4,5],3))



        