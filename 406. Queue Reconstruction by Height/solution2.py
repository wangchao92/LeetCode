class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        num = len(people)
        ans = []
        people.sort(key=lambda k: (k[0], -k[1]), reverse=True)
        for person in people:
            ans.insert(person[1], person)
        
        return ans
