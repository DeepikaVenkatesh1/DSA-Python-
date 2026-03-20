def findMissingNumber(nums):
    n = len(nums)
    expected_sum= n * (n+1) //2
    actual_sum = sum(nums)
    return expected_sum-actual_sum

print(findMissingNumber([0,1,2,4,5]))