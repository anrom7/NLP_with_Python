#vezdenko julia al-12 task 4 chapter 7
# Ddeveloping the chunker that starts by putting the whole sentence in a single chunk

import nltk
grammar = r"""
  NP:
  {<.*>+}
  }<VBD|IN>+{
  """
whole_sent = [("the", "DT"), ("shiny", "JJ"), ("hot", "JJ"), ("weather", "NN"), ("changes", "VBD"), ("into", "IN"), ("suffering", "NN"), ("for", "IN"), ("us", "PRP")]
single = nltk.RegexpParser(grammar)
print 'A single chunk:  ', single.parse(whole_sent)
