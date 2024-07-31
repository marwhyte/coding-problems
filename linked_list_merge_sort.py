from linked_list import LinkedList

def merge_sort(linked_list):
    """
    Sorts a linked list in asc order
    - Recursively divide linked list into sublists contai
    - Repeatedly merge the sublists to produce sorted sublists until one remains

    Returns a sorted linked list

    Runs in O(kn log n)
    """
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list
    
    left, right = split(linked_list)

    left_ll = merge_sort(left)
    right_ll = merge_sort(right)

    return merge(left_ll, right_ll)

def split(linked_list):
    """
    Divide the unsorted list at midpoint into sublists
    Takes O(k log n)
    """
    if linked_list is None or linked_list.head is None:
        left_half = linked_list
        right_half = None

        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size // 2
        mid_node = linked_list.node_at_index(mid - 1)

        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half

def merge(left, right):
    """
    Merges two linked lists, sorting by data in nodes
    Returns a new, merged list
    Runs in O(n)
    """

    merged = LinkedList()
    merged.add(0)
    curr = merged.head
    left_head = left.head
    right_head = right.head

    while left_head or right_head:
        if left_head is None:
            curr.next_node = right_head
            right_head = right_head.next_node
        elif right_head is None:
            curr.next_node = left_head
            left_head = left_head.next_node
        elif left_head.data < right_head.data:
            curr.next_node = left_head
            left_head = left_head.next_node
        else:
            curr.next_node = right_head
            right_head = right_head.next_node
        curr = curr.next_node

    head = merged.head.next_node
    merged.head = head

    return merged

ll = LinkedList()
ll.add(5)
ll.add(3)
ll.add(5)
ll.add(25)
ll.add(4)

print(merge_sort(ll))

