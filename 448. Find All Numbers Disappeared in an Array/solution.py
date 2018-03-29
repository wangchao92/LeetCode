class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for num in nums:
            nums[abs(num) - 1] = -abs(nums[abs(num) - 1])
        
        ans = []
        for i, num in enumerate(nums):
            if num > 0:
                ans.append(i + 1)
        return ans
