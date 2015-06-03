# Anna Hadzalo
#PRLS-11
#Chapter 8
# Task 20


import nltk
from nltk.draw.tree import draw_trees
tree1 = nltk.Tree('NP', ['Mary']) # Створюємо перше дерево
tree2 = nltk.Tree('NP', ['the', 'pictures']) # Створюємо друге дерево
tree3 = nltk.Tree('VP', ['painted', tree2]) # Створюємо третє дерево
draw_trees(tree1, tree2, tree3) # Виводимо на екран всі три створені дерева
