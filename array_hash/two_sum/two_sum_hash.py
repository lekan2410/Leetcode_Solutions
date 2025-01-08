class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Dictionary
        h = {}

        
        for i, n in enumerate(nums):
            diff = target - n

            #Checks if difference is in dictionary
            if diff in h:
                return [h[diff], i]
            h[n] = i
