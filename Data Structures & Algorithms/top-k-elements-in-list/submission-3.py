class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequencies
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        # Create frequency buckets
        freq = [[] for i in range(len(nums) + 1)]
        # Put numbers in the buckets 
        for num, cnt in counts.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
