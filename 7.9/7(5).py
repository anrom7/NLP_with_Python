
# Write a tag pattern to cover noun phrases.
# Add patterns to the grammar.Test the work with sentence of your own devising.

import nltk
grammar = r"""NP:{<DT|NN>?<VBG><NN>}"""
#Setting grammar.
sentence = [("the","DT"),("receiving","VBG"),("end","NN"),(",",","),
           ("assistant","NN"),("managing","VBG"),("editor","NN")]
chunk_parser = nltk.RegexpParser(grammar)
print chunk_parser.parse(sentence)
text = nltk.word_tokenize("Freedom will give your nail color a whole new lease on life")
sentence = nltk.pos_tag(text)
# Sentence of my own devising.
chunk_parser = nltk.RegexpParser(grammar)
print chunk_parser.parse(sentence)
# Results
