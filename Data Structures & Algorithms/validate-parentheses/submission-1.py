class Solution:
    def isValid(self, s: str) -> bool:
        # Creating an empty stack
        stack = []

        # Pairs dictionary
        pairs = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for char in s:
            if char in pairs:
                if not stack:
                    return False
                top = stack.pop()
                if top != pairs[char]:
                    return False
            else:
                stack.append(char)
        
        return not stack 

        