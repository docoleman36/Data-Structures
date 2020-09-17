class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # what attributes do we need?
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        # create a new node
        new_node = Node(value)
        if self.head is None:
            # update head and tail attributes
            self.head = new_node
            self.tail = new_node
        elif self.head == self.tail:
            # update its pointer
            new_node.set_next_node(self.head)
            # update head
            self.head = new_node

        else:
            # create a new node
            new_node = Node(value)
            # set next_node of my new node to the head
            new_node.set_next_node(self.head)
            # update head attribute
            self.head = new_node

    def add_to_tail(self, value):
            # create a new node
        new_node = Node(value)
        # 1. LL is empty
        if self.head is None:
            # update head and tail attributes
            self.head = new_node
            self.tail = new_node

        # 2. ll is not empty
        else:
            # update next_node of our tail
            self.tail.set_next_node(new_node)
            # update self.tail
            self.tail = new_node

    def remove_head(self):
        # empty list
        if self.head is None:
            return None
        # else, return VALUE of the old head
        else:
            ret_value = self.head.get_value()
            # list with 1 elements
            if self.head == self.tail:
                self.head = None
                self.tail = None
            # list with +2 elements
            else:
                self.head = self.head.get_next_node()
            return ret_value

    def remove_tail(self):
        # empty list
        if self.head is None:
            return None
        else:
            ret_value = self.tail.get_value()
            # list with 1 element?
            if self.tail == self.head:
                self.tail = None
                self.head = None
            # list with +2 elements?
            else:
                self.tail = self.tail.get_next_node()
            # update tail
            return ret_value

    def contains(self, value):
        # loop through LL until next pointer is None
        cur_node = self.head
        while cur_node is not None:
            # if we find 'value'
            if cur_node.get_value() == value:
                return True
        return False

    def get_max(self):
        # TODO time permitting
        pass
