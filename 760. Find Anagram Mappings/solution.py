class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        dict = {}
        for i, num in enumerate(B):
            if num in dict:
                dict[num].append(i)
            else:
                dict[num] = [i]
        ans = []
        for num in A:
            if num in dict:
                if len(dict[num]) > 0:
                    print dict[num][0],
                    ans.append(dict[num][0])
                else:
                    print "Not Found"
            else:
                print "Not Found"
        return ans
