class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = dict()
        index = 0
        for num in nums:
            if target - num in visited:
                return [visited[target - num], index]
            visited[num] = index
            index += 1
        return None
