class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = [0]*26

        if len(s)!=len(t):
            return False
        
        for ch in s:
            char_count[ord(ch) - ord('a')] += 1
        for ch in t:
            char_count[ord(ch) - ord('a')] -=1

        for c in char_count:
            if c!=0:
                return False
        return True