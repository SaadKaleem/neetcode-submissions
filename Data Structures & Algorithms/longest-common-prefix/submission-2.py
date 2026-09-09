import math

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest_word_index = self.getShortestWordIndex(strs)

        for char_idx, char in enumerate(strs[smallest_word_index]):
            for word_index, s in enumerate(strs):
                if word_index == smallest_word_index:
                    continue
                else:
                    if char != s[char_idx]:
                        return strs[smallest_word_index][:char_idx]
                
        return strs[smallest_word_index]



    def getShortestWordIndex(self, strs: List[str]) -> int:
        smallest_word_index = 0

        for idx, s in enumerate(strs):
            if len(s) < len(strs[smallest_word_index]):
                smallest_word_index = idx

        return smallest_word_index
