# Anastasiya Ostapchuk
# PRLs-12
# Chapter 5, Exercise 7
# TODO: Create 2 dictionaries. Use the command "d1.update(d2)". What will happen?

import nltk
from nltk import *
d1={'world':'N','satellite':'N','be':'V','whole':'ADJ'}
d2={'room':'N','dance':'V','night':'N'}
# 2 dictionaries were created
print "Dictionaries before updating:"
print "d1=", d1
print "d2=", d2
d1.update(d2)
print "Dictionaries after updating:"
# The mentioned command was used
print "d1=",d1
print "d2=",d2
# "d2" wasn't changed while "d1" got new entries and keys from that dictionary
