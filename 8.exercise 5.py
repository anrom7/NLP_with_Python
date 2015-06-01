# Fedorchak V ALs - 11
#Ch.8,Ex5
#a. Write code to produce two trees, one for each reading of the phrase old men
#and women.
#b. Encode any of the trees presented in this chapter as a labeled bracketing,
#and use nltk.Tree() to check that it is well-formed. Now use draw() to display
#the tree.
#c. As in (a), draw a tree for The woman saw a man last Thursday.

import nltk
from nltk.draw.tree import draw_trees

"""
a.
"""
# Create Trees
k = nltk.Tree('NP', ['men', 'and', 'women'])
whole_tree = nltk.Tree('ADJP', ['old', k])
print "First reading of the phrase old men and women"
print whole_tree

k2 = nltk.Tree('NP', ['old', 'men'])
whole_tree2 = nltk.Tree('NP', [k2, 'and', 'women'])
print "Second reading of the phrase old men and women"
print whole_tree2

"""
b.
"""
kt = nltk.Tree('NP', ['the', 'little', 'yellow', 'dog'])
kt2 = nltk.Tree('NP', ['the', 'cat'])
kt3 = nltk.Tree('PP', ['at', kt2])
kt4 = nltk.Tree('VP', ['barked', kt3])
whole_tree3 = nltk.Tree('S', [kt, kt4])
print whole_tree3
whole_tree3.draw()

"""
c.
"""
#Sentence: The dog saw a man in the park
#Defining trees
j1 = nltk.Tree('NP', ['The', ' dog'])
j2 = nltk.Tree('NP', ['the', 'park'])
j3 = nltk.Tree('PP', ['in', j2])
j4 = nltk.Tree('NP', ['a','man', j3])
j5 = nltk.Tree('VP', ['saw', j4])
whole_tree4 = nltk.Tree('S', [j1, j5])

jr_1 = nltk.Tree('NP', ['The', ' dog'])
jr_2 = nltk.Tree('NP', ['the', 'park'])
jr_3 = nltk.Tree('PP', ['in', jr_2])
jr_4 = nltk.Tree('NP', ['a','man'])
jr_5 = nltk.Tree('VP', ['saw', jr_4, jr_3])
whole_tree5 = nltk.Tree('S', [jr_1, jr_5])
#presenting these trees, drawing them
draw_trees(whole_tree4, whole_tree5) 


