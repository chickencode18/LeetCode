class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> charMap; 
        int maxLength = 0;
        int left = 0;

        for (int i = 0; i < s.length(); ++i) {
            char currentChar = s[i];

       
            if (charMap.find(currentChar) != charMap.end() && charMap[currentChar] >= left) {
                left = charMap[currentChar] + 1; 
            }

            charMap[currentChar] = i;
            maxLength = max(maxLength, i - left + 1);
        }

        return maxLength;
    }
};