# Categorizing and Tagging Words.
# Pokotylo Olena ALs-11
# Chapter 7 (exercise 5)
import nltk
grammar = r"""
NP:{<DT|NN>?<VBG><NN>}"""# create a chunk parser.chunk determiner(DT)/noun(NN),gerund(VBG) and noun(NN) 
sentence = [("the","DT"),("receiving","VBG"),("end","NN"),(",",","), ("assistant","NN"),("managing","VBG"),("editor","NN")]
cp = nltk.RegexpParser(grammar)# result is a tree
print cp.parse(sentence)
# my own sentence
sentence = [("Jamming", "VBG"), ("too", "RB"), ("much", "RB"), ("clothing", "VBG"), ("into", "IN"), ("a", "DT"), ("washing", "VBG"), ("machine", "NN"), ("will", "MD"), ("result", "VB"), ("in", "IN"), ("disaster","NN")]
cp = nltk.RegexpParser(grammar)
print cp.parse(sentence)
# As we ca see, we can find the noun phrases that contain gerunds. in our
# last sentence I found the phrases like "a washing machine"
