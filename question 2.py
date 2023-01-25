def sum(nums,target):
    nums_map={}
    for i,num in enumerate(nums):
        if target-num in nums_map:
            return (nums_map[target-num],i)
        else:
            nums_map[num]=i
    return none
