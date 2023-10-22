def threeSum(nums):
    nums.sort()
    result = []
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i-1]:
            continue
        l, r = i+1, len(nums) - 1
        while l < r:
            threeSum= a + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                result.append([a, nums[l], nums[r]]) 

    
    print("")


threeSum([-1,0,1,2,-1,-4])