"""
A module for deserializing binary trees encoded with LeetCode's serializing format.
It also provides a way to visualize trees as ASCII output to the terminal.

Example:
    >>> from leetcode_trees import binarytree
    >>> tree1 = binarytree.tree_from_list(["A","B","C",None,"D",None,None,"E"])
    >>> binarytree.print_tree(tree1)
	       _______A_______
	      B___            C   
	         _D                 
	        E              
    >>> tree2 = binarytree.tree_from_list(list(range(12)))
    >>> binarytree.print_tree(tree1)
               ________0________
           ___1___           ___2___
         _3_     _4__      _5       6 
        7   8   9   10   11            
    >>> tree3 = binarytree.tree_from_list(["here", "is", "an", "example", None, "tree", "with", None, "words", "as", "node", None, "values"])
    >>> binarytree.print_tree(tree3)
                 _______here_________
            ___is                ___an_____
         example              tree_      with__
            words           as   node       values
"""
from queue import Queue


class TreeNode(object):
    """A simple node object for building binary trees."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


def tree_from_list(values):
    """Build a binary tree from a list of values.

    The list of values is interpreted to be serialized using LeetCode's format,
    using level order traversal and with None signifying path terminators.

    https://support.leetcode.com/hc/en-us/articles/360011883654-What-does-1-null-2-3-mean-in-binary-tree-representation-

    Example:
   	>>> from leetcode_trees import binarytree
	>>> tree = binarytree.tree_from_list([5,1,4,None,None,3,6])
	>>> binarytree.print_tree(tree)
	   ___5___
	  1      _4_
		3   6 
    """
    root = None
    is_root = True
    node_queue = Queue()
    for val in values:
        if not node_queue.empty():
            # If the node_queue is non-empty, parent nodes have been processed,
            # so we're not currently processing the root.
            parent_node, left_child = node_queue.get()
            is_root = False
        if val is not None:
            node = TreeNode(val=val)
            node_queue.put((node, True))
            node_queue.put((node, False))
            if is_root:
                root = node
            else:
                if left_child:
                    parent_node.left = node
                else:
                    parent_node.right = node
    return root


def print_tree(root):
    """Print a binary tree to the terminal.

    Given the root node, print a binary tree using the string
    representation of the node values.

    Examples:
               _a_
              b   c
    
             ___a___
           _b_      c_
          d   e       f
    
    The trick is to process the level order traversal backwards,
    centering the parents of the child nodes. At then end, reverse
    the order of the strings.

    h   i   j   k   l   m   n   o
     _d_     _e_     _f_     _g_
       ___b___         ___c___
           _______a______

           _______a______
       ___b___         ___c___
     _d_     _e_     _f_     _g_
    h   i   j   k   l   m   n   o
    """
    levels = level_list(root)
    lines = []
    prev_level = []
    prev_level_pos = []
    curr_level_pos = []
    for level in reversed(levels):
        line = ""
        if not prev_level:
            # Deepest level of tree
            for node in level:
                if node is not None and node.val is not None:
                    val = str(node.val)
                else:
                    val = " "
                # midpoint of string representation of val
                val_midpoint = len(val) // 2
                # If not the first element, add a separation.
                if len(line) > 0:
                    line += "   "
                # Absolute position of the node, with string centered.
                node_pos = val_midpoint + len(line)
                line += val
                # Store child's position
                curr_level_pos.append(node_pos)
        else:
            # These nodes have children.
            for i, node in enumerate(level):
                if node is not None and node.val is not None:
                    val = str(node.val)
                else:
                    val = " "
                # midpoint of string representation of val
                val_midpoint = len(val) // 2
                left_child = prev_level[i*2]
                right_child = prev_level[i*2+1]
                left_child_pos = prev_level_pos[i*2]
                right_child_pos = prev_level_pos[i*2+1]
                # Set position of parent as midpoint of the children's positions.
                node_pos = (left_child_pos + right_child_pos)//2
                # 
                while len(line) <= left_child_pos:
                    line += " "
                while len(line) < node_pos - val_midpoint:
                    if left_child is None:
                        line += " "
                    else:
                        line += "_"
                line += val
                while  len(line) < right_child_pos:
                    if right_child is None:
                        line += " "
                    else:
                        line += "_"
                curr_level_pos.append(node_pos)
        lines.append(line)
        prev_level = level
        prev_level_pos = curr_level_pos
        curr_level_pos = []
    for line in reversed(lines):
        print(line)


def level_list(root):
    """Get full level order traversal of binary tree nodes.

    Example:
	>>> from leetcode_trees import binarytree
	>>> tree = binarytree.tree_from_list([5,1,4,None,None,3,6])
	>>> binarytree.print_tree(tree)
	   ___5___
	  1      _4_
		3   6
	>>> print(binarytree.level_representation(tree))
	[[5], [1, 4], [None, None, 3, 6]]

    The list of lists contain TreeNode objects.
    """
    curr_level = [root]
    levels = [curr_level]
    next_level = []
    while True:
        for node in curr_level:
            if node is not None:
                next_level.append(node.left)
                next_level.append(node.right)
            else:
                next_level.append(None)
                next_level.append(None)
        if not all(n is None for n in next_level):
            levels.append(next_level)
            curr_level = next_level
            next_level = []
        else:
            break
    return levels
