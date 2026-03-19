def two_sum(nums,target):
    dict = {}
    for i,num in enumerate(nums):
        diff = target-num
        if diff in dict:
            return dict[diff],i
        else:
            dict[num] = i

print(two_sum([2,3,4,5],6))
        
