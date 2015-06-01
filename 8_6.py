# Anna Karbivska, ALs-11
# 8.9.6
#Write a recursive function to traverse a tree and return the depth of the tree, such
#that a tree with a single node would have depth zero. (Hint: the depth of a subtree
#is the maximum depth of its children, plus one.)
import nltk
k = nltk.Tree (' (S (NP Ann) (VP cought (NP flu)))')
def traverse (k):
    try:                   # building a recursive funtion
        k.node
    except  Attribute Error :
        print k,
    else:
        print '(', k.node,
        for child in k:
               traverse(child) # traversing a treebank 
        print ')',
print k.height()  # output
nltk.Tree.draw (k)
