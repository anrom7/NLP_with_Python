# vezdenko julia al-12 task9 chapter8
import nltk
grammar1 = nltk.parse_cfg(
"""
S -> NP VP
VP -> V NP | V NP PP
PP -> P NP
V -> "saw" | "ate" | "walked"
NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
Det -> "a" | "an" | "the" | "my"
N -> "man" | "dog" | "cat" | "telescope" | "park"
P -> "in" | "on" | "by" | "with"
""")

sent = "Mary saw Bob".split()
rd_parser = nltk.RecursiveDescentParser(grammar1)
for tree in rd_parser.nbest_parse(sent):
        print tree

# A production like VP -> V NP | V NP PP has a disjunction on the righthand side,
# shown by the |, and is an abbreviation for the two productions  VP -> V NP and VP -> V NP PP.
# If we parse the sentences that are more than 20 words in length using the
# grammar shown in Example 8-1, we end up with two or more trees.
# Since our grammar licenses two or more trees for these sentences,
# the sentences are said to be structurally ambiguous. 
