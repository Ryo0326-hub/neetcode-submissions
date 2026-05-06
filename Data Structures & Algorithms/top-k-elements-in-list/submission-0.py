class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a dictionary of the number frequency count
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        # Define nums_unique
        nums_unique = list(counts.keys())
        
        # Sort counts dict by frequency (high to low)
        sorted_counts = sorted(
            nums_unique, 
            key=lambda num: counts[num], 
            reverse=True)

        return sorted_counts[:k]
