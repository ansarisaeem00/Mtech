"""
Binomial Heaps contain an unsorted list of binomial trees.

Ops: Extract_Min, Find_Min, Union, Insert.

"""

class BTree():
    '''
    An example of an implementation of a binomial tree.
    '''

    def __init__(self, root):
        self.root = root
        self.children = []
        self.degree = 0

    def merge(self, other):
        if self.degree == other.degree:
            if self.root < other.root:
                self.children.append(other)
                self.degree += 1
            else:
                other.children.append(self)
                other.degree += 1
        #print(self.children)

    # def __str__(self):
    #     return "(%, %)".format(self.root, self.degree)


class LLNode():

    def __init__(self, data):

        self.data = data
        self.next = None

class LList():
    '''
    Linked List class for Binary Heap to use for more efficiency.
    '''
    def __init__(self):
        self.head = None
        self.tail = None


    def insert(self, data):
        node = LLNode(data)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            #to keep the heap sorted by tree degree.
            curr_node = self.head
            while curr_node.next != None and data.degree >= curr_node.data.degree:
                curr_node = curr_node.next
            if curr_node == self.tail:
                curr_node.next = node
                self.tail = node
            else:
                tmp_node2 = curr_node.next
                curr_node.next = node
                curr_node.next.next = tmp_node2

    def remove(self, num):
        curr_node = self.head
        prev_node = None
        removed_node = None
        while curr_node.data.root != num:
            prev_node = curr_node
            curr_node = curr_node.next

        removed_node = curr_node.data
        if curr_node == self.tail:
            self.tail = prev_node
            prev_node.next = None
        else:
            prev_node.next = curr_node.next

        return removed_node
    # def __str__(self):
    #     string = []
    #     curr_node = self.head
    #     while curr_node != None:
    #         string.append(curr_node.data.__str__())
    #         curr_node = curr_node.next
    #     return string


class BHeap():
    '''
    An example of an implementation of a binomial heap.
    '''

    def __init__(self):
        '''Initializes a Binary Heap class
        '''
        self.heap_list = LList()

    def Find_Min(self):
        min = self.heap_list.head.data.root
        curr_node = self.heap_list.head
        while curr_node != None:
            if curr_node.data.root < min:
                min = curr_node.head.root
            curr_node = curr_node.next
        return min

    def Insert(self, num):
        tmp_btree = BTree(num)
        if self.heap_list.head == None:
            self.heap_list.insert(tmp_btree)
        else:
            tmp_bheap = BHeap()
            tmp_bheap.heap_list.insert(tmp_btree)
            self.union(tmp_bheap)
        print(self.heap_list)

    def Extract_Min(self):
        min = self.Find_Min()
        tree_w_min = self.heap_list.remove(min)
        curr_node = self.heap_list.head
        heap_1 = BHeap()
        heap_1.heap_list = self.heap_list
        heap_1.heap_list.remove(tree_w_min)
        heap_2 = BHeap()
        for child in tree_w_min.children:
            heap_2.heap_list.insert(child)
        self = heap_1.union(heap_2)

    def union(self, other):
        '''
        This method contains two steps:

        1st: place all binomial trees in other into self (Could cause duplicate trees).

        2nd: loop over all binomial trees in the heap list, if there are
            binomial trees of the same order, merge them.
        '''
        curr_node = other.heap_list.head
        while curr_node != None:
            self.heap_list.insert(curr_node.data)
            curr_node = curr_node.next

        curr_node = self.heap_list.head
        while curr_node != self.heap_list.tail and curr_node != None:
            if curr_node.data.degree == curr_node.next.data.degree:
                curr_node.data.merge(curr_node.next.data)
                if curr_node.next.next is None:
                    curr_node.next = None
                    self.heap_list.tail = curr_node
                else:
                    curr_node.next = curr_node.next.next
            curr_node = curr_node.next

    def str(self):
        print(self.heap_list)


if __name__ == "__main__":
    bheap = BHeap()
    #for num in range(0, 100, 5):
    bheap.Insert(50)
    #print(bheap.heap_list.head.data.root)
    bheap.Insert(20)    
    #print(bheap.heap_list.head.data.degree)    
    bheap.Insert(5)
    #print(bheap.heap_list.head.data.root)
    bheap.Insert(12)
    #print(bheap.heap_list.head.data.children)
    #print(bheap.Find_Min())
        

    #print(bheap.Extract_Min())