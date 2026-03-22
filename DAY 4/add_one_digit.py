class Solution:
    def addOneDigit(self,digits:list)->list:
        for i in range(len(digits)-1,-1,-1):
            if digits[i]<9:
                digits[i]+=1
                return digits
            digits[i] = 0
    
sol=Solution()
print(sol.addOneDigit([1,2,3]))

