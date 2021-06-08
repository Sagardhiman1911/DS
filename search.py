def linear(list1, target):
    for i in range(len(list1)):
        if list1[i] == target:
            return i
    return None


my_list = [1, 2, 3, 4, 5]
# print(linear(my_list, 3))


def binary_search(list1, target):
    first = 0
    last = len(list1) - 1
    while first <= last:
        mid = (first + last)//2
        if list1[mid] == target:
            return mid
        elif list1[mid] < target:
            first = mid + 1
        else:
            last = mid - 1
    return None


# print(binary_search(my_list, 5))


def rec_binary_search(list1, target):
    if len(list1) == 0:
        return False
    else:
        mid = len(list1)//2
        if list1[mid] == target:
            return True
        elif list1[mid] < target:
            return rec_binary_search(list1[mid+1:], target)
        else:
            return rec_binary_search(list1[:mid], target)


print(rec_binary_search(my_list, 5))
