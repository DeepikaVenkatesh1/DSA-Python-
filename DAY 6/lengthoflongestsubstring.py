class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left = 0
        char_map = {}
        max_length = 0

        for right in range(len(s)):
            char_map[s[right]] = char_map.get(s[right], 0) + 1

            while len(char_map) > 2:
                char_map[s[left]] -= 1
                if char_map[s[left]] == 0:
                    del char_map[s[left]]
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
    
