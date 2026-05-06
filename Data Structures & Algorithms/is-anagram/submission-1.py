class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # Count s
        CountS = {} # create dictionary
        for char in s:
            CountS[char] = CountS.get(char, 0) + 1
        
        # Count t
        CountT = {}
        for char in t:
            CountT[char] = CountT.get(char, 0) + 1
        
        return CountS == CountT

        