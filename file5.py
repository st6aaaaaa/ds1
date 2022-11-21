def merge_sort(a):
    if len(a)<=1:
        return a
    pivot = int(len(a)/2)
    left = merge_sort(a[0:pivot])
    right = merge_sort(a[pivot:])
    return merge(left,right)
def merge(left,right):
    ret = []
    left_cursor = right_cursor = 0

    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] < right[right_cursor]:
            ret.append(left[left_cursor])
            left_cursor+=1
        else:
            ret.append(right[right_cursor])
            right_cursor+=1
    ret.extend(left[left_cursor:])
    ret.extend(right[right_cursor:])

    return ret

a =[3,2,1,4,5]
a = merge_sort(a)
print(a)



