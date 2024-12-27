from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxCo = 0
        maxEle= 0
        for i in nums:
            count = 0
            print(i)
            for j in nums:
                if i == j:
                    count +=1
            if count > maxCo:
                maxCo = count
                maxEle = i
        print(maxEle)
        
sol= Solution()
sol.majorityElement([5,3,5,2,6,3])