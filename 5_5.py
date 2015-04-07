# Author: Uliana Hentosh
Dictionary = {'concerted': 'ADJ', 'values': 'N', 'run': 'V', 'invetively': 'ADV'} # copied dictionary from the book
print (Dictionary.keys()) #checking list of keys
ABV = {'fisg':'N', 'orange':'ADJ','owl':'N','articulate':'V'} # created my dictionary
print (ABV ['articulate']) # checking value
ABV.update(Dictionary) # united two dictionaries
print (ABV ['concerted']) # checked value from dict 'Dictionary' if it is in dict 'ABV'
print (ABV ['xyz']) # error will apear as 'xyz' is not in any dictionary
