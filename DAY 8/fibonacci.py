class Solution:
    def fibonacci(self,n)->int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fibonacci(n-1)+self.fibonacci(n-2)
    
sol = Solution()
print(sol.fibonacci(10))
    



        
        