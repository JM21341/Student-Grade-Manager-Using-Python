import class_test as ctest

def insertNode(head, data):
    new_node = ctest.Node(data)

    if head is None:
        head = new_node
    else:
        curr = head
        # linked list traversal
        while curr.Node.next is not None:
            curr = curr.Node.next
        
        curr.next = new_node # sets the next node of the last node as the new node

        new_node.prev = curr
    
    return head

if __name__ == "__main__":
    pass