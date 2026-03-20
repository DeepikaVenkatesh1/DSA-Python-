def containDuplicate(nums):
    seen =set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
    
print(containDuplicate([1,2,3,4,5]))
print(containDuplicate([1,2,3,1]))