# Time : O(n2)
# Space : O(1)
def twoSum(nums, target):
    result = list()
    valid = False      
    x=0
    while x < len(nums):
        y=x+1
        while y < len(nums):
            if nums[x]+nums[y] == target:
                result.append(x)
                result.append(y)
                valid=True
                break
            y +=1
        if valid:
            break
        x +=1
    print(result)
    return result


twoSum([2,7,11,15],9)