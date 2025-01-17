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

# Step 4: Inserting a node at first position
head = node1
new_node = Node(50)
new_node.next = head
head = new_node

# Step 5: Printing Linked list using Head method
current = head
while current is not None:
    print(current.data)
    current = current.next