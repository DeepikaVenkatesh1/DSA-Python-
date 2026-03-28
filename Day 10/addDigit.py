class Solution:
    from typing import List
    def addonedigit(self,digit:List)->List:
        for i in range(len(digit)-1,-1,-1):
            if digit[i]<9:
                digit[i]+=1
                return digit
            digit[i]=0
sol=Solution()
print(sol.addonedigit([1,3,9]))

