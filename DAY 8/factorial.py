class Solution:
    def factorial(self,n)->int:
        if n == 1 or n == 0:
            return 1
        return n * self.factorial(n-1)
    
sol = Solution()
print(sol.factorial(5))
