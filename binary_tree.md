# Binary Trees

## Definition and Use Cases
By definition, a **binary tree** is a data structure in which each node has at most two children, referred to as the left child and the right child. The first node is called the "root", other nodes form "subtrees" and the last node of every subtree is called a "leaf". Certain rules apply to the data submitted to the tree, its organization determines the type of tree you are working with.

![Tree](/Final/images/linked_list.JPG "Binary tree - Image took from the BYU idaho learning modules")

When we talk about binary tree we must talk about balance, a "balanced" tree is usually achieved by maintaining the tree in such a way that the heights of the two subtrees of any node differ by at most one.

![Balanced trees](/Final/images/balanced_trees.png "Balanced trees - Image took from www.geeksforgeeks.org")

## Types of Binary Trees
There are several types of binary trees, each with its own unique properties:

* **Binary Search Tree**: Also called BST, is a binary tree in which every node obeys the following rules: 

    * The left subtree of a node contains only nodes with values lesser than the node’s value.

    * The right subtree of a node contains only nodes with values greater than the node’s value.

These properties make BSTs useful for efficient searching and sorting.

* **AVL Tress**: Is a balanced BST, meaning that the difference between the distance from any left or right child, down to a leaf is less than one.

To achieve this the tree follow a couple of rules that involve rotations between nodes that ensure a balanced tree

These are perfect for situations were frequent data lookups are necessary, but insertions and deletions are rare.

* **Segment tree**: Is a tree data structure used for storing information about intervals, or segments. It allows querying which of the stored segments contain a given point. It is, in principle, a static structure; that is, it’s a structure that cannot be modified once it’s built

![Segment trees](/Final/images/segment.png "Segment tree - Image took from www.geeksforgeeks.org")

Segment Trees are useful whenever you’re frequently working with ranges of numerical data. The most common use cases for Segment Trees are:

1. Sum all elements in a range.
2. Find the min or max value of elements in a range.
3. Update all elements in a range.

## Operations

Due to the broad variety of Binary trees, we will refer to BST from now on, as they are one of the most common implementation of binary trees

Common operations performed on BSTs include:

* **Insertion**: Adds a new node to the tree. O(log n) - Recursively search the subtrees to find the next available spot

* **Deletion**: Removes a node from the tree. O(log n) - Recursively search the subtrees to find the value and then remove it. This will require some cleanup of the adjacent nodes 

* **Search**: Finds a value in the tree. O(log n)

* **Traversal**: Visits each node in the tree in a specific order. There are two types of traversal methods:
   - **Forward**: Left -> Root -> Right. Traverses the tree from the smallest to the biggest. O(n)
   
   - **Backward**: Right -> Root -> Left. Traverses the tree from the biggest to the smallest. O(n)

## Implementation Example
* An example where a binary search tree (BST) can be particularly useful is in finding the “nth smallest” element in a set of data.

In a BST, the in-order traversal of nodes results in the nodes being visited in sorted order. Therefore, by performing an forward traversal and keeping a count of nodes visited, we can find the nth smallest element.

```python
class BST:

    class Node:

        def __init__(self, data):
       
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None
        self.count = 0

    def insert(self, data, node = None):
        if self.root is None:
            self.root = self.Node(data)
        else:
            if node is None:
                node = self.root
            if data < node.data:
                if node.left is None:
                    node.left = self.Node(data)
                else:
                    self.insert(data, node.left)
            elif data >= node.data:
                if node.right is None:  
                    node.right = self.Node(data)
                else:
                    self.insert(data, node.right)
 
        
    def nth_smallest(self, n, node=None):
        if node is None:
            node = self.root
        result = self._nth_smallest(n, node)
        if result is not None:
            self.count = 0
            return result.data
        else:
            self.count = 0
            return None

    def _nth_smallest(self, n, node):
        if node is None:
            return None
        left = self._nth_smallest(n, node.left)
        if left is not None:
            return left
        self.count += 1
        if self.count == n:
            return node
        return self._nth_smallest(n, node.right)


tree = BST()

keys = [20, 8, 22, 4, 12, 10, 14, 9]

for key in keys:
    tree.insert(key)

print(tree.nth_smallest(3))

```


## Exercise

* Based on the previous example, implement a feature that finds the nth largest element in a set of data. Essentially, now we just have to implement an backward traversal 

* [Take a look at one possible solution for this](binary_tree_exercise.py)