numbers = [1, 3, 2, 4, 7, 5, 2]


def is_sorted(values):
    for index in range(len(values) - 1):
        if values[index] > values[index + 1]:
            return False
    return True


def selection_sort(values):
    """
    Takes O(n2)
    """
    # traverse through all element
    for i in range(len(values)):
        min_idx = i
        # find the min element in remaining array
        for j in range(i+1, len(values)):
            if values[min_idx] > values[j]:
                min_idx = j
        # swap the found minimum with the first element
        values[i], values[min_idx] = values[min_idx], values[i]
    return values


print(selection_sort(numbers))


def partition(start, end, array):
    # Initialize pivot index to start
    pivot_index = start
    pivot = array[pivot_index]

    # This loop runs till start pointer crosses
    # end pointer, and when it does we swap the
    # pivot with element on end pointer
    while start < end:
        # Increment the start pointer till it finds an
        # element greater than  pivot
        while start < len(array) and array[start] <= pivot:
            start += 1

        # Decrement the end pointer till it finds an
        # element less than pivot
        while array[end] > pivot:
            end -= 1

        # If start and end have not crossed each other,
        # swap the numbers on start and end
        if start < end:
            array[start], array[end] = array[end], array[start]

    # Swap pivot element with element on end pointer.
    # This puts pivot on its correct sorted place.
    array[end], array[pivot_index] = array[pivot_index], array[end]

    return end


def quick_sort(start, end, array):
    if start < end:
        # p is partitioning index, array[p]
        # is at right place
        p = partition(start, end, array)

        # Sort elements before partition
        # and after partition
        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)
    return array


list1 = [10, 7, 8, 9, 1, 5]
print(quick_sort(0, len(list1) - 1, list1))

