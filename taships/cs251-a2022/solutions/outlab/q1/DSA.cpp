#include "DSA.h"

/* ------------------------------- Data Structures ---------------------------------- */

// ------------------------------- Singly Linked List -----------------------------

SinglyLinkedListNode::SinglyLinkedListNode() {
    data = -1;
    next = NULL;
}

SinglyLinkedListNode::SinglyLinkedListNode (ll val) {
    data = val;
    next = NULL;
}

ostream& operator<<(ostream &out, const SinglyLinkedListNode &node) {
    return out << node.data;
}

SinglyLinkedList::SinglyLinkedList () {
    head = NULL;
    tail = NULL;
}

void SinglyLinkedList::insert (ll data) {
    // input: data to be inserted
    SinglyLinkedListNode *node = new SinglyLinkedListNode(data);
    if (head == NULL) {
        head = node;
    }
    else {
        tail -> next = node;
    }
    tail = node;
}

SinglyLinkedListNode* SinglyLinkedList::find (ll data) {
    // input: data to be found
    SinglyLinkedListNode *ptr = head, *prev = NULL;
    while (ptr != NULL && ptr -> data != data) {
        prev = ptr;
        ptr = ptr -> next;
    }
    return prev;
}

bool SinglyLinkedList::deleteVal (ll data) {
    // input: data to be deleted
    SinglyLinkedListNode *prev = find(data);
    if (prev -> next == NULL) {
        return false;
    }
    prev -> next -> next = prev -> next;
    return true;
}

void SinglyLinkedList::printer (string sep = ", ") {
    // input: separator to be used
    SinglyLinkedListNode *ptr = head;
    cout << "[";
    while (ptr != NULL) {
        cout << *ptr;
        ptr = ptr -> next;
        if (ptr != NULL) {
            cout << sep;
        }
    }
    cout << "]\n";
}

void SinglyLinkedList::reverse () {
    SinglyLinkedListNode *ptr = head, *prev = NULL;
    while (ptr != NULL) {
        SinglyLinkedListNode *ptr2 = ptr -> next;
        ptr -> next = prev;
        prev = ptr;
        ptr = ptr2;
    }
    tail = ptr;
    head = prev;
}

SinglyLinkedList merge (SinglyLinkedList list1, SinglyLinkedList list2) {
    // input: two sorted lists
    SinglyLinkedList merged;
    SinglyLinkedListNode *head1 = list1.head, *head2 = list2.head;
    while (head1 != NULL && head2 != NULL) {
        if (head1 -> data < head2 -> data) {
            merged.insert(head1 -> data);
            head1 = head1 -> next;
        }
        else {
            merged.insert(head2 -> data);
            head2 = head2 -> next;
        }
    }
    if (head1 == NULL && head2 != NULL) {
        merged.tail -> next = head2;
    }
    if (head2 == NULL && head1 != NULL) {
        merged.tail -> next = head1;
    }
    return merged;
}

// ------------------------------- Doubly Linked List -----------------------------

DoublyLinkedListNode::DoublyLinkedListNode () {
    data = -1;
    next = NULL;
    prev = NULL;
}

DoublyLinkedListNode::DoublyLinkedListNode (ll val) {
    data = val;
    next = NULL;
    prev = NULL;
}

ostream& operator<<(ostream &out, const DoublyLinkedListNode &node) {
    return out << node.data;
}

DoublyLinkedList::DoublyLinkedList () {
    head = NULL;
    tail = NULL;
}

void DoublyLinkedList::insert (ll data) {
    // input: data to be inserted
    DoublyLinkedListNode *node = new DoublyLinkedListNode(data);
    if (head == NULL) {
        head = node;
    }
    else {
        tail -> next = node;
        node -> prev = tail;
    }
    tail = node;
}

void DoublyLinkedList::printer (string sep = ", ") {
    // input: separator to be used
    DoublyLinkedListNode *ptr = head;
    cout << "[";
    while (ptr != NULL) {
        cout << *ptr;
        ptr = ptr -> next;
        if (ptr != NULL) {
            cout << sep;
        }
    }
    cout << "]\n";
}

void DoublyLinkedList::reverse () {
    DoublyLinkedListNode *ptr = head, *pr = NULL;
    while (ptr != NULL) {
        DoublyLinkedListNode *ptr2 = ptr -> next;
        if (ptr2 != NULL) {
            ptr2 -> prev = ptr;
        }
        ptr -> next = pr;
        ptr -> prev - ptr2;
        pr = ptr;
        ptr = ptr2;
    }
    tail = ptr;
    head = pr;
}

// ------------------------------- Binary Search Tree -----------------------------

BSTNode::BSTNode (ll val) {
    info = val;
    level = 0;
    left = NULL;
    right = NULL;
}

ostream& operator<<(ostream &out, const BSTNode &node) {
    return out << node.info;
}

BinarySearchTree::BinarySearchTree () {
    root = NULL;
}

void BinarySearchTree::insert(ll val) {
    // input: value to add
    if (root == NULL) {
        root = new BSTNode(val);
    }
    else {
        BSTNode *ptr = root;
        while (true) {
            if (val < ptr -> info) {
                if (ptr -> left != NULL) {
                    ptr = ptr -> left;
                }
                else {
                    ptr -> left = new BSTNode(val);
                    break;
                }
            }
            else if (val > ptr -> info) {
                if (ptr -> right != NULL) {
                    ptr = ptr -> right;
                }
                else {
                    ptr -> right = new BSTNode(val);
                    break;
                }
            }
            break;
        }
    }
}

void BinarySearchTree::traverse (BSTNode* T, order tt) {
    // input: root of tree and type of traversal from among PRE, IN and POST
    if (tt == PRE) {
        cout << T << endl;
        if (T -> left != NULL) {
            traverse(T -> left,tt);
        }
        if (T -> right != NULL) {
            traverse(T -> right,tt);
        }
    }
    else if (tt == IN) {
        if (T -> left != NULL) {
            traverse(T -> left,tt);
        }
        cout << T << endl;
        if (T -> right != NULL) {
            traverse(T -> right,tt);
        }
    }
    else if (tt == POST) {
        if (T -> left != NULL) {
            traverse(T -> left,tt);
        }
        if (T -> right != NULL) {
            traverse(T -> right,tt);
        }
        cout << T << endl;
    }
}

ll BinarySearchTree::height(BSTNode *T) {
    // input: root of tree
    if (T -> left == NULL && T -> right == NULL) {
        return 0;
    }
    else if (T -> right == NULL) {
        return 1 + height(T -> left);
    }
    else if (T -> left == NULL) {
        return 1 + height(T -> right);
    }
    return max(1 + height(T -> left),1 + height(T -> right));
}

// ------------------------------- Suffix Trie -----------------------------

Trie::Trie () {
    count = 0;
    nodes = map<char,Trie*>();
}

bool Trie::find(Trie* T, char c) {
    // input: root of tree and char to find
    return ((T -> nodes).find(c) != (T -> nodes).end());
}

void Trie::insert(string s) {
    // input: string to insert
    Trie* ptr = this;
    for (auto c: s) {
        if (!find(ptr,c)) {
            (ptr -> nodes)[c] = new Trie();
        }
        ptr = (ptr -> nodes)[c];
        (ptr -> count)++;
    }
}

bool Trie::checkPrefix(string s) {
    // input: string to check
    Trie* ptr = this;
    for (ll i = 0; i < s.length(); i++) {
        if (!find(ptr,s[i])) {
            if (i == s.length() - 1) {
                (ptr -> nodes)[s[i]] = NULL;
            }
            else {
                (ptr -> nodes)[s[i]] = new Trie();
            }
        }
        else if ((ptr -> nodes)[s[i]] == NULL or i == s.length() - 1) {
            return true;
        }
        ptr = (ptr -> nodes)[s[i]];
    }
    return false;
}

ll Trie::countPrefix(string s) {
    // input: prefix to match
    bool found = true;
    Trie* ptr = this;
    for (auto c: s) {
        if (find(ptr,c)) {
            ptr = (ptr -> nodes)[c];
        }
        else {
            found = false;
            break;
        }
    }
    if (found) {
        return ptr -> count;
    }
    return 0;
}

// ------------------------------- Heap -----------------------------

void swap (int &x, int &y) {
    int temp = x;
    x = y;
    y = temp;
}

Heap::Heap (int capacity) {
    maxSize = capacity;
    n = 0;
    H = new int[maxSize];
};

int Heap::parent (int i) {
    return (i - 1) / 2;
}

int Heap::left (int i) {
    return 2 * i + 1;
}

int Heap::right (int i) {
    return 2 * (i + 1);
}

void Heap::insert (int e) {
    if (n != maxSize) {
        H[n] = e;
        int i = n;
        n++;
        while (i != 0 && H[parent(i)] > H[i]) {
        swap(H[i],H[parent(i)]);
        i = parent(i);
        }
    }
}

int Heap::min () {
    if (n != 0) {
        return H[0];
    }
    return -1;
}

void Heap::Heapify (int root) {
    int l = left(root), r = right(root), s = root;
    if (l < n && H[l] < H[root]) {
        s = l;
    }
    if (r < n && H[r] < H[s]) {
        s = r;
    }
    if (s != root) {
        swap(H[root],H[s]);
        Heapify(s);
    }
}

void Heap::deleteMin () {
    if (n > 0) {
        if (n == 1) {
        H = new int[maxSize];
        n = 0;
        }
        else {
        n--;
        H[0] = H[n];
        Heapify(0);
        }
    }
}