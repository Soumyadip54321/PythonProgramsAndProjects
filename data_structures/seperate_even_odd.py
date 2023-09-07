#from Linked_list import Node
from Linked_list import LinkedList
import random


def sort_list_with_odd_even(input_list):
    even_node_to_swap = input_list.get_head_node()
    even_node_prev = None
    odd_node_to_swap = input_list.get_head_node()
    odd_node_to_swap_prev = None

    while even_node_to_swap is not None and odd_node_to_swap is not None:
        if even_node_to_swap.get_value() % 2 == 0:         # For head node
            odd_node_to_swap = even_node_to_swap.get_next_node()
            while odd_node_to_swap:
                if odd_node_to_swap.get_value() % 2 != 0:

                    if even_node_prev is None:
                        input_list.head_node = odd_node_to_swap
                        temp = odd_node_to_swap.get_next_node()
                        if even_node_to_swap.get_next_node() == odd_node_to_swap:
                            input_list.head_node.set_next_node(even_node_to_swap)
                        else:
                            input_list.head_node.set_next_node(even_node_to_swap.get_next_node())
                            odd_node_to_swap_prev.set_next_node(even_node_to_swap)

                    elif even_node_to_swap.get_next_node() == odd_node_to_swap:
                        even_node_prev.set_next_node(odd_node_to_swap)
                        temp = odd_node_to_swap.get_next_node()
                        odd_node_to_swap.set_next_node(even_node_to_swap)

                    else:
                        even_node_prev.set_next_node(odd_node_to_swap)
                        temp = odd_node_to_swap.get_next_node()
                        odd_node_to_swap.set_next_node(even_node_to_swap.get_next_node())
                        odd_node_to_swap_prev.set_next_node(even_node_to_swap)

                    even_node_to_swap.set_next_node(temp)
                    even_node_prev = odd_node_to_swap
                    #even_node_to_swap = odd_node_to_swap.get_next_node()
                    linked_list = ll.stringify_list()           # printing the linked list with odds in front of the evens
                    break
                else:
                    odd_node_to_swap_prev = odd_node_to_swap
                    odd_node_to_swap = odd_node_to_swap.get_next_node()
        else:
            even_node_prev = even_node_to_swap
            even_node_to_swap = even_node_to_swap.get_next_node()

    return input_list


ll = LinkedList(12)
for i in range(5):
    ll.insert_beginning(random.randint(1, 10))
"""ll.insert_beginning(7)
ll.insert_beginning(4)
ll.insert_beginning(2)"""

# TESTING CODE-----------------------

print(ll.stringify_list())
new_list = sort_list_with_odd_even(ll)
print("The odd-first-even-later sorted linked list is")
print(new_list.stringify_list())









