
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

# Step 4: Printing Linked list (pointer methon). Also possible using Head method
current = node1
while current is not None:
    print(current.data)
    current = current.next

# Step 4: Printing Linked list using Head method
head = node1
current = head
while current is not None:
    print(current.data)
    current = current.next

# Note:
# why head is not using for this traversing here?
# if we traverse by head then after increment or updating head, head can't back to previous.
# That's why we take a current pointer and traverse the liked list by updating this pointer.