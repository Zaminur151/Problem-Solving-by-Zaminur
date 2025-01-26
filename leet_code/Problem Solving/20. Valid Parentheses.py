class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")":"(", "}":"{", "]":"[" }

        for i in s:
            if i in closeToOpen:  # checks if the current character i is a closing bracket (i.e., one of ")", "}", or "]").
                if stack and stack[-1] == closeToOpen[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        if stack:
            return False
        else:
            return True

sol = Solution() 
print(sol.isValid('({[]})'))