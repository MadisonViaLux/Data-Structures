# How do you find and return the middle node of a singly linked list
# in one pass? You do not have access to the length of the list. If
# the list is even, you should return the first of the two “middle”
# nodes. You may not store the nodes in another data structure.



# make a function that makes one pass through the given LL

# stops when node.next = null (while loop)

# send in the next node in the function call add 1 to our counter (node.next)

# base case is when node = null return the counter

# half the counter to get the middle point then return the the value,
# if counter is even should return the first of the two “middle” nodes

# compare returned with the current-level and repeat until we get to the half way point

# def new_func(node):
#     fast = slow = node
#     while(fast.next, fast.next.next):
#         slow = slow.next
#         fast = fast.next.next
#     return slow.value





# How do you reverse a singly linked list without recursion?  You
# may not store the list, or it’s values, in another data structure.
# The linked list is constructed only using the class below.  You may
# modify the class as you see fit to solve the problem, but the list
# has already been constructed.


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def add(self, value):
        self.next = Node(value)
def reverse(head):
    pass
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
print(reverse(head))
