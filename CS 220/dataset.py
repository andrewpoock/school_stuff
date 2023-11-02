# Dataset.py


class Dataset:
    '''Dataset is a collection of numbers from which simple
    descriptive statistics can be computed.'''

    def __init__(self):
        '''post: self is an empty Dataset'''
        self._nums = []

    def size(self):
        '''size of the collection

        post: returns count of numbers that have been added to self'''

        return len(self._nums)

    def add(self, x):
        '''add x to the data set
        post: x is added to the data set'''

        return self._nums.append(x)

    def min(self):
        '''find the minimum
        pre: size of self >= 1
        post: returns smallest number in self'''

        assert len(self._nums) > 0
        _min = self._nums[0]
        for num in self._nums:
            if num < _min:
                _min = num
        return _min

    def max(self):
        '''find the maximum
        pre: size of self >= 1
        post: returns largest number in self'''

        return max(self._nums)

    def average(self):
        '''calculate the mean
        pre: size of self >= 1
        post: returns the mean of the values in self'''

        return sum(self._nums)/self.size()

    def std_deviation(nums):
        '''calculate the standard deviation
        pre: size of self >= 2
        post: returns the standard deviation of the values in self'''
