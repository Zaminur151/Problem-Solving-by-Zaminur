class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0 or n==1:
            return 1
        
        ways =[0]*(n+1)         # [0] creates a list with a single element, [0] * (n+1) duplicates the list [0] exactly n+1 times. so it's [0,0,0,----,0]
        ways[0] = ways[1] = 1
        for i in range(2, n+1):
            ways[i] = ways[i-1] + ways[i-2]
        return ways[n]
    
sol = Solution()
print(sol.climbStairs(5))