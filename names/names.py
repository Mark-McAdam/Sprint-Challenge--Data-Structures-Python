import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

end_time = time.time()
runtime = end_time - start_time
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {runtime} seconds")



class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Case 1: value is less than self.value
        if value < self.value:
            # If there is no left child, insert value here
            if self.left is None:
                self.left = BSTNode(value)
            else:
                # Repeat the process on left subtree
                self.left.insert(value)

        # Case 2: value is greater than or equal self.value
        elif value >= self.value:
            # If there is no right child, insert value here
            if self.right is None:
                self.right = BSTNode(value)
            else:
                # Repeat the process on right subtree
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    # this is basically the preorder version of the contains 
    # function - this node then left then right 

    # there is also a postorder version that would
    # left sub tree right then current 
    def contains(self, target):
        # Case 1: self.value is equal to the target
        if self.value == target:
            return True
        # Case 2: target is less than self.value 
        if target < self.value:
            # if self.left is None, it isn't in the tree
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        # Case 3: otherwise
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # forget about the left subtree
        # iterate through the nodes using a loop construct
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()


    # Call the function `fn` on the value of each node
    # this then left then right 
    def for_each(self, fn):
        fn(self.value)

        if self.left:
            self.left.for_each(fn)

        if self.right:
            self.right.for_each(fn)


print('*'*50)
print('Part two ')
start_time2 = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# _________________________________________________________

bst = BSTNode(names_1[0])

for name in names_1:
    bst.insert(name)

for name in names_2:
    if bst.contains(name):
        duplicates.append(name)


end_time2 = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
runtime2 = end_time2 - start_time2
print (f"runtime2 : {runtime2} seconds")

# run time 2 minus runtime 1 
runtime_diff = runtime - runtime2
print (f"runtime difference: {runtime_diff} seconds faster")

runtime_mult = runtime/runtime2
# runtime 2 divided by runtime 1
print (f"runtime multiple: {runtime_mult} times faster")


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
