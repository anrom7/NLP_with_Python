# Iryna Kupyak, PRLs-12, chapter 7, exercise 1

# The most widespread file representation uses IOB tags. In this scheme, each token is tagged with one of three special
# chunk tags, I (inside), O (outside), or B (begin).
# A token is tagged as B if it marks the beginning of a chunk. Subsequent tokens within the chunk are tagged I.
# All other tokens are tagged O.
# The B and I tags are suffixed with the chunk type, e.g., B-NP, INP.
# Of course, it is not necessary to specify a chunk type for tokens that appear outside a chunk, so these are just labeled O.
# If we used only I and O tags we would meet the problem with the merges of chunks.
# B-tag marks the beggining of chunk, if we didn't use this tag we wouldn't see the beggining of the second consecutive chunk. 

import nltk
#Adding the text
text = '''
he PRP B-NP
accepted VBD B-VP
the DT B-NP
position NN I-NP
of IN B-PP
vice NN B-NP
chairman NN I-NP
of IN B-PP
Carlyle NNP B-NP
Group NNP I-NP
, , O
a DT B-NP
merchant NN I-NP
banking NN I-NP
concern NN I-NP
. . O
'''
nltk.chunk.conllstr2tree(text, chunk_types=['NP']).draw() # A tree representation of chunk structure
# text only with I and O tags 
text='''
a DT B-NP
merchant NN I-NP
banking NN I-NP
concern NN I-NP
. . O
'''
nltk.chunk.conllstr2tree(text, chunk_types=['NP']).draw() # A tree representation of chunk structure

