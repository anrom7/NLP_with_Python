#Chapter 7
#Exercise 1
#Author Sofiya Zaliska ALs-11
#The IOB format categorizes tagged tokens as I, O, and B. Why are three tags
#necessary? What problem would be caused if we used I and O tags exclusively?
# The most widespread file representation uses IOB tags. In this scheme, each token is tagged with one of three special
# chunk tags, I (inside), O (outside), or B (begin).
# A token is tagged as B if it marks the beginning of a chunk. Subsequent tokens within the chunk are tagged I.
# All other tokens are tagged O.
# The B and I tags are suffixed with the chunk type, e.g., B-NP, INP.
# Of course, it is not necessary to specify a chunk type for tokens that appear outside a chunk, so these are just labeled O.
# If we used only I and O tags we would meet the problem with the merges of chunks.
# B-tag marks the beggining of chunk, if we didn't use this tag we wouldn't see the beggining of the second consecutive chunk.
import nltk
# adding text (information in a file)
text='''
He PRP B-NP
saw VBD O
the DT B-NP
white JJ I-NP
cat NN I-NP
'''
nltk.chunk.conllstr2tree(text, chunk_types=['NP']).draw() # building a tree representation from the string
# text only with I and O tags 
text='''
cat NN I-NP
. . O
'''
nltk.chunk.conllstr2tree(text, chunk_types=['NP']).draw() # building a tree representation from the string
