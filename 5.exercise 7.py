Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import nltk
>>> # d1 - dictionary
>>> # d2 - dictionary # 2
>>> d1 = dict( dog = 'N', go ='V', red = 'ADJ', fast = 'ADV')
>>> d2 = dict(cat ='N', jump ='V', violet = 'ADJ', hardly = 'ADV',  get ='V', pretty = 'ADJ', badly = 'ADV')
>>> d1.update(d2)
>>> d1
{'cat': 'N', 'badly': 'ADV', 'pretty': 'ADJ', 'dog': 'N', 'violet': 'ADJ', 'go': 'V', 'red': 'ADJ', 'jump': 'V', 'hardly': 'ADV', 'fast': 'ADV', 'get': 'V'}
>>> 
