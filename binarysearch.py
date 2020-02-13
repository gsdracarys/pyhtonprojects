def binarysearch(list,target):
    if len(list) == 0:
        return -1

    left = 0
    right = (len(list) -1)
    while left < right:
        mid = (left + right)/2
        if list[mid] == target:
            print(target)
            print(mid)
        if (list[left] < target):
            left = mid + 1
        else:
            right = mid - 1

print(binarysearch([1,2,3,4,5,6], 7))