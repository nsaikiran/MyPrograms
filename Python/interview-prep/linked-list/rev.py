# Node in a single LL
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

# Given a list construct LL out of it.
def construct_ll(input_list):
    head, prev = None, None
    for obj in input_list:
        curr_node = Node(obj)
        if not head:
            head = curr_node
        if prev:
            prev.next = curr_node
        prev = curr_node
    return head

# Each link is reversed, that is the intuition
def reverse_ll(head_node):
    curr_node = head_node
    prev_node = None
    while curr_node:
        temp = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = temp
    return prev_node

def print_ll(head_node: Node):
    curr_node = head_node
    while curr_node:
        print(curr_node.data, " ", end="")
        curr_node = curr_node.next
    print("")

if __name__ == '__main__':
    print_ll(reverse_ll(construct_ll([1,2,3,4,5,6,7,8,9])))
