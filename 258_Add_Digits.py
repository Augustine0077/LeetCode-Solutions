class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Direct mathematical approach to find the digital root.
        if num == 0:
            return 0
        return 1 + (num - 1) % 9
