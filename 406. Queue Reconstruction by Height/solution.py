class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        num = len(people)
        ans = [None] * num
        people.sort(key=lambda k: (k[0], -k[1]))
        for person in people:
            pos = 0
            for idx in range(num):
                if pos == person[1] and ans[idx] is None:
                    ans[idx] = person
                    break
                if ans[idx] is None:
                    pos += 1
        
        return ans
