class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dict = {}
        for letter in s:
            if letter in dict:
                dict[letter] += 1
            else:
                dict[letter] = 1
        for letter in t:
            if letter not in dict or dict[letter] == 0:
                return letter
            else:
                dict[letter] -= 1
        return ''
