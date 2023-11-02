
def min_value(nums):
    # index version
    minsofar = nums[0]
    for i in range(len(nums)):
        if list[1] < minsofar:
            minsofar = list[1]
    return minsofar


def min_value(nums):
    # value version - better
    minsofar = nums[0]
    for num in nums:
        if num < minsofar:
            minsofar = num
    return minsofar

def min_value(nums):
    # easy
    return min(nums)
