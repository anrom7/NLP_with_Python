#Chapter 5
#Exercise 11
#Author Sofiya Zaliska ALs-11, 30.03.2015
#Learn about the affix tagger (type help(nltk.AffixTagger)). Train an affix tagger
#and run it on some new text. Experiment with different settings for the affix length
#and the minimum word length. Discuss your findings.
import nltk  
from nltk.corpus import brown #��������� ����������� ������
>>> help (nltk.AffixTagger) #��������� ���� �������� ��� AffixTagger
Help on class AffixTagger in module nltk.tag.sequential:

class AffixTagger(ContextTagger, yaml.YAMLObject)
 |  A tagger that chooses a token's tag based on a leading or trailing
 |  substring of its word string.  (It is important to note that these
 |  substrings are not necessarily "true" morphological affixes).  In
 |  particular, a fixed-length substring of the word is looked up in a
 |  table, and the corresponding tag is returned.  Affix taggers are
 |  typically constructed by training them on a tagged corpus.
 |  
 |  Construct a new affix tagger.
 |  
 |  :param affix_length: The length of the affixes that should be
 |      considered during training and tagging.  Use negative
 |      numbers for suffixes.
 |  :param min_stem_length: Any words whose length is less than
 |      min_stem_length+abs(affix_length) will be assigned a
 |      tag of None by this tagger.
 |  
 |  Method resolution order:
 |      AffixTagger
 |      ContextTagger
 |      SequentialBackoffTagger
 |      nltk.tag.api.TaggerI
 |      yaml.YAMLObject
 |      __builtin__.object
 |  
 |  Methods defined here:
 |  
 |  __init__(self, train=None, model=None, affix_length=-3, min_stem_length=2, backoff=None, cutoff=0, verbose=False)
 |  
 |  context(self, tokens, index, history)
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  yaml_tag = '!nltk.AffixTagger'
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from ContextTagger:
 |  
 |  __repr__(self)
 |  
 |  choose_tag(self, tokens, index, history)
 |  
 |  size(self)
 |      :return: The number of entries in the table used by this
 |          tagger to map from contexts to tags.
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from SequentialBackoffTagger:
 |  
 |  tag(self, tokens)
 |  
 |  tag_one(self, tokens, index, history)
 |      Determine an appropriate tag for the specified token, and
 |      return that tag.  If this tagger is unable to determine a tag
 |      for the specified token, then its backoff tagger is consulted.
 |      
 |      :rtype: str
 |      :type tokens: list
 |      :param tokens: The list of words that are being tagged.
 |      :type index: int
 |      :param index: The index of the word whose tag should be
 |          returned.
 |      :type history: list(str)
 |      :param history: A list of the tags for all words before *index*.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from SequentialBackoffTagger:
 |  
 |  backoff
 |      The backoff tagger for this tagger.
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from nltk.tag.api.TaggerI:
 |  
 |  batch_tag(self, sentences)
 |      Apply ``self.tag()`` to each element of *sentences*.  I.e.:
 |      
 |          return [self.tag(sent) for sent in sentences]
 |  
 |  evaluate(self, gold)
 |      Score the accuracy of the tagger against the gold standard.
 |      Strip the tags from the gold standard text, retag it using
 |      the tagger, then compute the accuracy score.
 |      
 |      :type gold: list(list(tuple(str, str)))
 |      :param gold: The list of tagged sentences to score the tagger on.
 |      :rtype: float
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from nltk.tag.api.TaggerI:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  ----------------------------------------------------------------------
 |  Class methods inherited from yaml.YAMLObject:
 |  
 |  from_yaml(cls, loader, node) from yaml.YAMLObjectMetaclass
 |      Convert a representation node to a Python object.
 |  
 |  to_yaml(cls, dumper, data) from yaml.YAMLObjectMetaclass
 |      Convert a Python object to a representation node.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes inherited from yaml.YAMLObject:
 |  
 |  __metaclass__ = <class 'yaml.YAMLObjectMetaclass'>
 |      The metaclass for YAMLObject.
 |  
 |  yaml_dumper = <class 'yaml.dumper.Dumper'>
 |  
 |  
 |  yaml_flow_style = None
 |  
 |  yaml_loader = <class 'yaml.loader.Loader'>

training=brown.tagged_sents(categories='news') #�����, ��� �����'����� ������������ ���� � ��� �������������� �����
sent=('Stephane Hessel the former French Resistance fighter whose 2010 manifesto Time for Outrage inspired social protesters in Europe dies aged 95').split() #�������, ��� ������ ���������������
for i in range(4): #������������ AffixTagger � ������ ���������� affix_length �� min_stem_length
    affix_tagger=nltk.AffixTagger(training,affix_length=int(i),min_stem_length=int(i))
    affix_tagger.tag(sent)
    print affix_tagger.evaluate(brown.tagged_sents(categories='news'))

        
[('Stephane', None), ('Hessel', None), ('the', 'AT'), ('former', 'AP'), ('French', 'JJ'), ('Resistance', None), ('fighter', None), ('whose', 'WP$'), ('2010', None), ('manifesto', None), ('Time', 'NN-TL'), ('for', 'IN'), ('Outrage', None), ('inspired', 'VBN'), ('social', 'JJ'), ('protesters', None), ('in', 'IN'), ('Europe', 'NP'), ('dies', 'VBZ'), ('aged', 'VBN'), ('95', 'CD')]
0.934900650397
[('Stephane', 'NP'), ('Hessel', 'NP'), ('the', 'AT'), ('former', 'IN'), ('French', 'NP'), ('Resistance', 'NP'), ('fighter', 'IN'), ('whose', 'BEDZ'), ('2010', 'CD'), ('manifesto', 'NN'), ('Time', 'AT'), ('for', 'IN'), ('Outrage', 'NP'), ('inspired', 'IN'), ('social', 'NN'), ('protesters', 'NN'), ('in', 'IN'), ('Europe', 'NP'), ('dies', 'NN'), ('aged', 'CC'), ('95', 'CD')]
0.351472840464
[('Stephane', 'NN-TL'), ('Hessel', 'NP'), ('the', None), ('former', 'CD'), ('French', 'NP'), ('Resistance', 'NP'), ('fighter', 'OD'), ('whose', 'WDT'), ('2010', 'JJ'), ('manifesto', 'NN'), ('Time', 'NP'), ('for', None), ('Outrage', 'JJ-TL'), ('inspired', 'NN'), ('social', 'DTI'), ('protesters', 'NN'), ('in', None), ('Europe', 'NP'), ('dies', 'NN'), ('aged', 'IN'), ('95', None)]
0.235704198739
[('Stephane', 'NP'), ('Hessel', 'NP'), ('the', None), ('former', 'JJ'), ('French', 'NP'), ('Resistance', 'NN-TL'), ('fighter', 'VBG'), ('whose', None), ('2010', None), ('manifesto', 'NN'), ('Time', None), ('for', None), ('Outrage', 'NNS-HL'), ('inspired', 'NN'), ('social', 'JJ'), ('protesters', 'NN'), ('in', None), ('Europe', 'NP'), ('dies', None), ('aged', None), ('95', None)]
0.166119696879

