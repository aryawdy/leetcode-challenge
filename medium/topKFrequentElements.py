# Time : O(mn)
# Space : O(n)
def topKFrequent(nums, k):
    result = list()
    hashMap = {}
    deleteKey = 0
    for num in nums:
        if num in hashMap:
            hashMap[num] = hashMap.get(num) + 1
        else:
            hashMap[num] = 1
    
    for i in range(k):
        max=0
        for key in hashMap:
            if hashMap[key] > max:
                max = hashMap[key]
                deleteKey = key

        hashMap.pop(deleteKey)
        result.append(deleteKey)

    print(result)
    return result    

topKFrequent([1,1,1,2,2,3], 2)