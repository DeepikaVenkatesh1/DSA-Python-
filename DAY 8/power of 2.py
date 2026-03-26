class Solution:
    def power(self,n)->bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        if (n % 2) != 0:
            return False
        return self.power(n//2)
sol = Solution()
print(sol.power(8))
print(sol.power(6))
            
