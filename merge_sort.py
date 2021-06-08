def merge_sort(list1):
    """
    Sorts a list in ascending order.
    Returns a new sorted list.

    Divide: find the mid point and divide in sub lists
    Conquer: recursively sort the sub lists created in previous step.
    Combine: Merge the sorted sub lists created in previous step.
    """
    if len(list1) <= 1:
        return list1

    left_half, right_half = split(list1)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(list2):
    """
    Divide a list into 2
    Return left and right list
    """
    mid = len(list2)//2
    left = list2[:mid]
    right = list2[mid:]

    return left, right


def merge(left, right):
    """
    Merges 2 lists, sorting them in process.
    return new list
    """
    l = list()
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1
    while j < len(right):
        l.append(right[j])
        j += 1
    return l

