################################## Data Structures ################################

# ------------------------------- Singly Linked List -----------------------------

class SinglyLinkedListNode:
    '''
    |  Singly Linked List Node class.
    
    |  Available member functions include:
    |    initialising constructor
    |    string converter
    '''
    
    def __init__(self, data: int) -> None:
        '''
        |  Construct a new Singly Linked List Node object
        
        |  Args:
        |    data: input value for the node
        
        >>> from DSA import SinglyLinkedListNode
        >>> n = SinglyLinkedListNode(2)
        >>> n.data
        2
        '''
        self.data = data
        self.next = None
    
    def __str__(self) -> str:
        '''
        |  Return node value as a string for printing
        
        |  Returns:
        |    str: string of the node value
        
        >>> from DSA import SinglyLinkedListNode
        >>> n = SinglyLinkedListNode(2)
        >>> print(n)
        2
        '''
        return str(self.data)

class SinglyLinkedList:
    '''
    |  Singly Linked List class.
    
    |  Available member functions include:
    |    initialising constructor
    |    insert
    |    find
    |    deleteVal
    |    printer
    |    reverse
    '''
    
    def __init__(self) -> None:
        '''
        |  Construct a new Singly Linked List Node object
        
        >>> from DSA import SinglyLinkedList
        >>> l = SinglyLinkedList()
        >>> type(l)
        <class 'DSA.SinglyLinkedList'>
        '''
        self.head = None
        self.tail = None
   
    def insert(self, data: int) -> None:
        '''
        |  Insert node into the list
        
        |  Args:
        |    data: input value for the node
        
        >>> from DSA import SinglyLinkedList
        >>> l = SinglyLinkedList()
        >>> l.insert(1)
        >>> l.insert(2)
        >>> l.insert(3)
        >>> l.printer()
        [1, 2, 3]
        '''
        node = SinglyLinkedListNode(data) # new node
        if not self.head: # no head
            self.head = node
        else:
            self.tail.next = node # add behind tail
        self.tail = node # move tail
    
    def find(self, data: int) -> SinglyLinkedListNode:
        '''
        |  Find value in the list
        
        |  Args:
        |    data: value to be found
        
        |  Return:
        |    SinglyLinkedListNode: node if found
        |    None: if not found
        
        >>> from DSA import SinglyLinkedList
        >>> l = SinglyLinkedList()
        >>> l.insert(1)
        >>> l.insert(2)
        >>> l.insert(4)
        >>> l.insert(3)
        >>> print(l.find(4))
        2
        '''
        head = self.head
        prev = None
        while head != None and head.data != data:
            prev = head
            head = head.next
        return prev
    
    def deleteVal(self, data: int) -> bool:
        '''
        |  Delete value in the list
        
        |  Args:
        |    data: value to be deleted
        
        |  Return:
        |    bool: True/False
        
        >>> from DSA import SinglyLinkedList
        >>> l = SinglyLinkedList()
        >>> l.insert(1)
        >>> l.insert(2)
        >>> l.insert(4)
        >>> l.insert(3)
        >>> print(l.deleteVal(2))
        True
        '''
        prevPos = self.find(data)
        if prevPos.next == None:
            return False
        prevPos.next.next = prevPos.next
        return True
    
    def printer(self, sep: str = ', ') -> None:
        '''
        |  Print the list
        
        |  Args:
        |    sep: string separator
        
        >>> from DSA import SinglyLinkedList
        >>> l = SinglyLinkedList()
        >>> l.insert(1)
        >>> l.insert(2)
        >>> l.insert(3)
        >>> l.printer()
        [1, 2, 3]
        '''
        ptr = self.head
        print('[', end = '')
        while ptr != None:
            print(ptr, end = '')
            ptr = ptr.next
            if ptr != None:
                print(sep, end = '')
        print(']')
    
    def reverse(self) -> None:
        '''
        |  Reverse the list  
        
        >>> from DSA import SinglyLinkedList
        >>> l = SinglyLinkedList()
        >>> l.insert(1)
        >>> l.insert(2)
        >>> l.insert(3)
        >>> l.reverse()
        >>> l.printer()
        [3, 2, 1]
        '''
        head = self.head # head pointer
        prev = None # previous pointer
        while head != None: # while there is forward link left
            newHead = head.next # save extra pointer to next element
            head.next = prev # reverse the link of current element
            prev = head # move pointer to previous element
            head = newHead # use extra pointer to move to next element
        self.tail = self.head
        self.head = prev

def merge(list1: SinglyLinkedList, list2: SinglyLinkedList) -> SinglyLinkedList:
    '''
    |  Merge two sorted linked lists
    
    |  Args:
    |    list1: first list
    |    list2: second list
    
    |  Return:
    |    SinglyLinkedList: merged list
    
    >>> from DSA import SinglyLinkedList, merge
    >>> L1 = SinglyLinkedList()
    >>> L1.insert(2)
    >>> L1.insert(4)
    >>> L1.insert(7)
    >>> L2 = SinglyLinkedList()
    >>> L2.insert(1)
    >>> L2.insert(4)
    >>> L2.insert(5)
    >>> merge(L1,L2).printer()
    [1, 2, 4, 4, 5, 7]
    '''
    merged = SinglyLinkedList()
    head1 = list1.head
    head2 = list2.head
    while head1 != None and head2 != None: # both lists not empty
        if head1.data < head2.data: # link node with smaller data
            merged.insert(head1.data)
            head1 = head1.next
        else:
            merged.insert(head2.data)
            head2 = head2.next
    if head1 == None and head2 != None: # list 1 finished
        merged.tail.next = head2 # add remaining list 2 as is
    if head1 != None and head2 == None: # list 2 finished
        merged.tail.next = head1 # add remaining list 1 as is
    return merged

# ------------------------------ Doubly Linked List ----------------------------

class DoublyLinkedListNode:
    '''
    |  Doubly Linked List Node class.
    
    |  Available member functions include:
    |    initialising constructor
    |    string converter
    '''
    
    def __init__(self, data: int) -> None:
        '''
        |  Construct new Doubly Linked List Node object
        
        |  Args:
        |    data: value of the node
        
        >>> from DSA import DoublyLinkedListNode
        >>> n = DoublyLinkedListNode(3)
        >>> n.data
        3
        '''
        self.data = data
        self.next = None
        self.prev = None
    
    def __str__(self) -> str:
        '''
        |  Return node value as a string for printing
        
        |  Return:
        |    str: string of the node value
        
        >>> from DSA import DoublyLinkedListNode
        >>> n = DoublyLinkedListNode(3)
        >>> print(n)
        3
        '''
        return str(self.data) 

class DoublyLinkedList:
    '''
    |  Doubly Linked List class.
    
    |  Available member functions include:
    |    initialising constructor
    |    insert
    |    printer
    |    reverse
    '''
    
    def __init__(self) -> None:
        '''
        |  Construct a new Singly Linked List Node object
        
        >>> from DSA import DoublyLinkedList
        >>> l = DoublyLinkedList()
        >>> type(l)
        <class 'DSA.DoublyLinkedList'>
        '''
        self.head = None
        self.tail = None
    
    def insert(self, data: int) -> None:
        '''
        |  Insert node into the list
        
        |  Args:
        |    data: input value for the node
        
        >>> from DSA import DoublyLinkedList
        >>> l = DoublyLinkedList()
        >>> l.insert(1)
        >>> l.insert(2)
        >>> l.insert(3)
        >>> l.printer()
        [1, 2, 3]
        '''
        node = DoublyLinkedListNode(data) # new node
        if not self.head: # no head
            self.head = node
        else:
            self.tail.next = node # add behind tail
            node.prev = self.tail
        self.tail = node # move tail
    
    def printer(self, sep: str = ', ') -> None:
        '''
        |  Print the list
        
        |  Args:
        |    sep: string separator
        
        >>> from DSA import DoublyLinkedList
        >>> l = DoublyLinkedList()
        >>> l.insert(1)
        >>> l.insert(2)
        >>> l.insert(3)
        >>> l.printer()
        [1, 2, 3]
        '''
        ptr = self.head
        print('[', end = '')
        while ptr != None:
            print(ptr, end = '')
            ptr = ptr.next
            if ptr != None:
                print(sep, end = '')
        print(']')
    
    def reverse(self) -> None:
        '''
        |  Reverse the list  
        
        >>> from DSA import DoublyLinkedList
        >>> l = DoublyLinkedList()
        >>> l.insert(1)
        >>> l.insert(2)
        >>> l.insert(3)
        >>> l.reverse()
        >>> l.printer()
        [3, 2, 1]
        '''
        head = self.head # head pointer
        prev = None # previous pointer
        while head != None: # new node left
            newHead = head.next # save pointer to next node (cut forward link)
            if newHead != None: # check if next node has a reverse link
                newHead.prev = head # save pointer to previous node (cut reverse link)
            head.next = prev # reverse the forward link
            head.prev = newHead # reverse the reverse link
            prev = head # move pointer to previous element
            head = newHead # use saved pointer to move head
        self.tail = self.head
        self.head = prev

# -------------------------- Binary Search Tree ------------------------------


class BSTNode:
    '''
    |  BST Node class.
    
    |  Available member functions include:
    |    initialising constructor
    |    string converter
    '''
    
    def __init__(self, info: int) -> None:
        '''
        |  Construct new BST Node object
        
        |  Args:
        |    info: value of the node
        
        >>> from DSA import BSTNode
        >>> n = BSTNode(4)
        >>> type(n)
        <class 'DSA.BSTNode'>
        '''
        self.info = info
        self.left = None
        self.right = None
        self.level = None
    
    def __str__(self) -> str:
        '''
        |  Return node value as a string for printing
        
        |  Return:
        |    str: string of the node value
        
        >>> from DSA import BSTNode
        >>> n = BSTNode(4)
        >>> print(n)
        4
        '''
        return str(self.info)

class BinarySearchTree:
    '''
    |  Binary Search Tree class.
    
    |  Available member functions include:
    |    initialising constructor
    |    insert
    |    traverse
    |    height
    '''
    
    def __init__(self) -> None:
        '''
        |  Construct a new Binary Search Tree object
        
        >>> from DSA import BinarySearchTree
        >>> t = BinarySearchTree()
        >>> type(t)
        <class 'DSA.BinarySearchTree'>
        '''
        self.root = None
    
    def insert(self, val: int) -> None:  
        '''
        |  Insert node into the tree
        
        |  Args:
        |    val: input value for the node
        
        >>> from DSA import BinarySearchTree
        >>> t = BinarySearchTree()
        >>> t.insert(3)
        >>> t.insert(1)
        >>> t.insert(6)
        >>> t.insert(4)
        >>> t.insert(5)
        >>> t.traverse('IN')
        1 3 4 5 6 
        '''
        if self.root == None:
            self.root = BSTNode(val)
        else:
            current = self.root
            while True:
                if val < current.info: # move to left sub-tree
                    if current.left:
                        current = current.left # root moved
                    else:
                        current.left = BSTNode(val) # left init
                        break
                elif val > current.info: # move to right sub-tree
                    if current.right:
                        current = current.right # root moved
                    else:
                        current.right = BSTNode(val) # right init
                        break
                else:
                    break # value exists
    
    def traverse(self, order: str) -> None:
        '''
        |  Traverses the tree
        
        |  Args:
        |    order: traversal method out of 'PRE', 'IN' and 'POST'
        
        >>> from DSA import BinarySearchTree
        >>> t = BinarySearchTree()
        >>> t.insert(3)
        >>> t.insert(1)
        >>> t.insert(6)
        >>> t.insert(4)
        >>> t.insert(5)
        >>> t.traverse('IN')
        1 3 4 5 6 
        '''
        def preOrder(root):
            print(root.info, end = ' ')
            if root.left != None:
                preOrder(root.left)
            if root.right != None:
                preOrder(root.right)
        def inOrder(root):
            if root.left != None:
                inOrder(root.left)
            print(root.info, end = ' ')
            if root.right != None:
                inOrder(root.right)
        def postOrder(root):
            if root.left != None:
                postOrder(root.left)
            if root.right != None:
                postOrder(root.right)
            print(root.info, end = ' ')
        if order == 'PRE':
            preOrder(self.root)
        elif order == 'IN':
            inOrder(self.root)
        elif order == 'POST':
            postOrder(self.root)
    
    def height(self, root: BSTNode) -> int:
        '''
        |  Calculates height of the tree
        
        |  Args:
        |    root: node to calculate height for
        
        >>> from DSA import BinarySearchTree
        >>> t = BinarySearchTree()
        >>> t.insert(3)
        >>> t.insert(1)
        >>> t.insert(6)
        >>> t.insert(4)
        >>> t.insert(5)
        >>> t.height(t.root)
        3
        '''
        if root.left == None and root.right == None:
            return 0
        elif root.right == None:
            return 1 + self.height(root.left)
        elif root.left == None:
            return 1 + self.height(root.right)
        else:
            return 1 + max(self.height(root.left),self.height(root.right))

# --------------------------------- Suffix Trie --------------------------------

class Trie:
    '''
    |  Trie class.
    
    |  Available member functions include:
    |    initialising constructor
    |    find
    |    insert
    |    checkPrefix
    |    countPrefix
    '''
    
    def __init__(self) -> None:
        '''
        |  Construct a new Trie object
        
        >>> from DSA import Trie
        >>> t = Trie()
        >>> type(t)
        <class 'DSA.Trie'>
        '''
        self.T = {}
    
    def find(self, root: dict, c: str) -> bool:
        '''
        |  Find a char in a Trie
        
        |  Args:
        |    root: Trie to search
        |    c: character to find
        
        |  Return:
        |    bool: True/False
        
        >>> from DSA import Trie
        >>> t = Trie()
        >>> t.insert('abcd')
        >>> t.insert('ace')
        >>> t.insert('about')
        >>> t.find(t.T['a']['b'],'o')
        True
        '''
        return (c in root)
    
    def insert(self, s: str) -> None:
        '''
        |  Insert string into the Trie
        
        |  Args:
        |    s: string to insert
        
        >>> from DSA import Trie
        >>> t = Trie()
        >>> t.insert('abcd')
        >>> t.insert('ace')
        >>> t.insert('about')
        >>> t.find(t.T['a']['b'],'o')
        True
        '''
        root = self.T
        for c in s:
            if not self.find(root,c):
                root[c] = {}
            root = root[c]
            root.setdefault('#',0)
            root['#'] += 1
    
    def checkPrefix(self, s: str) -> bool:
        '''
        |  Check if string is a prefix
        
        |  Args:
        |    s: string to check
        
        |  Return:
        |    bool: True/False
        
        >>> from DSA import Trie
        >>> t = Trie()
        >>> t.insert('abcd')
        >>> t.insert('ace')
        >>> t.insert('about')
        >>> t.checkPrefix('ab')
        True
        '''
        root = self.T
        for idx, char in enumerate(s):
            if char not in root:
                if idx == len(s) - 1:    
                    root[char] = '#'
                else:
                    root[char] = {}
            elif root[char] == '#' or idx == len(s) - 1:
                return True
            root = root[char]
        return False
    
    def countPrefix(self, s: str) -> int:
        '''
        |  Count strings who have some prefix
        
        |  Args:
        |    s: string to check prefix
        
        >>> from DSA import Trie
        >>> t = Trie()
        >>> t.insert('abcd')
        >>> t.insert('ace')
        >>> t.insert('about')
        >>> t.countPrefix('ab')
        2
        '''
        found = True
        root = self.T
        for c in s:
            if self.find(root,c):
                root = root[c]
            else:
                found = False
                break
        if found:
            return root['#']
        return 0