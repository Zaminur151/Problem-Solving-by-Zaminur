class Solution:
    def mySqrt(self, x: int) -> int:

        result = 0
        left = 0
        right = (x+1)//2  # to get ceilling(only for positive int)
        while left <= right:
            mid = (left+right)//2
            if mid**2 > x:
                right = mid-1

            elif mid**2 < x:
                left = mid+1
                result = mid
            else:
                return mid
        return result
    
sol = Solution()
print(sol.mySqrt(16))

""" 
it works but not the best solution
high run time and space com..
"""
        # i = 0
        # current = 0
        # while current <= x:
        #     ans = i
        #     i += 1
        #     current = i*i
        # return ans
