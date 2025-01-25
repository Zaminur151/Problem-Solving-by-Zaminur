
# Need to learn Pointer
# Need to learn Travarsal
# after that should solve it


from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
       numsTemp = nums1+nums2
       for i in range(0,len(numsTemp)-2, +1):
           for j in range(i+1,len(numsTemp)-1 -i, +1):
               if numsTemp[i] > numsTemp[j]:
                   temp = numsTemp[j]
                   numsTemp[j] = numsTemp[j]
                   numsTemp[j] = temp

       print (numsTemp)
        
sol = Solution()
sol.merge([1,2,4],3,[0,3],2)


"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
       numsTemp = nums1+nums2
       for i in range(len(numsTemp)-1):
           for j in range(len(numsTemp)-1 -i):
               if numsTemp[j] > numsTemp[j+1]:
                   temp = numsTemp[j]
                   numsTemp[j] = numsTemp[j+1]
                   numsTemp[j+1] = temp

       print (numsTemp)
        
sol = Solution()
sol.merge([1,2,4],3,[0,3],2)
"""

