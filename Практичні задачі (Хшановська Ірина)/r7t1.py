
#
import nltk
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
nltk.chunk.conllstr2tree(text, chunk_types=['NP']).draw()  
text='''
a DT B-NP
merchant NN I-NP
banking NN I-NP
concern NN I-NP
. . O
'''
nltk.chunk.conllstr2tree(text, chunk_types=['NP']).draw()
#In this program we use I,O and B tags.
# A token is tagged as B if it marks the beginning of a chunk. Subsequent tokens within the chunk are tagged I.
# All other tokens are tagged O.
# The B and I tags are suffixed with the chunk type.

