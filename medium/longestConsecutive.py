def longestConsecutive(nums):
    numMap = set(nums)
    longest = 0

    for num in nums:
        if num-1 not in numMap:
            length = 0
            while num + length in numMap:
                length += 1
            longest = max(length, longest)

    return longest





longestConsecutive([100,4,200,1,3,2])
longestConsecutive([0,3,7,2,5,8,4,6,0,1])