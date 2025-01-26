from typing import List

# moor's voting algorithm (only applicable when mejority element is more then n/2 times)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
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