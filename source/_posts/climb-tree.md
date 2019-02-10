---
title: So you want to climb that tree?
date: 2019-02-10 15:19:16
tags: ["data structures", "algorithms", "programming"]
---

I have been feeling a bit nervous lately that I am not skilled enough to solve tree (data-structure) problems. Not only on the interview prep side but also while writing application code. It is true! I failed to identify a problem as a tree problem while at work once and ended up writing a monstrous function that somehow got the job done. By the time I realized it was too late to implement/reimplement it. (However, the feature works! it still does :D )

So here it goes! My effort to get good at identifying and solving tree problems. In fact, this effort started quite a while back, but I guess writing this document will help me and anyone else looking to get a framework for attacking tree problems.

Also, this document is better suited for people who have already taken up a computer science course or encountered trees. If that is not you, I heavily suggest [reading through some basics](https://en.wikipedia.org/wiki/Tree_(data_structure)) about tree.

## Types

There are different types of trees. So it might be worth taking time to explore a bit on getting idea about different kind of trees.

In case of interviewing, you will often encounter these more

- Binary Tree
- Binary Search Tree
- AVL Tree

There are a [huge number of tree](https://en.wikipedia.org/wiki/List_of_data_structures#Trees) types that you could encounter while writing applications. I have noticed common occurence of N-ary trees in practice.

## Traversals

Step 1 is getting good at tree traversals. I have already done my practice in this section by writing up [this blog post](/blog/binary-tree-traversal/) and solving some problems related to them.

Key here is to know both the recursive and iterative approach for solving the traversal problems. Going top list down the set of leetcode problems here. If you could solve the below problems in both ways, you are good to go to the next level!

1. [Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)
2. [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
3. [Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)
4. [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)

ufff! You are done with it. What's next?

This is good NEWS. By this time, given a tree problem, the first question that you would ask yourself should be

```
____________________________________
/ Can a tree traversal help me solve \
\ this?                              /
------------------------------------
       \   ^__^
        \  (oo)\_______
           (__)\       )\/\
               ||----w |
               ||     ||
```

Once you are done with binary, try N-ary trees. This is gonna be so easy for you. Also this is a proof that if you get good at binary trees, you can face other kind of trees with a little confidence.

1. [N-ary Tree Preorder Traversal](https://leetcode.com/problems/n-ary-tree-preorder-traversal/)
2. No in-order available because there is no answer to "after which children will we visit the root node?"
3. [N-ary Tree Postorder Traversal](https://leetcode.com/problems/n-ary-tree-postorder-traversal/)
4. [N-ary Tree Level Order Traversal](https://leetcode.com/problems/n-ary-tree-level-order-traversal/)

These problems just vary in the way their child visitation is implemented.

```cpp
if (curr->left != nullptr)
    st.push(curr->left);

if (curr->right != nullptr)
    st.push(curr->right);

//// becomes

for (auto & child: curr->children)
    st.push(child);
```

and

```cpp
if (curr->right != nullptr)
    st.push(curr->right);

if (curr->left != nullptr)
    st.push(curr->left);

//// becomes

for (auto it = curr->children.rbegin(); it != curr->children.rend(); ++it)
    st.push(*it);
```

You could basically use this knowledge to attack on some general tree problems like the below.

1. [Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) - Supplement level order with a stack and you are done!
2. [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)  - Do a level order traversal and add the last element of each level to the result
3. [Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/) - Supplement level order traversal with a stack to capture the level order in reverse order.
4. [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) - Post-order traversal the nodes and invert if any of the child is present.
5. [Binary Tree Tilt](https://leetcode.com/problems/binary-tree-tilt/) - Post-order traversal to save the sum of subtrees in a map and pre-order traversal to compute the tilt of each node. (recursion might only need a post-order + a global variable)
6. [Binary Tree Vertical Order Traversal](https://leetcode.com/problems/binary-tree-vertical-order-traversal/) - Level order traversal with a pair<TreeNode*, int> (int contains the vertical level information) + use a map<vector<int>> to store the results.

## Depth

> The depth of a node is defined as: the number of edges between the node and the root.

Note that leetcode and some other places consider the count of nodes instead of edges while computing the depth.

1. [Maximum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/) - classic level order it. :D
2. [Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/) - Level order traversal + return the depth of the first leaf node.
3. [Maximum Depth of N-ary Tree](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/) - classic level order again :D

## Bye!

I have to abruptly end this post now. Because I am lagging a bit in stamina and I have to recharge before further attacks :D

I solved most of the above problems continuously over a Saturday. ah, that felt good. Today is Sunday and I think I should just post this out in my blog for now. I actually feel pretty good about it! My leetcode rating went from 2 to 2.5 :D (yay!)

There are still common tree problems floating around us, which I haven't listed and solved yet. (like the diameter of a binary tree). But keeping them for some other time. Until then, bye!
