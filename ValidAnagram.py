class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letterCounts = dict()
        for letterS in s:
            letterCounts[letterS] = letterCounts.get(letterS, 0) + 1
        for letterT in t:
            letterCounts[letterT] = letterCounts.get(letterT, 0) - 1
        for letter, count in letterCounts.items():
            if count != 0:
                return False
        return True
