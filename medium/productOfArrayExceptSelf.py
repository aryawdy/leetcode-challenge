def productExceptSelf(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        prefix = 1
        postfix = 1
        result = [0]*n
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
  
        for i in range(n-1,-1,-1):
            result[i] *= postfix
            postfix *= nums[i]
              

        print(result)
        return result
            
            

productExceptSelf([1,2,3,4])