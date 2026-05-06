class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Define left and right pointers 
        l = 0
        r = len(s) - 1

        # Magnificient loop
        while l < r:
            # Check if each letter is alphanumeric 
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            else:
                if s[l].lower() != s[r].lower():
                    return False 
                l += 1
                r -= 1
        return True