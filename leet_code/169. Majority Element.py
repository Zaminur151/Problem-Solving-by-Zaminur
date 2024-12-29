from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        maxEle= 0
        for i in nums:
            if count == 0:
                candidate = i
            if candidate == i:
                count +=1
            else:
                count -=1
        
        print(candidate)
        
sol= Solution()
sol.majorityElement([2,2,1,1,1,2,2])