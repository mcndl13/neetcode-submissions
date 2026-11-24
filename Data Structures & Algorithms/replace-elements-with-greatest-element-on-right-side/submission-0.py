class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_val = -1
        for idx in range(len(arr) - 1, -1, -1):
            temp = arr[idx]  
            arr[idx] = max_val 
            max_val = max(temp, max_val)

        return arr
        