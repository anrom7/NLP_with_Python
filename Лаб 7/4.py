

import nltk
grammar = r"""
  NP:
  {<DT>?<JJ>*<NN>}
  """
whole_sent = [("the", "DT"), ("older", "JJ"), ("woman", "NN"), ("railed", "VBD"), ("at", "IN"), ("the", "DT"), ("child", "NN")]
single = nltk.RegexpParser(grammar)
print 'A single chunk:  ', single.parse(whole_sent)


