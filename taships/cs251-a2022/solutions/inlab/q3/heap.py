class Heap:
    '''
    |  Heap class.
    |  Available member functions include:
    |    initialising constructor
    |    parent
    |    left
    |    right
    |    insert
    |    min
    |    Heapify
    |    deleteMin
    '''
    
    def __init__(self, cap: int) -> None:
        '''
        |  Construct new Heap object
        |  Args:
        |    cap: capacity
        '''
        self.H = []
        self.n = 0
        self.M = cap
    
    def parent(self, i: int) -> int:
        '''
        |  Find parent of given node
        |  Args:
        |    i: index of node
        |  Return:
        |    int: index of parent
        '''
        return (i - 1) // 2
    
    def left(self, i: int) -> int:
        '''
        |  Find left child of given node
        |  Args:
        |    i: index of node
        |  Return:
        |    int: index of left child
        '''
        return (2 * i) + 1
    
    def right(self, i: int) -> int:
        '''
        |  Find right child of given node
        |  Args:
        |    i: index of node
        |  Return:
        |    int: index of right child
        '''
        return 2 * (i + 1)
    
    def insert(self, val: int) -> None:
        '''
        |  Insert node into heap
        |  Args:
        |    val: value to insert
        '''
        if self.n != self.M:
            self.H[self.n] = val
            i = self.n
            self.n += 1
            while i != 0 and self.H[self.parent(i)] > self.H[i]:
                self.H[i], self.H[self.parent(i)] = self.H[self.parent(i)], self.H[i]
                i = self.parent(i)
    
    def min(self) -> int:
        '''
        |  Find minimum value in heap
        |  Return:
        |    int: the minimum value
        |    -1: if heap is empty
        '''
        if (self.n != 0):
            return self.H[0]
        return -1
    
    def Heapify(self, root: int) -> None:
        '''
        |  Heapify function
        |  Args:
        |    root: index of top node of the heap
        '''
        l = self.left(root)
        r = self.right(root)
        s = root
        if (l < self.n and self.H[l] < self.H[root]):
            s = l
        if (r < self.n and self.H[r] < self.H[s]):
            s = r
        if s != root:
            self.H[root], self.H[s] = self.H[s], self.H[root]
            self.Heapify(s)
    
    def deleteMin(self) -> None:
        '''
        |  Delete the minimum value
        '''
        if n > 0:
            if n == 1:
                self.H = []
                n = 0
            else:
                n -= 1
                self.H[0] = self.H[n]
                self.Heapify(0)