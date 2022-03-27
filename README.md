# leetcode-trees
LeetCode-style binary tree deserializer and ASCII tree visualizer.

LeetCode uses a serialized format to represent binary trees using level order traversal where `None` values indicate path terminators (i.e. that no node is present in this possible child location).

This package provides a function `leetcode_trees.binarytree.tree_from_list` which builds a tree from a serialized list of node values and returns the root. This root node can then be used as inputs to functions expecting a standard tree representation with nodes `node` whose children are accessed using `node.left` and `node.right`, and whose value is stored in `node.val`.

This package also includes a simple ASCII-based binary tree visualizer which prints trees to the terminal.

## Example
```
>>> from leetcode_trees import binarytree
>>> tree = binarytree.tree_from_list(list(range(14)))
>>> binarytree.print_tree(tree)
       ________0_________
   ___1___           ____2____
 _3_     _4__      _5__      _6 
7   8   9   10   11   12   13    
>>> tree2 = binarytree.tree_from_list(['A','B','C','D',None,'E',None,'F','G','H'])
>>> binarytree.print_tree(tree2)
       _______A_______
   ___B            ___C   
 _D_             _E         
F   G           H            
>>> tree3 = binarytree.tree_from_list(["you","can","also","have","node","values","with","longer","string",None,"representations"])
>>> binarytree.print_tree(tree3)
                _____________you______________
        ______can______                    _also__
    _have___         node____            values  with
longer   string       representations                
>>> tree4 = binarytree.tree_from_list(['A','B',None,None,'C','D','E','F'])
>>> binarytree.print_tree(tree4)
               _______________A               
              B_______                                
                   ___C___                                
                 _D       E                                 
                F                             
```

## Installation

### Recommended - Install Using pip
```
pip install git+https://github.com/cflamant/leetcode-trees.git
```
Alternatively, you can download the repository and copy the directory `leetcode_trees` into the directory you are working in.
