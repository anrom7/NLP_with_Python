import nltk
text = nltk.word_tokenize("They wind back the clock, while we chase after the wind")
nltk.pos_tag(text)
#Here we see that They and we are PRP, pronouns; wind and chase are VBP, verbs in the Present Simple tense; back is RB, an adverb; the is DT, a Determiner; clock and wind are NN, nouns; while and after are IN, prepositions.
#In the first instance WIND   /waind/ is a verb, in the second /wind/ is a noun. The difference in pronounciation between the two words is that /waind/ features a long vowel, while /wind/ uses a short vowel.
