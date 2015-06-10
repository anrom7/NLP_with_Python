 Develop a wrapper for the earley_parser so that a trace is only printed if the
# input sequence fails to parse.



#Feature-based grammars are parsed in NLTK using an Earley chart parser.
#After tokenizing the input, we import the load_parser function, which takes a
#grammar filename as input and returns a chart parser cp. Calling the parser’s
#nbest_parse() method will return a list trees of parse trees; trees will be empty
#if the grammar fails to parse the input and otherwise will contain one or more
#parse trees, depending on whether the input is syntactically ambiguous.


# this is an example when the grammar can parse the input;
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
