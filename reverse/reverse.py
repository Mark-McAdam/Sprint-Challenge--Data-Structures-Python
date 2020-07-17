class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        """
        reverse the contents of the list using recursion, not a loop

        NOT A LOOP MARK 
        """
    
        # Recursive version
        
        # case 3 
        # node is none, basically tail node will
        # pass none as the next node because its the end
        if node is None:
            return

        # If the node is the tail, set it to the head
        # The current tail's get next value will be None

        if node.get_next() is None:
            # Set to head
            self.head = node
            # The current node's next node will be its previous
            node.set_next(prev)
            return

        # Capture the current node's next node
        next_node = node.get_next()

        # The current node's next node will be its previous
        node.set_next(prev)
        
        # call method recursively
        # call next node as the current 
        # node as previous 
        self.reverse_list(next_node, node)


    




# non recursive version of iterating through
# set previous to None
        # set current to head
        # prev = None
        # current_node = self.head 
        
        # while(current_node): 
            
        #     # new node from next 
        #     newnode = current_node.get_next()
            
        #     # current node to previous node
        #     current_node.set_next(prev)
            
        #     # set prev to current 
        #     prev = current_node
            
        #     # move current and previous nodes one step forward
        #     current_node = newnode

        # self.head = prev

        # now that its laid out I just need to do it recursively. 