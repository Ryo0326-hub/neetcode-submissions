class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Create an empty hashmap seen
        HashMap<Integer, Integer> seen = new HashMap<>();

        // Cook
        for (int i = 0; i < nums.length; i++) {
            int current = nums[i];
            int needed = target - current;

            if (seen.containsKey(needed)) {
                return new int[] {seen.get(needed), i};
            } else {
                seen.put(nums[i], i);
            }
        }
        return new int[] {};
    }
}
