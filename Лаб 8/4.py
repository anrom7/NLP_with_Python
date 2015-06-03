
import nltk
from nltk.corpus import treebank
parsed_sents = treebank.parsed_sents()
parsed_sents[3]
print parsed_sents[3]
type(parsed_sents[3])
from nltk import Tree
help(Tree)
parsed_sents[3].draw()
parsed_sents[3][0][0]
parsed_sents[3][0][0]
parsed_sents[3].node
for i in parsed_sents[3]:i.node 
for i in parsed_sents[3]:i.leaves
print i.leaves
for i in parsed_sents[3].productions():
  print i# print rules for grammar
for i in parsed_sents[3].productions():
	print i.rhs(), i.lhs()
for i in parsed_sents[3].productions():
	print i.is_nonlexical
