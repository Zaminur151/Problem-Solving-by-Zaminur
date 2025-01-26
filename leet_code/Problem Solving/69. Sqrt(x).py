class Solution:
    def mySqrt(self, x: int) -> int:

        result = 0
        left = 0
        right = x
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


        # i = 0
        # current = 0
        # while current <= x:
        #     ans = i
        #     i += 1
        #     current = (i)*(i)
        # return ans
