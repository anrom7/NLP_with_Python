# Categorizing and Tagging Words.
# Pokotylo Olena ALs-11
# 5.10 (exercise 27)
# Inspect the confusion matrix for the bigram tagger t2 defined in 5, and identify one or more sets of tags to collapse. Define a dictionary to do the mapping, and evaluate the tagger on the simplified data.
>>> import nltk
>>> from nltk.corpus import brown
>>> brown_tagged_sents = brown.tagged_sents(categories='movies')

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    brown_tagged_sents = brown.tagged_sents(categories='movies')
  File "C:\Python27\lib\site-packages\nltk\corpus\reader\tagged.py", line 211, in tagged_sents
    self, self._resolve(fileids, categories), simplify_tags)
  File "C:\Python27\lib\site-packages\nltk\corpus\reader\tagged.py", line 191, in _resolve
    return self.fileids(categories)
  File "C:\Python27\lib\site-packages\nltk\corpus\reader\api.py", line 337, in fileids
    raise ValueError('Category %s not found' % categories)
ValueError: Category movies not found
>>> brown_tagged_sents = brown.tagged_sents(categories='news')
>>> brown_sents = brown.sents(categories='news')
>>> train_sents = brown_tagged_sents[:1000]
>>> test_sents = brown_tagged_sents[1000:1200]
>>> t0 = nltk.DefaultTagger('NN')
>>> t1 = nltk.UnigramTagger(train_sents, backoff=t0)
>>> t2 = nltk.BigramTagger(train_sents, backoff=t1)
>>> test_tags = [tag for sent in brown.sents(categories='news')
	     for (word, tag) in t2.tag(sent)]
>>> gold_tags = [tag for (word, tag) in brown.tagged_words(categories='news')]
>>> cm = nltk.ConfusionMatrix(gold_tags, test_tags)
>>> mistakes=nltk.defaultdict(int)
>>> for i in range(int(len(test_tags))):
	if test_tags[i] !=gold_tags [i]:
		pair=(test_tags [i], gold_tags [i])
		if pair not in mistakes:
			mistakes[pair]+=1

			
>>> print cm.key(), '\n''List of mistakes',mistakes, '\n', 'Evaluation of the tagger t2:', t2.evaluate(test_sents)
Value key:
    0: '
    1: ''
    2: (
    3: (-HL
    4: )
    5: )-HL
    6: *
    7: *-HL
    8: ,
    9: ,-HL
   10: --
   11: .
   12: .-HL
   13: :
   14: :-HL
   15: ABL
   16: ABN
   17: ABN-HL
   18: ABX
   19: AP
   20: AP$
   21: AP-HL
   22: AP-TL
   23: AT
   24: AT-HL
   25: AT-TL
   26: BE
   27: BE-HL
   28: BED
   29: BED*
   30: BEDZ
   31: BEDZ*
   32: BEDZ-HL
   33: BEG
   34: BEM
   35: BEN
   36: BER
   37: BER*
   38: BER-HL
   39: BER-TL
   40: BEZ
   41: BEZ*
   42: BEZ-HL
   43: CC
   44: CC-HL
   45: CC-TL
   46: CD
   47: CD$
   48: CD-HL
   49: CD-TL
   50: CS
   51: CS-HL
   52: DO
   53: DO*
   54: DO-HL
   55: DOD
   56: DOD*
   57: DOZ
   58: DOZ*
   59: DT
   60: DT$
   61: DT+BEZ
   62: DT-HL
   63: DTI
   64: DTI-HL
   65: DTS
   66: DTX
   67: EX
   68: EX+BEZ
   69: FW-*
   70: FW-AT
   71: FW-AT-HL
   72: FW-AT-TL
   73: FW-CC
   74: FW-CD
   75: FW-DT
   76: FW-IN
   77: FW-IN+AT-TL
   78: FW-IN+NN
   79: FW-IN+NN-TL
   80: FW-IN-TL
   81: FW-JJ
   82: FW-JJ-TL
   83: FW-NN
   84: FW-NN-TL
   85: FW-NNS
   86: FW-PP$-NC
   87: FW-VB
   88: FW-VB-NC
   89: FW-WDT
   90: HV
   91: HVD
   92: HVD*
   93: HVD-HL
   94: HVG
   95: HVN
   96: HVZ
   97: HVZ*
   98: IN
   99: IN-HL
  100: IN-TL
  101: JJ
  102: JJ-HL
  103: JJ-NC
  104: JJ-TL
  105: JJR
  106: JJR-HL
  107: JJR-NC
  108: JJR-TL
  109: JJS
  110: JJS-TL
  111: JJT
  112: JJT-HL
  113: MD
  114: MD*
  115: MD*-HL
  116: MD+HV
  117: MD-HL
  118: MD-TL
  119: NN
  120: NN$
  121: NN$-HL
  122: NN$-TL
  123: NN-HL
  124: NN-NC
  125: NN-TL
  126: NN-TL-HL
  127: NNS
  128: NNS$
  129: NNS$-HL
  130: NNS$-TL
  131: NNS-HL
  132: NNS-TL
  133: NNS-TL-HL
  134: NP
  135: NP$
  136: NP$-TL
  137: NP+BEZ
  138: NP-HL
  139: NP-TL
  140: NP-TL-HL
  141: NPS
  142: NPS$
  143: NPS$-TL
  144: NPS-HL
  145: NPS-TL
  146: NR
  147: NR$
  148: NR$-TL
  149: NR-HL
  150: NR-TL
  151: OD
  152: OD-HL
  153: OD-TL
  154: PN
  155: PN$
  156: PN+HVZ
  157: PN-HL
  158: PP$
  159: PP$$
  160: PP$-TL
  161: PPL
  162: PPLS
  163: PPO
  164: PPS
  165: PPS+BEZ
  166: PPS+BEZ-HL
  167: PPS+HVZ
  168: PPS+MD
  169: PPSS
  170: PPSS+BEM
  171: PPSS+BER
  172: PPSS+HV
  173: PPSS+HVD
  174: PPSS+MD
  175: PPSS-HL
  176: QL
  177: QL-TL
  178: QLP
  179: RB
  180: RB$
  181: RB+BEZ
  182: RB-HL
  183: RB-TL
  184: RBR
  185: RBT
  186: RP
  187: RP-HL
  188: TO
  189: TO-HL
  190: TO-TL
  191: UH
  192: UH-TL
  193: VB
  194: VB+PPO
  195: VB-HL
  196: VB-TL
  197: VBD
  198: VBD-HL
  199: VBD-TL
  200: VBG
  201: VBG-HL
  202: VBG-TL
  203: VBN
  204: VBN-HL
  205: VBN-TL
  206: VBN-TL-HL
  207: VBZ
  208: VBZ-HL
  209: WDT
  210: WDT+BEZ
  211: WP$
  212: WPO
  213: WPS
  214: WPS+BEZ
  215: WQL
  216: WRB
  217: ``

List of mistakes defaultdict(<type 'int'>, {('NN', 'FW-*'): 1, ('IN', 'TO'): 1, ('PPS+BEZ', 'PPS+BEZ-HL'): 1, ('NN', 'FW-AT-TL'): 1, ('NN', 'PPO'): 1, ('IN', 'NN'): 1, ('IN', 'PP$'): 1, ('NN', 'WRB'): 1, ('NN', 'FW-IN+AT-TL'): 1, ('VBN', 'NR'): 1, ('NN', 'NNS$-TL'): 1, ('IN', 'IN-HL'): 1, ('JJ-TL', 'NP-TL'): 1, ('NP', 'JJ-TL'): 1, ('CS', 'DT'): 1, ('NN', 'NP'): 1, ('VBD', 'VBN-HL'): 1, ('NP', 'NP-HL'): 1, ('PPO', 'PPSS'): 1, ('AP', 'QL'): 1, ('CC', 'CC-HL'): 1, ('DO*', 'DOZ*'): 1, ('NN', 'VBZ-HL'): 1, ('IN', 'JJ-TL'): 1, ('VBD', 'NN'): 1, ('NN', 'WDT+BEZ'): 1, ('RB', 'QL'): 1, ('NN', 'FW-IN+NN-TL'): 1, ('RB', 'CS'): 1, ('NN', 'MD*'): 1, ('NNS', 'NNS-HL'): 1, ('CS', 'RB'): 1, ('NN', 'VB-HL'): 1, ('AP', 'NN'): 1, ('PP$', 'PP$-TL'): 1, ('NN', 'NP-HL'): 1, ('NN', 'PPSS+HV'): 1, ('VBD', 'VBD-HL'): 1, ('NN', 'BED*'): 1, ('JJ', 'VB'): 1, ('VB', 'NN-HL'): 1, ('IN', 'RB'): 1, ('JJ-TL', 'JJ'): 1, ('VBZ-HL', 'NNS'): 1, ('ABN', 'NN'): 1, ('NN-HL', 'NP-TL'): 1, ('VB', 'VBN'): 1, ('NN', 'CD-TL'): 1, ('NN-HL', 'NN'): 1, ('NNS', 'NNS-TL'): 1, ('RB', 'VB'): 1, ('PPSS+HVD', 'PPSS+MD'): 1, ('RB', 'JJ'): 1, ('QL', 'JJ'): 1, ('NN', 'WDT'): 1, ('NN', 'NNS$-HL'): 1, ('NN', 'NPS$-TL'): 1, ('RB', 'OD-HL'): 1, ('OD', 'OD-TL'): 1, ('NN', 'BER-TL'): 1, ('VB', 'VB-HL'): 1, (':', ':-HL'): 1, ('NN', 'RB$'): 1, ('JJ-TL', 'FW-JJ-TL'): 1, ('VBZ', 'NNS'): 1, ('DT', 'CS'): 1, ('NN', 'FW-CC'): 1, ('VBG', 'NN'): 1, ('PPSS', 'PPO'): 1, ('IN', 'CS'): 1, ('NN-TL-HL', 'NN-TL'): 1, ('VBG-HL', 'VBG'): 1, ('TO', 'TO-HL'): 1, ('NN', 'NPS-HL'): 1, ('NN', 'DTX'): 1, ('NN', 'FW-AT'): 1, ('NN', 'PN+HVZ'): 1, ('VBN-HL', 'VBD'): 1, ('NN', 'VBN-HL'): 1, ('NN', 'HVD*'): 1, ('NN-TL', 'NN-TL-HL'): 1, ('OD-TL', 'OD'): 1, ('NR-TL', 'JJ-TL'): 1, ('NN', 'RB-TL'): 1, ('AP', 'IN'): 1, ('NP-HL', 'JJ-TL'): 1, ('ABN', 'RB'): 1, ('CC', 'CC-TL'): 1, ('JJ', 'IN'): 1, ('NN', 'OD'): 1, ('NN', 'JJ'): 1, ('NN', 'JJS'): 1, ('NN', 'NR$'): 1, ('IN-HL', 'IN'): 1, ('JJR', 'VB'): 1, ('NN', 'JJR-HL'): 1, ('BEDZ', 'BEDZ-HL'): 1, ('NN', 'NPS$'): 1, ('HVD', 'HVD-HL'): 1, ('VBG-TL', 'VBG'): 1, ('ABN', 'ABN-HL'): 1, ('VBN', 'JJ'): 1, ('VBN', 'VB'): 1, ('NN', 'UH'): 1, ('NN', 'NR-HL'): 1, ('NN', 'IN'): 1, ('NN', 'FW-NN-TL'): 1, ('ABN', 'QL'): 1, ('NN', 'PPS+MD'): 1, ('NN', 'NN$-TL'): 1, ('DTI', 'DTI-HL'): 1, ('NN', 'RBR'): 1, ('NN', 'JJ-NC'): 1, ('TO', 'TO-TL'): 1, ('VBD', 'VB'): 1, ('NN', 'NPS-TL'): 1, ('VB', 'NN'): 1, ('TO', 'NPS'): 1, ('NN', 'RB+BEZ'): 1, ('JJ-TL', 'NN-TL'): 1, ('NNS', 'NN'): 1, ('NN', 'RP'): 1, ('RB', 'NN'): 1, ('PPS', 'PPO'): 1, ('NP', 'FW-IN'): 1, ('RB', 'AP'): 1, ('PPSS', 'NN'): 1, ('CS-HL', 'CS'): 1, ('JJ', 'NN'): 1, ('OD', 'NN'): 1, ('NN', 'FW-JJ-TL'): 1, ('NN', 'JJT'): 1, ('NP-TL', 'JJ'): 1, ('VB', 'JJ'): 1, ('NR', 'NN'): 1, ('NN', 'NN$-HL'): 1, ('NN', 'DT+BEZ'): 1, ('NN-TL', 'NN-HL'): 1, ('BEZ', 'BEZ-HL'): 1, ('VBN', 'NN-HL'): 1, ('EX', 'RB-HL'): 1, ('VBN-HL', 'VBN'): 1, ('WRB', 'WQL'): 1, ('CD', 'PN'): 1, ('TO', 'IN-HL'): 1, ('NN', 'FW-NNS'): 1, ('PPO', 'PPS'): 1, ('VBG', 'VBG-HL'): 1, ('NN', 'VBN-TL'): 1, ('AP', 'AP-HL'): 1, ('PPSS', 'PPSS-HL'): 1, ('NP', 'JJ'): 1, ('NN', 'PPLS'): 1, ('NP-TL', 'NN-TL'): 1, ('CS', 'QL'): 1, ('NN', 'PN$'): 1, ('EX', 'RB'): 1, ('NN', 'PN'): 1, ('NN-TL', 'NN'): 1, ('NN', 'JJ-HL'): 1, ('RB', 'IN'): 1, ('VBD', 'JJ'): 1, ('AP', 'AP-TL'): 1, ('QL', 'AP'): 1, ('CD', 'CD-TL'): 1, ('NN', 'FW-IN'): 1, ('VBD', 'VBN'): 1, ('CS', 'WPS'): 1, ('NN', 'PPL'): 1, ('NN', 'JJR-TL'): 1, ('NP', 'FW-AT-TL'): 1, ('MD', 'NN'): 1, ('QL', 'CS'): 1, ('NP', 'NN-TL'): 1, ('QL', 'ABN'): 1, ('NN', 'PPSS+BER'): 1, ('NN', 'NN-TL-HL'): 1, ('AP', 'QLP'): 1, ('PP$', 'PPO'): 1, ('JJ', 'ABL'): 1, ('NN', 'PPS+HVZ'): 1, ('NN-TL', 'NP-TL'): 1, ('JJ', 'QL'): 1, ('NN', 'VBD-TL'): 1, ('NN', 'CS'): 1, ('NN-TL-HL', 'NP'): 1, ('NN', 'NPS'): 1, ('DO', 'DO-HL'): 1, (',-HL', ','): 1, ('JJ-HL', 'RB'): 1, ('RBR', 'JJR'): 1, ('NN', 'HVZ'): 1, ('NN', 'VBG'): 1, ('PP$', 'PP$$'): 1, ('NN-TL', 'JJS'): 1, ('VB-HL', 'VB'): 1, (')-HL', ')'): 1, ('NN', 'PP$'): 1, ('NN', 'NNS-HL'): 1, ('NN', 'FW-PP$-NC'): 1, ('*', '*-HL'): 1, ('NN-TL', 'JJS-TL'): 1, ('RB', 'EX'): 1, ('JJ', 'VBN'): 1, ('NN', 'QL'): 1, ('NR', 'NR-HL'): 1, ('AT-TL', 'AT'): 1, ('NP', 'NN'): 1, ('DTX', 'CC'): 1, ('IN-TL', 'IN'): 1, ('NNS-TL', 'NNS'): 1, ('NN', 'DO*'): 1, ('CD-HL', 'CD-TL'): 1, ('CS', 'VB'): 1, ('NN-TL', 'NP-HL'): 1, ('AT', 'AT-TL'): 1, ('NNS-HL', 'NNS'): 1, ('NN', 'FW-JJ'): 1, ('OD', 'QL'): 1, ('VBN', 'NN'): 1, ('VBN', 'VBN-HL'): 1, ('NN', 'HVD'): 1, ('NN-TL', 'NP-TL-HL'): 1, ('NP', 'NN-HL'): 1, ('CC', 'IN'): 1, ('.', '.-HL'): 1, ('CD', 'OD'): 1, ('VB', 'VBD'): 1, ('(', '(-HL'): 1, (',', ',-HL'): 1, ('NN', 'VBD-HL'): 1, ('NN', 'BER*'): 1, ('NN', 'JJR-NC'): 1, ('HVD', 'HVN'): 1, ('QLP', 'RB'): 1, ('NN', 'IN-TL'): 1, ('ABL', 'RB'): 1, ('NN-TL', 'FW-NN-TL'): 1, ('NN', 'VBG-TL'): 1, ('IN', 'IN-TL'): 1, ('NN', 'PP$$'): 1, ('NN', 'NR$-TL'): 1, ('NN-HL', 'VB'): 1, ('NN', 'NN-NC'): 1, ('NN', 'VB'): 1, ('NN', 'FW-VB'): 1, ('NP-TL', 'JJ-TL'): 1, ('RB', 'AT'): 1, ('JJR', 'RBR'): 1, ('NN', 'CD-HL'): 1, ('JJ', 'RB'): 1, ('CD', 'OD-TL'): 1, ('CS', 'IN'): 1, ('QL', 'WRB'): 1, ('NN', 'PPSS'): 1, ('IN', 'VBG'): 1, ('JJ-HL', 'JJ-TL'): 1, ('MD', 'MD-HL'): 1, ('IN', 'QL'): 1, ('NN', 'CD$'): 1, ('CS', 'VB-HL'): 1, ('JJ', 'NN-TL'): 1, ('AT', 'NN'): 1, ('CD-HL', 'CD'): 1, ('PPS+HVZ', 'PPS+BEZ'): 1, ('NN', 'VBN'): 1, ('NN', '*'): 1, ('NN', 'DO'): 1, ('RB', 'OD'): 1, ('RP', 'IN'): 1, ('NP-TL', 'NP-HL'): 1, ('AP', 'JJ'): 1, ('VBZ', 'NNS-HL'): 1, ('JJ', 'JJ-TL'): 1, ('NN', 'NP+BEZ'): 1, ('NN', 'CD'): 1, ('AT', 'AT-HL'): 1, ('VBG', 'NN-HL'): 1, ('NNS', 'VBZ'): 1, ('AP', 'VB'): 1, ('NN', 'MD+HV'): 1, ('NN', 'BEZ*'): 1, ('NN', 'NP$-TL'): 1, ('NN', 'VBD'): 1, ('NN', 'DOD'): 1, ('NN-HL', 'NN-TL'): 1, ('VB', 'JJT'): 1, ('NN-TL', 'NP'): 1, ('NP', 'FW-AT-HL'): 1, ('AP', 'RBR'): 1, ('NP-TL', 'NP'): 1, ('NN', 'FW-CD'): 1, ('IN', 'RP'): 1, ('CS', 'WPO'): 1, ('RBT', 'AP'): 1, ('NN', 'NN-HL'): 1, ('CS', 'NN'): 1, ('JJS', 'NN'): 1, ('NN', 'FW-WDT'): 1, ('CD-TL', 'CD'): 1, ('NP', 'FW-IN-TL'): 1, ('ABL', 'QL'): 1, ('NN', 'NNS$'): 1, ('NN', 'JJ-TL'): 1, ('VBG', 'JJ'): 1, ('NN', 'BEZ'): 1, ('TO', 'IN-TL'): 1, ('NN', 'NP$'): 1, ('NN', 'NN$'): 1, ('VBN', 'VBD'): 1, ('QL', 'RBR'): 1, ('NN', 'PPS+BEZ'): 1, ('JJ-HL', 'JJ'): 1, ('WRB', 'RB'): 1, ('AT', 'RB'): 1, ('PN', 'PN-HL'): 1, ('CS', 'JJ'): 1, ('CD', 'NP'): 1, ('JJ', 'NP'): 1, ('NN', 'EX+BEZ'): 1, ('NN', 'VBG-HL'): 1, ('NN', 'JJR'): 1, ('NN', 'NN-TL'): 1, ('VBZ-HL', 'VBZ'): 1, ('TO-HL', 'IN-HL'): 1, ('JJS', 'VB'): 1, ('JJ', 'AP'): 1, ('NN', 'VB+PPO'): 1, ('NN', 'PPSS+MD'): 1, ('NN', 'HVG'): 1, ('NN', 'RBT'): 1, ('NNS', 'VBZ-HL'): 1, ('QL', 'RB'): 1, ('NN', 'NNS-TL'): 1, ('PN', 'CD'): 1, ('RB', 'CC'): 1, ('NN', 'AP$'): 1, ('NN', 'RB-HL'): 1, ('NN', 'AP'): 1, ('NN', 'ABN'): 1, ('RP', 'RP-HL'): 1, ('JJ', 'NR'): 1, ('NN-TL', 'NR'): 1, ('NN', 'FW-IN+NN'): 1, ('MD-HL', 'MD-TL'): 1, ('AT', 'FW-IN'): 1, ('NN', 'NR'): 1, ('NN', 'WPS+BEZ'): 1, ('AP', 'QL-TL'): 1, ('NN', 'OD-TL'): 1, ('NN', 'NP-TL'): 1, ('CD', 'CD-HL'): 1, ('NN', 'HVZ*'): 1, ('NN', 'BER'): 1, ('WPS', 'CS'): 1, ('NP', 'NP-TL'): 1, (')', ')-HL'): 1, ('IN', 'JJ'): 1, ('CC-HL', 'CC'): 1, ('NN', 'VBZ'): 1, ('NN', 'FW-VB-NC'): 1, ('NN', 'FW-NN'): 1, ('JJ', 'JJ-HL'): 1, ('NN', 'MD'): 1, ('BEZ-HL', 'BEZ'): 1, ('QL', 'RBT'): 1, ('NP-HL', 'NP'): 1, ('NN', 'RB'): 1, ('NN', 'VB-TL'): 1, ('TO', 'IN'): 1, ('AT-HL', 'AT'): 1, ('CC-TL', 'CC'): 1, ('RB', 'RB-HL'): 1, ('JJS-TL', 'NN-TL'): 1, ('JJR', 'QL'): 1, ('AP-HL', 'AP'): 1, ('WRB', 'QL'): 1, ('NN', 'CC'): 1, ('NN', 'NNS'): 1, ('JJ', 'NN-HL'): 1, ('JJ-TL', 'NP'): 1, ('OD', 'RB'): 1, ('AP', 'RB'): 1, ('VB', 'JJS'): 1, ('VBG', 'CS'): 1, ('MD-HL', 'MD'): 1, ('NN', 'JJT-HL'): 1, ('JJ-TL', 'NR-TL'): 1}) 
Evaluation of the tagger t2: 0.721908207099
>>> 
