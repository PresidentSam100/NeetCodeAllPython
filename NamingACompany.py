class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        wordMap = [set() for _ in range(26)]
        for idea in ideas:
            wordMap[ord(idea[0]) - ord('a')].add(idea[1:])
        ans = 0
        for char1 in range(25):
            for char2 in range(char1 + 1, 26):
                intersect = len(wordMap[char1] & wordMap[char2])
                ans += 2 * (len(wordMap[char1]) - intersect) * (len(wordMap[char2]) - intersect)
        return ans
