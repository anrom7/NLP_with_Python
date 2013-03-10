import nltk
train_sents = [
[('I','PRO'), ('her','PRO'), ('its','PRO'), ('my','PRO'), ('us','PRO')],
[('told','VD'), ('took','VD'), ('made','VD'), ('asked','VD')],
[('a','DET'), ('some','DET'), ('most','DET'), ('every','DET'), ('no','DET')],
[('nice','ADJ'), ('high','ADJ'), ('special','ADJ'), ('big','ADJ'), ('local','ADJ')],
[('ideas','N'), ('costs','N'), ('time','N'), ('education','N')],
]

text = 'I told a big ideas'

#if ((min_stem_length + abs(affix_length)) > word_length) then assigned_tag = None
affix_tagger = nltk.AffixTagger(train_sents, affix_length=-2, min_stem_length=0)
tags = affix_tagger.tag(nltk.word_tokenize(text))
print tags
affix_tagger = nltk.AffixTagger(train_sents, affix_length=-1, min_stem_length=2)
tags = affix_tagger.tag(nltk.word_tokenize(text))
print tags
affix_tagger = nltk.AffixTagger(train_sents, affix_length=2, min_stem_length=2)
tags = affix_tagger.tag(nltk.word_tokenize(text))
print tags
affix_tagger = nltk.AffixTagger(train_sents, affix_length=2, min_stem_length=5)
tags = affix_tagger.tag(nltk.word_tokenize(text))
print tags
