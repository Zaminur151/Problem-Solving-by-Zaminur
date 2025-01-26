
# time complexity O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        cnddt1, cnddt2, count1, count2 = 0, 0, 0, 0
        for i in nums:
            if cnddt1 == i:
                count1 += 1
            elif cnddt2 == i:
                count2 += 1
            elif count1 == 0:
                cnddt1, count1 = i, 1
            elif count2 == 0:
                cnddt2, count2 = i, 1
            else:
                count1 -= 1
                count2 -= 1

        count1, count2 = 0, 0
        for i in nums:
            if i == cnddt1:
                count1 += 1
            elif i == cnddt2:
                count2 += 1
        
        # Collect the results
        result = []
        if count1 > len(nums) // 3:
            result.append(cnddt1)
        if count2 > len(nums) // 3:
            result.append(cnddt2)
        
        return result
            
        