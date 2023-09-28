# Time : O(nlogn)
# Space : O(1)
# def containsDuplicate(nums):
#     sortedNums=sorted(nums)
#     for i in range(len(sortedNums) - 1):
#         if sortedNums[i] == sortedNums[i+1]:
#             return True
#     return False





# Time : O(n)
# Space : O(n)
def containsDuplicate(nums):
    seen = set()
    for x in nums:
      if x in seen: return True
      seen.add(x)
    return False


containsDuplicate([1,1,1,3,3,4,3,2,4,2])