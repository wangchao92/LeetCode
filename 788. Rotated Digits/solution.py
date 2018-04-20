class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        validNum = [0, 1, 2, 5, 6, 9, 8]
        ans = 0
        for num in range(1, N + 1):
            validFlag = True
            goodFlag = False
            while num > 0:
                x = num % 10
                num = num / 10
                if x not in validNum:
                    validFlag = False 
                    break
                if x == 2 or x == 5 or x == 6 or x == 9:
                    goodFlag = True
            
            if validFlag and goodFlag:
                ans += 1
                
        return ans
