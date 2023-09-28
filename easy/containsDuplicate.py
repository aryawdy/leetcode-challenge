# Time : O(nlogn)
# Space : O(1)
def containsDuplicate(nums):
    sortedNums=sorted(nums)
    for i in range(len(sortedNums) - 1):
        if sortedNums[i] == sortedNums[i+1]:
            return True
    return False


containsDuplicate([1,1,1,3,3,4,3,2,4,2])