# Binary search with recurion
# given a sorted list of int, return the index of number of the target number, -1 is not found
def binarySearch(l:list, target:int, low=0, high=None):
    if high==None: high=len(l)-1
    if low>=high:
        return low if l[low]==target else -1
    middle=(low+high)//2
    if l[middle]==target:
        return middle
    elif l[middle]>target:
        return binarySearch(l, target, low, middle-1)
    else:
        return binarySearch(l, target, middle+1, high)

mysortedlist=[1,2,3,4,5,6,7,8,9]
target=11
print(f'Binary search w/ recursion: the index of {target} in {mysortedlist} is {binarySearch(mysortedlist, target)}')

# similar to the above function, but uses while loop instead of recursion calls
def binarySearch2(l: list, target:int):
    low, high = 0, len(l)-1
    while low<=high:
        middle = (low+high)//2
        if l[middle]==target:
            return middle
        elif l[middle]>target:
            high=middle-1
        else:
            low=middle+1
    return -1
mysortedlist=[1,2,3,4,5,6,7,8,9]
target=9
print(f'Binary search w/o recursion: the index of {target} in {mysortedlist} is {binarySearch2(mysortedlist, target)}')