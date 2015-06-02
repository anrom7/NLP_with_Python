#Chapter 5
#Exercise 6
#Author Sofiya Zaliska ALs-11, 30.03.2015
#Try deleting an element from a dictionary d, using the syntax del d['abc']. Check
#that the item was deleted.
d={}#Creating empty dictionary
d['cat']='NN'#adding words to dictionary
d['dog']='NN'
d['run']='V'
d['abc']='LL'
print d # show dictionary
{'abc': 'LL', 'run': 'V', 'dog': 'NN', 'cat': 'NN'}
del d['abc']# delete word'abc' from dictionary d
print d # checks if the word is deleted
{'run': 'V', 'dog': 'NN', 'cat': 'NN'}


