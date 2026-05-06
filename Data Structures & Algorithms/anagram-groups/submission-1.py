class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create an empty dictionary called groups
        groups = {}

        for word in strs:
            # Use sorted word as key 
            key = "".join(sorted(word))
            # Construct a new group for a new key
            if key not in groups:
                groups[key] = []
            # Process each word and append to the dictionary 
            groups[key].append(word)
        
        return list(groups.values())
