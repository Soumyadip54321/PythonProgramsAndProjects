from Linked_list import Node
from Linked_list import LinkedList

def find_nth_last_element(input_list, n):
    first_ptr = input_list.head_node
    runner_ptr = None
    count_steps = 1
    while first_ptr is not None:
        first_ptr = first_ptr.get_next_node()
        count_steps += 1
        if count_steps >= n + 1:
            if runner_ptr is None:
                runner_ptr = input_list.head_node
                value = runner_ptr.get_value()
            else:
                runner_ptr = runner_ptr.get_next_node()
                value = runner_ptr.get_value()
    return runner_ptr


def generate_test_linked_list():
    linked_list = LinkedList(51)
    for i in range(50, 0, -1):
        linked_list.insert_beginning(i)
    return linked_list

# TESTING CODE-----------------------


test_list = generate_test_linked_list()
print(test_list.stringify_list())
nth_last = find_nth_last_element(test_list, 4)
print(nth_last.value)
