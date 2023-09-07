from Linked_list import Node
from Linked_list import LinkedList


def find_mid_of_linkedlist(input_list):
    first_ptr = input_list.head_node
    mid_ptr = input_list.head_node
    while first_ptr is not None:
        first_ptr = first_ptr.get_next_node()
        # value_1 = first_ptr.get_value()            # Same as below mentioned problem occurs here as well.
        if first_ptr:
            first_ptr = first_ptr.get_next_node()
            # first_ptr_value = first_ptr.get_value()   # On having this first_ptr_value address gets to None and then .get_value() called on it raises error.
            mid_ptr = mid_ptr.get_next_node()
            mid_value = mid_ptr.get_value()
        else:
            break
    return mid_ptr


def generate_test_linked_list():
    linked_list = LinkedList(4)
    for i in range(3, 0, -1):
        linked_list.insert_beginning(i)
    return linked_list
# TESTING CODE-----------------------


test_list = generate_test_linked_list()
print(test_list.stringify_list())
nth_last = find_mid_of_linkedlist(test_list)
print(nth_last.value)


