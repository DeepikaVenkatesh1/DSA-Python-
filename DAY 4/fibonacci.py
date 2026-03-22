class Solution:
    def climbStairs(self,n:int)->int:
        if n == 1:
            return 1
        elif n== 2:
            return 2
        prev2=1
        prev1=2
        for i in range(3,n+1):
            curr=prev2+prev1
            prev2=prev1
            prev1=curr
            
            return curr
sol=Solution()
print(sol.climbStairs(7))
print(sol.climbStairs(1))  
print(sol.climbStairs(2))  
print(sol.climbStairs(3))  
print(sol.climbStairs(4))  
print(sol.climbStairs(5))  
print(sol.climbStairs(7))
