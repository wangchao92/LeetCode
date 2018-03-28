class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) == 1:
            return True
        if ord(word[0]) > 96:
            for char in word:
                if ord(char) < 96:
                    return False
            return True
        else:
            if ord(word[1]) > 96:
                for char in word[1:]:
                    if ord(char) < 96:
                        return False
                return True
            else:
                for char in word[1:]:
                    if ord(char) > 96:
                        return False
                return True
