# Chapter 7
# Exercise 4
# Author Synytsia Svitlana
'''
An early definition of chunk was the material that occurs between chinks. Develop
a chunker that starts by putting the whole sentence in a single chunk, and
then does the rest of its work solely by chinking. Determine which tags (or tag
sequences) are most likely to make up chinks with the help of your own utility
program. Compare the performance and simplicity of this approach relative to a
chunker based entirely on chunk rules.
'''
# ����������� �������, �� ���������� ����� �������� � ������� �����

import nltk 
grammar = r"""
  NP:
  {<.*>+}
  }<VBD|IN>+{
  """
whole_sent = [("the", "DT"), ("shiny", "JJ"), ("hot", "JJ"), ("weather", "NN"), ("changes", "VBD"), ("into", "IN"), ("suffering", "NN"), ("for", "IN"), ("us", "PRP")]
single = nltk.RegexpParser(grammar)
print 'A single chunk:  ', single.parse(whole_sent)



