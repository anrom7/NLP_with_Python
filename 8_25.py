# Chapter 8
# Exercise 25
# Author Svitlana Synytsia
'''
Download several electronic books from Project Gutenberg. Write a program to
scan these texts for any extremely long sentences. What is the longest sentence you
can find? What syntactic construction(s) are responsible for such long sentences?
'''
# This program scans four text from Gutenberg for extremely long sentence.
# The longest Sentence has 136 words.
# This long sentence  has a following syntactic structure:
# S what S and S; S ans S that S: S and S and S and S; S that S and S that S.


import nltk
from nltk.corpus import gutenberg
sents=gutenberg.sents('bryant-stories.txt', 'austen-emma.txt')
max_len=max([len(s) for s in sents])
max_sent=[s for s in sents if len(s)==max_len]
print 'Max Len Sent:', max_sent
print 'Len of Max Sent:', max_len
