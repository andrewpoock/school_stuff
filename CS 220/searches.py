# searches.py

def serach_cheat(items, target):
    try:
        ans = items.index(target)
    except ValueError:
        ans = -1
    return ans

def search(items, target):
    for i in range(len(items)):
        if target == items[i]:
            return i
    # assert target is not in items
    return -1

def search1(items, target):
    for i, item in enumerate(items):
        if target == item:
            return i
    return -1

def search2(items target):
    low = 0
    high = len(items)-1
    while low <= high:
        mid = (low+high) // 2
        if target == items[mid]:
            return mid
        elif target < items[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1
