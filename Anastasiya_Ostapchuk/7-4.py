# Anastasiya Ostapchuk
# PRLs-12
# Chapter 7, Exercise 4
# TODO: Develop the chunker that starts by putting the whole sentence in a single chunk

import nltk
grammar = r"""
  NP:
  {<.*>+}
  }<VBD|IN>+{
  """
# {<.*>+} - Chunk everything.
# }<VBD|IN.>+{ - Chink sequences of VBD and IN
whole_sent = [("the", "DT"), ("hot", "JJ"), ("shiny", "JJ"), ("day", "NN"), ("turns", "VBD"), ("into", "IN"), ("beautiful", "JJ"), ("evening", "NN")]
single = nltk.RegexpParser(grammar)
print 'A single chunk:'
print single.parse(whole_sent)
