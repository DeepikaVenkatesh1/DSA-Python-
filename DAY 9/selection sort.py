class Solution:
    def selectionsort(self,arr):
        n = len(arr)
        for i in range(n):
            min_index=i
            for j in range(i+1,n):
                if arr[j]<arr[min_index]:
                    min_index=j
                    arr[i],arr[min_index]=arr[min_index],arr[i]
        return arr
    
sol=Solution()
print(sol.selectionsort([1,9,8,5,4]))

                