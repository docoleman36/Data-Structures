"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value:
            if self.right is not None:
                self.right.insert(value)
            else:
                new_node = BSTNode(value)
                self.right = new_node
        else:
            if self.left is not None:
                self.left.insert(value)
            else:
                new_node = BSTNode(value)
                self.left = new_node

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check if self.value is target
        if self.value is target:
            return True

        if target < self.value:
            if self.left is None:
                return False
            elif self.left.value == target:
                return True
            else:
                self.left.contains(target)
        else:
            if not self.right:
                return False
            elif self.right.value == target:
                return True
            else:
                self.right.contains(target)

    # Return the maximum value found in the tree

    def get_max(self):
        # go right until you cannot anymore
        # return value at far right
        if self.right is None:
            return self.value
        else:
            cur_node = self.right
            while cur_node.right is not None:
                cur_node = cur_node.right
            return cur_node.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.left is None and self.right is None:
            return

        # go left, call fn(value) for each node
        if self.left:
            self.left.for_each(fn)
        # go roght, call fn(value) for each node
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        # place print statement in between recursive calls
        # that explore left and right subtrees

        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        # Create a Queue to keep track of nodes
        # insert self onto beginning of Queue
        # while something still in Queue
        # add left and right if exist to the queue
        # print and remove first node
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        # create a stack to keep track of nodes we are processing
        # push root into stack

        # while something still in the stack (not done processing all nodes)
            # push when we START, pop when a node is DONE
            # +
            # use existing `for_each()` as a reference for traversal logic
            # and don't forget to call `print()`
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass


"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_print()
print("post order")
bst.post_order_dft()
