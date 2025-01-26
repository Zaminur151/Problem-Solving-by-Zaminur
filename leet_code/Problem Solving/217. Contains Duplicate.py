from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # Hash Map approch. time complexity of this approach is O(n)
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False

        # shorting approach. time complexity of this approach is O(n log n)
        """        
        nums.sort()
        for i in range(1, len(nums)-1):
            if nums[i] == nums[i-1]: 
                return True
        return False

        """
        # time complexity of this approach is O(n^2). so, this approach is not efficient for large arrays
        """        
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums), +1):
                if nums[i] == nums[j]: 
                    return True
        return False

        """
sol= Solution()
sol.containsDuplicate([1,2,3,1])