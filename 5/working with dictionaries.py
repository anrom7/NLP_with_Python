# chapter 5, task
pos = {'colorless': 'ADJ', 'ideas': 'N', 'sleep': 'V', 'furiously': 'ADV'} # copied dictionary from the book
print pos.keys() #checking list of keys
d = {'cat':'N', 'black':'ADJ','dog':'N','go':'V'} # created my dictionary
print d ['go'] # checking value
d.update(pos) # united two dictionaries
print d ['colorless'] # checked value from dict 'pos' if it is in dict 'd'
print d ['xyz'] # error will apear as 'xyz' is not in any dictionary


