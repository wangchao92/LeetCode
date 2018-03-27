class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {}
        for char in s:
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1
        flag = False
        for value in dict.values():
            if value % 2 == 1:
                if flag == True:
                    return False
                else:
                    flag = True
        return True
