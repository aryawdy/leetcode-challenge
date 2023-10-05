def productExceptSelf(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = list()
        postfix = list()
        result = list()
        total = 1
        for num in nums:
            total = total * num
            prefix.append(total)
            

        print(prefix)
        return result
            
            

productExceptSelf([1,2,3,4])