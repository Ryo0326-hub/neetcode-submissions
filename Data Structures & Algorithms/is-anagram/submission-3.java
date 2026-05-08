class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        
        int[] counts = new int[26];
        int[] countt = new int[26];

        // Loop through each string and count frequency
        for (int i = 0; i < s.length(); i++) {
            int index = s.charAt(i) - 'a';
            counts[index]++;
        }

        for (int j = 0; j < t.length(); j++) {
            int index = t.charAt(j) - 'a';
            countt[index]++;
        }

        return Arrays.equals(counts, countt); 
    }
}
