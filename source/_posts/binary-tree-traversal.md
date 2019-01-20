---
title: Binary Tree Traversals
date: 2019-01-18 05:19:39
tags: ["data structures"]
---

The goal of this document is to present a collection of things about binary tree traversals to get the reader up to speed while solving simple tree related problems. (Be it interview prep or competitive programming or application programming; This document will try to act as a quick intro/revision)

Trees are actually a kind of graph. Hence it could be traversed/searched in two ways (most of the times, this viewpoint is not presented in textbooks because we are used to learning graphs after trees.)

1. Depth-first
2. Breadth-first

Traversal = Visiting each node of the tree exactly once
Search = Given a value, search if a node in the tree contains that value

Both Traversal and search on a tree could be done via both depth-first and breadth-first manner.

## Structure
Before solving the traversal problems, I would like to present the structure of the binary tree.

```cpp
struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode(int x): val(x), left(NULL), right(NULL) {}
};
```
This is the structure used by the [leetcode](https://leetcode.com), but it will be similar elsewhere.

## Depth-first

Here is a simple image from Wikipedia for a warm up.

![depth](https://upload.wikimedia.org/wikipedia/commons/d/d4/Sorted_binary_tree_preorder.svg)

Various types of depth-first traversal/search are

1. Pre-Order (NLR)
2. In-Order (LNR)
3. Post-Order (LRN)

Traversals are usually classified based on the order in which the root node is visited.

If the root node is visited before other nodes, then it is called PRE-order.
If the root node is visited after other nodes, then it is called POST-order.
If the root node is visited in-between the visits of other nodes, then it is called IN-order.

Usually, the order in which the children nodes are visited does not matter i.e. left before right and right before left. But most materials and implementations do left before right.

Remember that the key to solving Depth-first traversal/search would be to use a stack - call stack in case of recursion and a stack implementation in case of an iterative approach. Don't worry much about this, but this going to be your take-home of the day and if you don't get this pattern in the first go, don't be worried; you will eventually get it!

Before moving on, I would like to state a very useful resource - [Wikipedia page](https://en.wikipedia.org/wiki/Tree_traversal), that contains crisp and clear pseudocode for most of the code written here. So do check it out!

### Pre-order

The root node is visited before visiting the children.

Pre-order for the example tree given in the above figure would be FBADCEGIH

Recursive Solution

```cpp
class Solution {
private:    
    void preorder(TreeNode* node, vector<int> & vec) {
        if (node == nullptr)
            return;
        
        vec.push_back(node->val);
        preorder(node->left, vec);
        preorder(node->right, vec);
    }

public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> vec;
        preorder(root, vec);
        return vec;
    }
};
```

Iterative Solution

```cpp
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> vec;
        
        if (root == nullptr)
            return vec;
        
        stack<TreeNode*> st;
        st.push(root);
        
        while (!st.empty()) {
            auto curr = st.top();
            st.pop();
            
            // visit the node
            vec.push_back(curr->val);
            
            // Visit children
            // Push right first to visit left first.
            if (curr->right != nullptr)
                st.push(curr->right);
            
            if (curr->left != nullptr)
                st.push(curr->left);
        }
        
        return vec;
    }
};
```

### In-order

Nodes are visited in left, root and right order.

I just noticed the term "Out-order" in the [Wikipedia page](https://en.wikipedia.org/wiki/Tree_traversal), for which the nodes are visited in right, root and left order. Some textbooks do not mention this explicitly.

This traversal seems to be useful especially for binary search trees. Example, in-order traversal of a BST gives ascending order of values present in it, whereas the out-order gives the descending order.

In-order for the example tree given in the above figure would be ABCDEFGHI

Out-order for the example tree given in the above figure would be IHGFEDCBA

Recursive Solution

```cpp
class Solution {
private:
    void inorder(TreeNode* node, vector<int> & vec) {
        if (node == nullptr)
            return;
        
        inorder(node->left, vec);
        vec.push_back(node->val);
        inorder(node->right, vec);
    }
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> vec;
        inorder(root, vec);
        return vec;
    }
};
```

Iterative Solution

```cpp
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> vec;
        
        stack<TreeNode*> st;
        auto curr = root;
        
        while (!st.empty() || curr != nullptr) {
            if (curr != nullptr) {
                st.push(curr);
                curr = curr->left;
            } else {
                // Nothing is there on the left, so visit the root stored at the top of stack
                curr = st.top();
                st.pop();
                
                // visit the node
                vec.push_back(curr->val);
                
                // Give control to the right subtree, since root is visited
                curr = curr->right;
            }
        }
        
        return vec;
    }
};
```

The iterative of in-order could seem complex at first. So, I suggest you to go through videos that explain it by tracing out on a whiteboard and eventually tracing out by yourself on a piece of paper.

### Post-order

The root node is visited after visiting the children.

Post-order for the example tree given in the above figure would be ACEDBHIGF

Recursive Solution

```cpp
class Solution {
private:
    void postorder(TreeNode* node, vector<int> & vec) {
        if (node == nullptr)
            return;
        
        postorder(node->left, vec);
        postorder(node->right, vec);
        vec.push_back(node->val);
    }
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> vec;
        postorder(root, vec);
        return vec;
    }
};
```

Iterative Solution

This could be done in a couple of ways. One is to use [two stacks](https://www.youtube.com/watch?v=qT65HltK2uE) and other is to build upon the algorithm used for in-order.

To be simple, I will list out the two stacks method here.

```cpp
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> vec;
        
        if (root == nullptr)
            return vec;
        
        stack<TreeNode*> st;
        stack<TreeNode*> result;
        
        st.push(root);
        
        while (!st.empty()) {
            auto curr = st.top();
            st.pop();
            
            result.push(curr);
            
            if (curr->left != nullptr)
                st.push(curr->left);
            
            if (curr->right != nullptr)
                st.push(curr->right);
        }
        
        while (!result.empty()) {
            auto curr = result.top();
            result.pop();
            vec.push_back(curr->val);
        }
        
        return vec;
    }
};
```


## Breadth-first

Breadth-first traversal/search, on the other hand, looks like

![breadth](https://upload.wikimedia.org/wikipedia/commons/d/d1/Sorted_binary_tree_breadth-first_traversal.svg)

Answer: FBGADICEH

I love doing this so much that I often try to solve any tree problem thrown at me with this first. haha. Why? This is probably one of the algorithms where a queue is used elegantly to solve the problem and you could use this technique to solve a lot of tree problems.

This is also referred to as level-order traversal sometimes.

I would like to show a few variations of the solution. Because these variations might often help you in implementing level-order and tweaking it a bit to arrive at your custom solution.

Using one queue and get a result back as a simple list of visited values
```cpp
class Solution {
public:
    vector<int> levelOrder(TreeNode* root) {
        vector<int> vec;
        
        if (root == nullptr)
            return vec;

        queue<TreeNode*> q;
        q.push(root);
        
        while (!q.empty()) {
            auto curr = q.front();
            q.pop();
            
            vec.push_back(curr->val);
            
            if (curr->left != nullptr)
                q.push(curr->left);
            
            if (curr->right != nullptr)
                q.push(curr->right);
        }
        
        return vec;
    }
};
```

Using two queues for level-order traversal. (Not so elegant. hmmm, yeah!)
```cpp
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> vec;
        
        if (root == nullptr)
            return vec;

        queue<TreeNode*> q;
        q.push(root);
        
        while (true) {
            queue<TreeNode*> children;
            vector<int> level;

            while (!q.empty()) {
                auto curr = q.front();
                q.pop();
                
                level.push_back(curr->val);
                
                if (curr->left != nullptr)
                    children.push(curr->left);
                
                if (curr->right != nullptr)
                    children.push(curr->right);               
            }
            
            vec.push_back(level);
            
            swap(q, children);
            
            if (q.empty() && children.empty())
                break;
        }
        
        return vec;
    }
};
```

The following code does the same thing as above but avoids a `while(true)`.

```cpp
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> vec;
        
        if (root == nullptr)
            return vec;

        queue<TreeNode*> q;
        q.push(root);
        
        while (!q.empty()) {
            // capture the current level size
            auto size = q.size();

            vector<int> level;

            // pop all nodes in current level
            for (auto i = 0; i < size; ++i) {
                auto curr = q.front();
                q.pop();
                
                level.push_back(curr->val);
                
                if (curr->left != nullptr)
                    q.push(curr->left);
                
                if (curr->right != nullptr)
                    q.push(curr->right);
            }
            
            vec.push_back(level);
        }
        
        return vec;
    }
};
```

## Complexity

All the above solutions have

Time Complexity = O(N)
Space Complexity = O(N)

Because you visit every node and allocate call-stack/stack/queue for N nodes.

If you want a more space efficient solution, check out Morris Traversal.

## What to choose?
With all these solutions for solving a problem put in front of you, you might be wondering which way to choose. So here is a small piece on it.

Most of the times, go with iterative stack/queue implementation.

Recursive is clean and help you to think about a lot of tree problems. But for larger trees, you might face call-stack overflow. On the other hand, the iterative stack/queue is allocated on the heap and often times heap is big enough to accommodate your nodes.

At the same time, while interviewing don't try to solve by Morris traversal unless explicitly mentioned by the interviewer. Because it is time-consuming and often not clear. Even while writing real-world code, you might go with iterative implementation and then refactor to Morris (when you have time for it).

## Closing Notes
1. If Depth-first, think in stacks
2. If Breadth-first, think in queues
3. All solutions above have time complexity = O(N) because each node is visited once.
4. All solutions above have space complexity = O(N) because of call-stack/stack/queue space used.
5. For a more efficient (but complex) solution, check out Morris traversal.

## References

1. Tree Traversals - https://en.wikipedia.org/wiki/Tree_traversal
1. Post-order two stacks - https://www.youtube.com/watch?v=qT65HltK2uE

Image Attributions

- https://en.wikipedia.org/wiki/File:Sorted_binary_tree_preorder.svg
- https://en.wikipedia.org/wiki/File:Sorted_binary_tree_breadth-first_traversal.svg