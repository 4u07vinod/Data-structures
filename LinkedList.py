
# A Python class for Linked List

# A Node class


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

class UnorderedList():

    def __init__(self):
        self.head = None

    def add(self, item):
        node = Node(item)
        node.set_next(self.head)
        self.head = node

    def is_empty(self):
        return self.head == None

    def search(self, item):
        current = self.head
        while current is not None:
            if item == current.get_data():
                return True
            current = current.get_next()
        return False

    def remove(self, item):
        current = self.head
        previous = None
        while current is not None:
            if item == current.get_data():
                previous.set_next(current.get_next())
                return True
            previous = current
            current = current.get_next()
        return False

    def size(self):
        current = self.head
        size = 0
        while current is not None:
            print ('data: {0}'.format(current.get_data()))
            current = current.get_next()
            size += 1
        return size

    def insert(self, index, item):
        current = self.head
        item = Node(item)
        if index == 0:
            item.set_next(current.get_next())
            self.head = item
            return
        previous = None
        position = 0
        while current is not None:
            if index == position:
                previous.set_next(item)
                item.set_next(current)
            position += 1
            previous = current
            current = current.get_next()

    def index(self, item):
        current = self.head
        index = 0
        while current is not None:
            if item == current.get_data():
                return index
            index += 1
            current = current.get_next()

    def append(self, item):
        item = Node(item)
        current = self.head
        while current.get_next() is not None:
            current = current.get_next()
        current.set_next(item)

    def pop(self):
        current = self.head
        if current.get_next() is None:
            print ('List is empty')
            return
        previous = None
        while current.get_next() is not None:
            previous = current
            current = current.get_next()
        previous.set_next(None)
        return current.get_data()


def distance_from_nth_last(head, n):
    current = head
    last = head
    for i in range(n):
        last = last.get_next()
    while last.get_next() is not None:
        curdrent = current.get_next()
        last = last.get_next()
    return current


def distance_from_nth_recursion(head, n):
    current = head
    size = 0
    while current is not None:
        current = current.get_next()
        size += 1
    current = head
    for i in xrange(size - (n+1)):
        current = current.get_next()
    return current

def add_to_list(head1, head2):
    number1 = get_number(head1)[::-1]
    number2 = get_number(head2)[::-1]
    number = int(number1) + int(number2)
    list = UnorderedList()
    for i in str(number):
        list.add(int(i))
    return list



def get_number(head):
    current = head
    list = []
    while current is not None:
        list.append(str(current.get_data()))
        current = current.get_next()
    return ''.join(list)





if __name__ == '__main__':
    list = UnorderedList()
    list.add(2)
    list.add(5)
    list.add(3)

    previous = None
    current = list.head
    n = 0
    while current is not None:
        data = current.get_data()
        print 1
        if data == 9:
            previous = current

        while current.get_data() == 9:
            current = current.get_next()
            n+=1
            print 2
            if current is None:
                break
        current = current.get_next()

    if n == 0:
        while current.get_next() is not None:
            current = current.get_next()

        current.set_data(current.get_data + 1)

    if n > 0:
        node = list.size() - n
        while current is not None:
            for i in range(node):
                current = current.get_next()
                print 3

            current.set_data(current.get_data()+1)







