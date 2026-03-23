from typing import List
class Solution:
    def stockPrice(self,prices:List[int])->int:
        profit = 0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                profit+=prices[i]-prices[i-1]
        return profit
sol=Solution()
print(sol.stockPrice([1,2,3,4]))