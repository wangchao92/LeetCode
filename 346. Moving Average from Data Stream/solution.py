class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.sum = 0;
        self.window = []
        self.size = size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.window) < self.size:
            self.window.append(val)
            self.sum += val
            return self.sum / float(len(self.window))
        else:
            self.sum -= self.window[0]
            self.sum += val
            del self.window[0]
            self.window.append(val)
            return self.sum / float(self.size)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
