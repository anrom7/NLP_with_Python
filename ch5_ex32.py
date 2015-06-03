# Anna Hadzalo
#PRLS-11
#Chapter 5
#Exercise 32

import nltk
help(nltk.tag.brill.demo)
#   open help
nltk.tag.brill.demo(num_sents=2000, max_rules=200, min_score=3, error_output='errors.out',
rule_output='rules.yaml', randomize=False, train=0.5, trace=3)                 
# duration 25sec with train=0.5
nltk.tag.brill.demo(num_sents=2000, max_rules=200, min_score=3, error_output='errors.out',
rule_output='rules.yaml', randomize=False, train=0.8, trace=3)
# duration 28sec with train=0.8
nltk.tag.brill.demo(num_sents=2000, max_rules=200, min_score=3, error_output='errors.out',
rule_output='rules.yaml', randomize=False, train=1, trace=3)
#duration 32sec with train=1
#the more meaning we have for train the less speed of processing 
