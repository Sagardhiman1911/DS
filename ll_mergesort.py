from ds import LinkedList


def merge_sort(ll):
    if ll.size() == 1:
        return ll
    elif ll.head is None:
        return ll
    left_half, right_half = split(ll)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(ll):
    if ll is None or ll.head is None:
        left_half = ll
        right_half = None
        return left_half, right_half
    else:
        size = ll.size()
        mid = size//2

        mid_node = ll.node_at_index(mid-1)

        left_half = ll
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half


def merge(left, right):
    """
    Merges 2 link list, sorting data in nodes
    return a new merged list
    """
    # create a new linked list that contains nodes from left, right
    merged = LinkedList()

    # Add a fake head that is discarded later
    merged.add(0)

    # Set current to the head of linked list
    current = merged.head

    # Obtain head nodes for left and right lists
    left_head = left.head
    right_head = right.head

    # Iterate over left and right until we reach the tail node of either
    while left_head or right_head:
        # if the head node of left is none are past the tail
        # add the node from right to merged linked list
        if left_head is None:
            current.next_node = right_head
            # call next on right to set loop condition to false
            right_head = right_head.next_node
        # if the head node of right is None we are past the tail
        # add the tail node from left to merged linked list
        elif right_head is None:
            current.next_node = left_head
            # call next on left to set loop condition to false
            left_head = left_head.next_node
        else:
            # Not at either tail node
            # obtain node data o perform comparison operations
            left_data = left_head.data
            right_data = right_head.data
            # if data on left is less than right, set current to left node
            if left_data < right_data:
                current.next_node = left_head
                # move left head to next node
                left_head = left_head.next_node
            # if data on left is greater than right, set current to right node
            else:
                current.next_node = right_head
                # move right head to next node
                right_head = right_head.next_node
        # move current to next node
        current = current.next_node
    # discard fake head and set first merged node as head
    head = merged.head.next_node
    merged.head = head

    return merged


l = LinkedList()
l.add(10)
l.add(2)
l.add(44)
l.add(5)
l.add(100)

print(l)
print(merge_sort(l))



