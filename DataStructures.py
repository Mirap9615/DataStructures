
class SingleListNode:
    def __init__(self, value=0):
        self.value = value
        self.next = None


class DoubleListNode:
    def __init__(self, value=0):
        self.value = value
        self.next = None
        self.prev = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get_tail(self):
        return self.tail

    def get_nth_position(self, n):
        if n >= self.size:
            return None
        curr = self.head
        for i in range(n):
            curr = curr.next
        return curr

    def append_by_node(self, node):
        if self.tail:
            self.tail.next = node
        self.tail = node
        if not self.head:
            self.head = node
        self.size += 1

    def append_by_value(self, value):
        node = SingleListNode(value)
        if self.tail:
            self.tail.next = node
        self.tail = node
        if not self.head:
            self.head = node
        self.size += 1

    def prepend_by_node(self, node):
        if self.head:
            node.next = self.head
        self.head = node
        if not self.tail:
            self.tail = node
        self.size += 1

    def prepend_by_value(self, value):
        node = SingleListNode(value)
        if self.head:
            node.next = self.head
        self.head = node
        if not self.tail:
            self.tail = node
        self.size += 1

    def delete_by_pos(self, position):
        if position >= self.size: return -1
        if position == 0:
            self.head = self.head.next
            if not self.head:
                self.tail = None
            self.size -= 1
            return 0
        if position == self.size - 1:
            self.tail = self.get_nth_position(self.size - 1)
            self.tail.next = None
            self.size -= 1
            return 0
        node_before = self.get_nth_position(position - 1)
        if node_before and node_before.next:
            node_before.next = node_before.next.next
            if not node_before.next:
                self.tail = node_before
        self.size -= 1

    def get_size(self):
        return self.size

    def insert_by_value(self, position, value):
        node = SingleListNode(value)
        if position >= self.size:
            return -1
        if position == 0:
            self.prepend_by_node(node)
            return 0
        curr = self.head
        for i in range(position - 1):
            curr = curr.next
        # curr will be the prev node
        if curr:
            node.next = curr.next
            curr.next = node
            if not curr.next.next:
                self.tail = curr.next
        # no need to check head here
        self.size += 1

    def update_node(self, position, value):
        node = self.get_nth_position(position)
        if node:
            node.value = value

    def reverse(self):
        # returns the new head
        prev = None
        curr = self.head
        self.tail = self.head
        while curr:
            # store next
            temp_next = curr.next
            # flip direction
            curr.next = prev
            # bring up the rear
            prev = curr
            # move on
            curr = temp_next
        self.head = prev
        return self.head


def functionName(inputString, inputChar, inputIn = 0):
    anyType = inputIn
    return anyType

def square(x):
    return x * x

def cube(x):
    return x * x * x

def apply_function(c, x):
    return c(x)

def zealous(x):
    return "Zealous"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(apply_function(square, 5))  # Output: 25
    print(apply_function(cube, 5))  # Output: 125
    print(apply_function(zealous, "helo"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


