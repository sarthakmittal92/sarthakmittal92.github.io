/**
 * @file DSA.cpp
 * @author Sarthak Mittal (200050129@iitb.ac.in)
 * @brief C++ implementations of data structures and their utility functions
 * @version 1
 * @date 2022-09-17
 */

#include <bits/stdc++.h>
/// long long int macro
#define ll long long int
/// int vector macro
#define vi vector<int>
/// long long vector macro
#define vll vector<ll>
using namespace std;

/* ------------------------------- Data Structures ---------------------------------- */

// ------------------------------- Singly Linked List -----------------------------

/**
 * @brief Singly Linked List Node class. Available member functions include
 * default constructor and initialising constructor.
 */
class SinglyLinkedListNode {

    public:

        /// data stored in the node
        ll data;

        /// pointer to the next node
        SinglyLinkedListNode* next;

        /**
         * @brief Construct a new Singly Linked List Node object
         */
        SinglyLinkedListNode () {
            data = -1;
            next = NULL;
        }

        /**
         * @brief Construct a new Singly Linked List Node object
         * @param[in] val input value for the node
         */
        SinglyLinkedListNode (ll val) {
            data = val;
            next = NULL;
        }

};

/**
 * @brief Function to print a Singly Linked List Node
 * @param[in] out standard output stream
 * @param[in] node the node to be printed
 * @return ostream&   
 */
ostream& operator<<(ostream &out, const SinglyLinkedListNode &node) {
    return out << node.data;
}

/**
 * @brief Singly Linked List class. Available member functions include
 * default constructor, insert, find, deleteVal, printer and reverse.
 */
class SinglyLinkedList {

    public:

        /// pointer to the head
        SinglyLinkedListNode *head;

        /// pointer to the tail
        SinglyLinkedListNode *tail;

        /**
         * @brief Construct a new Singly Linked List object
         */
        SinglyLinkedList () {
            head = NULL;
            tail = NULL;
        }

        /**
         * @brief Insert an element into the list
         * @param[in] data value to be inserted
         */
        void insert (ll data) {
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

        /**
         * @brief Find an element in the list
         * @param[in] data value to be found
         * @return SinglyLinkedListNode* 
         */
        SinglyLinkedListNode* find (ll data) {
            // input: data to be found
            SinglyLinkedListNode *ptr = head, *prev = NULL;
            while (ptr != NULL && ptr -> data != data) {
                prev = ptr;
                ptr = ptr -> next;
            }
            return prev;
        }

        /**
         * @brief Delete an element from list
         * @param[in] data value to be deleted
         * @return true/false
         */
        bool deleteVal (ll data) {
            // input: data to be deleted
            SinglyLinkedListNode *prev = find(data);
            if (prev -> next == NULL) {
                return false;
            }
            prev -> next -> next = prev -> next;
            return true;
        }

        /**
         * @brief Print the list
         * @param[in] sep separator string
         */
        void printer (string sep = ", ") {
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

        /**
         * @brief Reverse the list
         */
        void reverse () {
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

};

/**
 * @brief Merge two sorted linked lists
 * @param[in] list1 first list
 * @param[in] list2 second list
 * @return SinglyLinkedList 
 */
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

/**
 * @brief Doubly Linked List Node class. Available member functions include
 * default constructor and initialising constructor.
 */
class DoublyLinkedListNode {

    public:

        /// data stored in the node
        ll data;

        /// pointer to the next node
        DoublyLinkedListNode *next;

        /// pointer to the previous node
        DoublyLinkedListNode *prev;

        /**
         * @brief Construct a new Doubly Linked List Node object
         */
        DoublyLinkedListNode () {
            data = -1;
            next = NULL;
            prev = NULL;
        }

        /**
         * @brief Construct a new Doubly Linked List Node object
         * @param[in] val input value for the node
         */
        DoublyLinkedListNode (ll val) {
            data = val;
            next = NULL;
            prev = NULL;
        }

};

/**
 * @brief Function to print a Doubly Linked List Node
 * @param[in] out standard output stream
 * @param[in] node the node to be printed
 * @return ostream&   
 */
ostream& operator<<(ostream &out, const DoublyLinkedListNode &node) {
    return out << node.data;
}

/**
 * @brief Doubly Linked List class. Available member functions include
 * default constructor, insert, printer and reverse.
 */
class DoublyLinkedList {

    public:

        /// pointer to the head
        DoublyLinkedListNode *head;

        /// pointer to the tail
        DoublyLinkedListNode *tail;

        /**
         * @brief Construct a new Doubly Linked List object
         */
        DoublyLinkedList () {
            head = NULL;
            tail = NULL;
        }

        /**
         * @brief Insert an element into the list
         * @param[in] data value to be inserted 
         */
        void insert (ll data) {
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

        /**
         * @brief Print the list
         * @param[in] sep separator string
         */
        void printer (string sep = ", ") {
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

        /**
         * @brief Reverse the list
         */
        void reverse () {
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

};

// ------------------------------- Binary Search Tree -----------------------------

/**
 * @brief BST Node class. Available member functions include initialising constructor.
 */
class BSTNode {

    public:

        /// info stored in the node
        ll info;
        
        /// level of the node
        ll level;

        /// pointer to the left child
        BSTNode *left;
        
        /// pointer to the right child
        BSTNode *right;

        /**
         * @brief Construct a new BSTNode object
         * @param[in] val input value of the node
         */
        BSTNode (ll val) {
            info = val;
            level = 0;
            left = NULL;
            right = NULL;
        }

};

/**
 * @brief Function to print a BST Node
 * @param[in] out standard output stream
 * @param[in] node the node to be printed
 * @return ostream&   
 */
ostream& operator<<(ostream &out, const BSTNode &node) {
    return out << node.info;
}

/**
 * @brief BinarySearchTree class. Available member functions include
 * default constructor, insert, traverse and height.
 */
class BinarySearchTree {

    public:

        /// pointer to the root
        BSTNode *root;

        /// types of traversals
        enum order {PRE, IN, POST};

        /**
         * @brief Construct a new Binary Search Tree object
         */
        BinarySearchTree () {
            root = NULL;
        }

        /**
         * @brief Insert an element into the tree
         * @param[in] val value to be inserted 
         */
        void insert(ll val) {
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
        
        /**
         * @brief Traverse the tree
         * @param[in] T tree root pointer
         * @param tt type of traversal
         */
        void traverse (BSTNode* T, order tt) {
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

        /**
         * @brief Calculate height of the tree
         * @param[in] T tree root pointer
         * @return ll 
         */
        ll height(BSTNode *T) {
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

};

// ------------------------------- Suffix Trie -----------------------------

/**
 * @brief Trie class. Available member functions include
 * default constructor, find, insert, checkPrefix and countPrefix.
 */
class Trie {

    public:

        /// count of the string from root to leaf
        ll count;

        /// map/dictionary of nodes
        map<char,Trie*> nodes;

        /**
         * @brief Construct a new Trie object
         */
        Trie () {
            count = 0;
            nodes = map<char,Trie*>();
        }

        /**
         * @brief Find a char in a trie
         * @param[in] T trie root pointer
         * @param[in] c char to find
         * @return true/false
         */
        bool find(Trie* T, char c) {
            // input: root of tree and char to find
            return ((T -> nodes).find(c) != (T -> nodes).end());
        }

        /**
         * @brief Insert string into a trie
         * @param[in] s string to insert
         */
        void insert(string s) {
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

        /**
         * @brief Check if a string is a prefix
         * @param[in] s string to check
         * @return true/false
         */
        bool checkPrefix(string s) {
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

        /**
         * @brief Count how many strings have the given prefix
         * @param[in] s prefix to check
         * @return ll 
         */
        ll countPrefix(string s) {
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

};

// ------------------------------- Heap -----------------------------

/**
 * @brief Swap function
 * @param[in] x first value
 * @param[in] y second value
 */
void swap (int &x, int &y) {
    int temp = x;
    x = y;
    y = temp;
}

class Heap {
    /**
     * @brief Heap class. Available member functions include
     * initialising constructor, parent, left, right, insert, min, Heapify, deleteMin
     */

    int* H;
    int maxSize;
    int n;
    
    public:

        /**
         * @brief Construct a new Heap object
         * @param[in] capacity max capacity of heap
         */
        Heap (int capacity) {
            maxSize = capacity;
            n = 0;
            H = new int[maxSize];
        };

        /**
         * @brief Parent function
         * @param[in] i index of node
         * @return int
         */
        int parent (int i) {
            return (i - 1) / 2;
        }

        /**
         * @brief Left child function
         * @param[in] i index of node
         * @return int 
         */
        int left (int i) {
            return 2 * i + 1;
        }

        /**
         * @brief Right child function
         * @param[in] i index of node
         * @return int 
         */
        int right (int i) {
            return 2 * (i + 1);
        }

        /**
         * @brief Insert function
         * @param[in] e value to insert
         */
        void insert (int e) {
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

        /**
         * @brief Minimum of heap
         * @return int 
         */
        int min () {
            if (n != 0) {
                return H[0];
            }
            return -1;
        }

        /**
         * @brief Heapify function
         * @param[in] root root node
         */
        void Heapify (int root) {
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

        /**
         * @brief Delete minimum
         */
        void deleteMin () {
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

};