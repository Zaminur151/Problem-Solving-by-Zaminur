# Step 1: Creating a class to make Node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# Step 2: Creating Node
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# Step 3: Making connection between Nodes
node1.next = node2
node2.next = node3
node3.next = node4

# Step 4: Deleting from first position
head = node1
if head is not None:
    head = head.next # Now 1st node is out of liked list cz head can't able to reach 1st node

# Step 4: Deleting from last position
current = head
while current.next.next is not None:
    current = current.next
current.next = None

# Step 4: Deleting particular node
current = head
while current.next.data !=30:
    current = current.next
current.next = current.next.next


# Step 5: Printing Linked list using Head method
current = head
while current is not None:
    print(current.data)
    current = current.next