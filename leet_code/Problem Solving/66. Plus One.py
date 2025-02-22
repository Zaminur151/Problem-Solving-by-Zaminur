
# main solution
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            digits[i] = 0
        
        # to handle array like [9,9,9] to [1,0,0,0]
        return [1] + digits




# total syntex
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            digits[i] = 0

        return [1] + digits
solution = Solution()
print(solution.plusOne([9,9,9]))