import nltk
from nltk import tree
from nltk.draw.tree import draw_trees
# 1 дерево
tree1 = nltk.Tree('NP', ['the', 'dog'])
# 2 дерево
tree2 = nltk.Tree('NP', ['a', 'man'])
# 3 дерево
tree3 = nltk.Tree('VP', ['saw', tree2])
# Використання ф-ї draw_trees()
draw_trees(tree1, tree2, tree3)
