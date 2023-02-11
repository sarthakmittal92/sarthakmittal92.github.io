/**
 * @file DSA.h
 * @author Sarthak Mittal (200050129@iitb.ac.in)
 * @brief C++ declarations of data structures and their utility functions
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
        SinglyLinkedListNode();

        /**
         * @brief Construct a new Singly Linked List Node object
         * @param[in] val input value for the node
         */
        SinglyLinkedListNode(ll val);

};

/**
 * @brief Function to print a Singly Linked List Node
 * @param[in] out standard output stream
 * @param[in] node the node to be printed
 * @return ostream&   
 */
ostream& operator<<(ostream &out, const SinglyLinkedListNode &node);

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
        SinglyLinkedList();

        /**
         * @brief Insert an element into the list
         * @param[in] data value to be inserted
         */
        void insert(ll data);

        /**
         * @brief Find an element in the list
         * @param[in] data value to be found
         * @return SinglyLinkedListNode* 
         */
        SinglyLinkedListNode* find(ll data);

        /**
         * @brief Delete an element from list
         * @param[in] data value to be deleted
         * @return true/false
         */
        bool deleteVal(ll data);

        /**
         * @brief Print the list
         * @param[in] sep separator string
         */
        void printer(string sep);

        /**
         * @brief Reverse the list
         */
        void reverse();

};

/**
 * @brief Merge two sorted linked lists
 * @param[in] list1 first list
 * @param[in] list2 second list
 * @return SinglyLinkedList 
 */
SinglyLinkedList merge(SinglyLinkedList list1, SinglyLinkedList list2);

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
        DoublyLinkedListNode();

        /**
         * @brief Construct a new Doubly Linked List Node object
         * @param[in] val input value for the node
         */
        DoublyLinkedListNode(ll val);

};

/**
 * @brief Function to print a Doubly Linked List Node
 * @param[in] out standard output stream
 * @param[in] node the node to be printed
 * @return ostream&   
 */
ostream& operator<<(ostream &out, const DoublyLinkedListNode &node);

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
        DoublyLinkedList();

        /**
         * @brief Insert an element into the list
         * @param[in] data value to be inserted 
         */
        void insert(ll data);

        /**
         * @brief Print the list
         * @param[in] sep separator string
         */
        void printer(string sep);

        /**
         * @brief Reverse the list
         */
        void reverse();

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
        BSTNode (ll val);

};

/**
 * @brief Function to print a BST Node
 * @param[in] out standard output stream
 * @param[in] node the node to be printed
 * @return ostream&   
 */
ostream& operator<<(ostream &out, const BSTNode &node);

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
        BinarySearchTree();

        /**
         * @brief Insert an element into the tree
         * @param[in] val value to be inserted 
         */
        void insert(ll val);
        
        /**
         * @brief Traverse the tree
         * @param[in] T tree root pointer
         * @param tt type of traversal
         */
        void traverse(BSTNode* T, order tt);

        /**
         * @brief Calculate height of the tree
         * @param[in] T tree root pointer
         * @return ll 
         */
        ll height(BSTNode *T);

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
        Trie();

        /**
         * @brief Find a char in a trie
         * @param[in] T trie root pointer
         * @param[in] c char to find
         * @return true/false
         */
        bool find(Trie* T, char c);

        /**
         * @brief Insert string into a trie
         * @param[in] s string to insert
         */
        void insert(string s);

        /**
         * @brief Check if a string is a prefix
         * @param[in] s string to check
         * @return true/false
         */
        bool checkPrefix(string s);

        /**
         * @brief Count how many strings have the given prefix
         * @param[in] s prefix to check
         * @return ll 
         */
        ll countPrefix(string s);

};

// ------------------------------- Heap -----------------------------

/**
 * @brief Swap function
 * @param[in] x first value
 * @param[in] y second value
 */
void swap(int &x, int &y);

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
        Heap(int capacity);

        /**
         * @brief Parent function
         * @param[in] i index of node
         * @return int
         */
        int parent(int i);

        /**
         * @brief Left child function
         * @param[in] i index of node
         * @return int 
         */
        int left(int i);

        /**
         * @brief Right child function
         * @param[in] i index of node
         * @return int 
         */
        int right(int i);

        /**
         * @brief Insert function
         * @param[in] e value to insert
         */
        void insert(int e);

        /**
         * @brief Minimum of heap
         * @return int 
         */
        int min();

        /**
         * @brief Heapify function
         * @param[in] root root node
         */
        void Heapify(int root);

        /**
         * @brief Delete minimum
         */
        void deleteMin();

};