myList = [1,4,2,8,5,7,10]

# non in place quick sort 1
def quicksort1(l):
    if len(l)<2:
        return l
    pivot = l[0]
    left = list(filter(lambda x: x<=pivot, l[1:]))
    right = list(filter(lambda x: x>pivot, l[1:]))
    return quicksort1(left) + [pivot] + quicksort1(right)

print(f"Quicksort1: {quicksort1(myList)}")

# non in place quick sort 2
def quicksort2(l:list):
    if len(l)<2:
        return l
    left, right, equal = [], [], []
    pivot=l[0]
    for i in l:
        if i<pivot:
            left.append(i)
        elif i==pivot:
            equal.append(i)
        else:
            right.append(i)
    return quicksort2(left)+equal+quicksort2(right)

print(f'Quicksort2: {quicksort2(myList)}')

# in place quick sort; assuming unique numbers
def partition(l:list, low:int, high:int):
    end=high
    pivot=l[end]
    # low is guaranteed to be lower than high as inputs
    while low<high:
        while low<high and l[low]<=pivot: low+=1
        while low<high and l[high]>=pivot: high-=1
        if low<high:
            l[low], l[high] = l[high], l[low]
    l[low], l[end] = l[end], l[low]
    # place the pivot to its correct position
    return low

def quicksort3(l:list, left=0, right=None):
    if right==None: right=len(l)-1
    if left>=right: return
    indexPivot = partition(l, left, right)
    quicksort3(l, left=left, right=indexPivot-1)
    quicksort3(l, left=indexPivot+1, right=right)
    return
quicksort3(myList)
print(f'Quicksort3: in place {myList}')

# in place merge sort
def mergesort(l, left=0, right=None):
    if right==None:
        right=len(l)-1
    if left>=right:
        return
    middle = (left+right)//2 #integer division
    mergesort(l, left=left, right=middle)
    mergesort(l, left=middle+1, right=right)
    merge(l, left, middle, right)
    return
def merge(l:list, left:int, middle:int, right:int):
    if left==middle:
        if l[left] > l[right]:
            l[left], l[right] = l[right], l[left]
        return
    # create temp list
    templist=[]
    low, high = left, middle+1
    while low<=middle and high<=right:
        if l[low]<=l[high]:
            templist.append(l[low])
            low+=1
        else:
            templist.append(l[high])
            high+=1
    # rewrite the original list
    for i in range(len(templist)):
        l[i+left]=templist[i]
    return
myList = [1,4,2,8,5,7,10]
mergesort(myList)
print(f'Mergesort recursive: in place {myList}')

# mergesort iterative 
def merge_iterative(lst:list):
    if len(lst)<=1: return lst
    stack=[(0, len(lst)-1, (len(lst)-1)//2)]
    end=len(lst)-1
    start=0
    while stack!=[]:
        while end>start:
            middle=(start+end)//2
            stack.append((middle+1, end, middle))
            stack.append((start, middle, middle))
            end=middle
		# leaves while-loop when end==start==middle
        merge(lst, start, end, middle)
        start, end, middle=stack.pop()

    merge(lst, 0, len(lst)-1, (len(lst)-1)//2)
    return

myList = [1,4,2,8,5,7,10]
merge_iterative(myList)
print(f'Mergesort iterative: in place {myList}')


# insertion sort
def insertionsort(l:list):
    if len(l)<2:
        return
    i=0
    while i<len(l):
        select=l[i]
        j=i-1
        while j>=0:
            # l[j+1] is empty right now
            if l[j]>select:
                l[j], l[j+1] = l[j+1], l[j]
            # else:
            #     l[j+1]=select
            #     break
            j-=1
        i+=1
    return
myList = [1,4,2,8,5,7,10]
insertionsort(myList)
print(f'Insertionsort: in place {myList}')

# heap sort
from heapq import heappush, heappop
def heapsort(lst):
    heap=[]
    for i in range(len(lst)):
        heappush(heap, lst[i])
    for i in range(len(lst)):
        lst[i] = heappop(heap)
    return
myList = [1,4,2,8,5,7,10]
heapsort(myList)
print(f'Heapsort: in place {myList}')