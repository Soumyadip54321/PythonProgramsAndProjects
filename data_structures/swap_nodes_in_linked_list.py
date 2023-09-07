
from Linked_list import Node
from Linked_list import LinkedList


def swap_nodes(input_list, value1, value2):
    print(f'Swapping {value1} with {value2}')
    node1 = input_list.head_node
    node2 = input_list.head_node
    node1_prev_node = None
    node2_prev_node = None

    if value2 == value1:
        print("Swapping not possible since values are same\n")
        return

    while node1 is not None:
        if node1.get_value() == value1:
            break
        node1_prev_node = node1
        node1 = node1.get_next_node()

    while node2 is not None:
        if node2.get_value() == value2:
            break
        node2_prev_node = node2
        node2 = node2.get_next_node()

    if node2 is None or node1 is None:
        print("Swap not possible since one or more nodes are not present in linked list\n")
        return

    if node1_prev_node is None:
        input_list.head_node = node2
    else:
        node1_prev_node.set_next_node(node2)

    if node2_prev_node is None:
        input_list.head_node = node1
    else:
        node2_prev_node.set_next_node(node1)

    temp = node1.get_next_node()
    node1.set_next_node(node2.get_next_node())
    node2.set_next_node(temp)


ll = LinkedList()
for i in range(10):
  ll.insert_beginning(i)

print(ll.stringify_list())
swap_nodes(ll, 9, 5)
print(ll.stringify_list())



