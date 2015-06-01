# Anna Karbivska ALs-11
# 5.10.5
#Using the Python interpreter in interactive mode, experiment with the dictionary examples in this chapter. Create a dictionary d, and add some entries. What happens whether you try to access a non-existent entry, e.g., d['xyz']?
>>> import nltk
>>> d={'book' : 'paper', 'phone' : 'door'} # dictionary d, and add some entries
>>> d['tea'] = 'drink'# adding new value
>>> print d ['xyz']

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print d ['xyz']
KeyError: 'xyz'
>>> # error we got: KeyError: 'xyz'
