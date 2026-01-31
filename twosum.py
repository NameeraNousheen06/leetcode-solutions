class Solution(object):
    def twoSum(self, nums, target):
        hash = {}

        for i,n in enumerate(nums):
            diff=target-n
            if diff in hash:
                return(hash[diff],i)
            hash[n]=i
        return
        