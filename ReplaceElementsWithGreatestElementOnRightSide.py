class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1
        for index in range(len(arr) - 1, -1, -1):
            newMax = max(rightMax, arr[index])
            arr[index] = rightMax
            rightMax = newMax
        return arr
