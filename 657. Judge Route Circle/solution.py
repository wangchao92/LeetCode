class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        UDstack = []
        LRstack = []
        for char in moves:
            if char == 'U' or char == 'D':
                if len(UDstack) == 0:
                    UDstack.append(char)
                else:
                    if UDstack[-1] == char:
                        UDstack.append(char)
                    else:
                        UDstack.pop()
            else:
                if len(LRstack) == 0:
                    LRstack.append(char)
                else:
                    if LRstack[-1] == char:
                        LRstack.append(char)
                    else:
                        LRstack.pop()
        if len(LRstack) == 0 and len(UDstack) == 0:
            return True
        else:
            return False
