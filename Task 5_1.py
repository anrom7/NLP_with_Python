
#TASK 5.1


import nltk
hd_ln=nltk.word_tokenize("SOVIET VIRGIN LANDS SHORT OF GOAL AGAIN")
nltk.pos_tag(hd_ln)
"""
divide sentence into words and tag them
"""
for i in hd_ln:
	if len(i)>=2:
		para=i[:2]
		if para[0][1].startswith('J') and para[1][1].startswith('V'):
			print(para)
"""
Cicle determines parts of speech to tag them correctly
"""
