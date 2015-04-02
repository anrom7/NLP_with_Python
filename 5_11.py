# Chapter 5
# Exercise 11
# Author Svitlana Synytsia
'''
Learn about the affix tagger (type  help(nltk.AffixTagger) ). Train an affix tagger
and run it on some new text. Experiment with different settings for the affix length
and the minimum word length. Discuss your findings.
'''
import nltk
from nltk.corpus import brown
training=brown.tagged_sents(categories='news')
'''Змінна, яка запам'ятовує використання тегів у промаркованому тексті
'''
sent=('Stephane Hessel the former French Resistance fighter whose 2010 manifesto Time for Outrage inspired social protesters in Europe dies aged 95').split()
'''
Довільне речення
'''
for i in range(4): 
	affix_tagger=nltk.AffixTagger(training,affix_length=int(i),min_stem_length=int(i))
	affix_tagger.tag(sent)
	print affix_tagger.evaluate(brown.tagged_sents(categories='news'))
'''
Функція для тегування речення sent
'''
