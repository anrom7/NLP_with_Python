import nltk
tokens = 'Kim likes children'.split()
from nltk import load_parser
cp = load_parser('grammars/book_grammars/feat0.fcfg', trace=2)
trees = cp.nbest_parse(tokens)
for tree in trees:
    print tree
    
# but when the grammar can't parse the sentence, the tree will be empty
# for this example I'll use another grammar "feat1.fcfg"
tokens = 'who do you claim that'.split()
from nltk import load_parser
cp = load_parser('grammars/book_grammars/feat1.fcfg')
for tree in cp.nbest_parse(tokens):
    print tree

# So we can see the empty line, and we have no errors, because the grammar is correct.
