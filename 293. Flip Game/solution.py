class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        for i in range(len(s)):
            str = list(s)
            if s[i] == '+':
                if i + 1 >= len(s):
                    break
                if s[i + 1] == '+':
                    str[i] = '-'
                    str[i + 1] = '-'
                    ans.append("".join(str))
                    
        return ans
