class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        flag = False
        num = 0
        ans = 0
        for i in nums:
            if i == 1:
                if not flag:
                    flag = True
                    num = 1
                else:
                    num += 1
            else:
                if flag:
                    if num > ans:
                        ans = num
                    flag = False
                    num = 0
        if flag:
            if num > ans:
                ans = num
        return ans
