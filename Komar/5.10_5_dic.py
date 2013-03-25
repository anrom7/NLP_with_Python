#Komar Mariia ALs-11 chapter_5 Ex_5
#Using the Python interpreter in interactive mode, experiment with the dictionary. Create a dictionary d, and add some entries. What happens whether you try access a non-existent entry, e.g., d['xyz']?

import nltk
from nltk.corpus import brown 
d = {'charming': 'ADJ', 'home': 'N', 'go': 'V', 'slowly': 'ADV'} # add new words to the dictionary 
print d ['xvz'] #access a non-existent entry d['xyz']
