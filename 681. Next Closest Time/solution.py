class Solution(object):
    def isvalid(self, time):
        hh1, mm1 = int(time.split(":")[0][0]), int(time.split(":")[1][0])
        hh2, mm2 = int(time.split(":")[0][1]), int(time.split(":")[1][1])
        if hh1 * 10 + hh2 > 23:
            return False
        if mm1 * 10 + mm2 > 59:
            return False
        return True
            
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        hm = time.split(":")
        digit = []
        digit.append(hm[0][0])
        digit.append(hm[0][1])
        digit.append(hm[1][0])
        digit.append(hm[1][1])
        candidates = set()
        for h1 in range(4):
            for h2 in range(4):
                for m1 in range(4):
                    for m2 in range(4):
                        newtime = digit[h1] + digit[h2] + ":" + digit[m1] + digit[m2]
                        if self.isvalid(newtime):
                            candidates.add(newtime)
                            
        candidates = list(candidates)
        candidates.sort()
        idx = candidates.index(time)
        if idx == len(candidates) - 1:
            return candidates[0]
        else:
            return candidates[idx + 1]
                            
