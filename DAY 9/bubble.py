class Solution:
    def bubble(self,arr):
        n = len(arr)
        for i in range(n):
            for j in range(0,n-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        return arr
            
sol=Solution()
print(sol.bubble([1,4,2,3]))
    
