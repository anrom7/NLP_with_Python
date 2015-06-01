##Viktoriia Palianytsia, AL-11, chapter 8, task 4
import nltk
from nltk.corpus import treebank# import Tree
parsed_sents = treebank.parsed_sents()
parsed_sents[3]
print parsed_sents[3]# print tree
type(parsed_sents[3])
from nltk import Tree
help(Tree)#Help on class Tree in module nltk.tree
parsed_sents[3].draw()# we can see the tree
parsed_sents[3][0][0]
parsed_sents[3][0][0]
parsed_sents[3].node# access to the node (main S)
for i in parsed_sents[3]:i.node # output of the node
for i in parsed_sents[3]:i.leaves# access to the leaves
print i.leaves# output of the leaves
for i in parsed_sents[3].productions():# different types of rules
	print i# print rules for grammar
for i in parsed_sents[3].productions():
	print i.rhs(), i.lhs()# print the right or left part of the rules
for i in parsed_sents[3].productions():
	print i.is_nonlexical# we can see bound method Production and nonlexical rules	
# With the help of function (help(Tree)) we can work with variety of other useful methods.
# which can help us to get access to the Tree.
