class RingBuffer:
    """
     RingBuffer has two methods, append and get. 

    """

    def __init__(self, capacity):
        # define total capacity
        self.capacity = capacity
        # start point
        self.current = 0
        # placeholder list equal to capacity size
        self.storage = [None]*capacity

    def append(self, item):
        """
        The append method adds the given element to the buffer. 
        """

        # case 1 current item is less then capacity
        if self.current < self.capacity:
            # store the item at current place on list by key
            self.storage[self.current] = item
            # increment current place
            self.current += 1
        # case 2 at key 0 current 0 
        else:
            self.current = 0
            self.storage[self.current] = item
            self.current += 1

    def get(self):
        """
        The get method returns all of the elements in the buffer 
        in a list in their given order. 
        """
        # return list of all items in storage 
        # if item does not equal None 
        # It should not return any None values in the list 
        # even if they are present in the ring buffer.
        return [x for x in self.storage if x != None]