'''
Binary tree is a kind of datastructure which each node
has at most of 2 branches, where left side always less
than the node itself and right side is greater
e.g.

     8
   /   \
  4    10
 / |    | 
3  6    25
    \
    7

as you see, the node '8' has 2 branches '4' on the left
and '10' on the right. The advantage of storing data like
this is for searching. Let say we need to find 25, we
can probe from the root(8) 25 is bigger, then go to the
right(10), 25 is bigger go to the right(25) then we found
it only 3 probes, compared to sorted list that we need
to probe the entire list.

search function below will try to get the node that
value matches the `value` parameter in the tree
but it's buggy now, can you fix it?
'''

node7 = {value: 7, left: None, right: None}
node6 = {value: 6, left: None, right: node7}
node3 = {value: 3, left: None, right: None}
node4 = {value: 4, left: node3, right: node6}
node25 = {value: 25, left: None, right: None}
node10 = {value: 10, left: None, right: node25}
node8 = {value: 8, left: node4, right: node10}
root = node8

def search(node, value):
    if node.value == value:
        return node
    else if (node.value < value):
        search(node, node.left)
    else if (node.value > value):
        search(node, node.right)
    
    return node.value

#search(root, 10)
#search(root, 12)
#search(node6, 6)
#search(node6, 4)
