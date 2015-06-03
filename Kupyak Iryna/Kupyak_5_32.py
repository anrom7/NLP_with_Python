# Iryna Kupyak, PRLs-12, chapter 5, exercise 32
import nltk
help(nltk.tag.brill.demo)
nltk.tag.brill.demo(num_sents=400, max_rules=100, min_score=3, error_output='errors.out', rule_output='rules.yaml', randomize=False, train=0.3, trace=3)
nltk.tag.brill.demo(num_sents=600, max_rules=200, min_score=3, error_output='errors.out', rule_output='rules.yaml', randomize=False, train=0.3, trace=3)
#This time I changed the number of sentences (num_sents) and maximum number of rule instances to create (max_rules), first 400 sentences and 100 rules, then with 600 sentences and 100 rules, respectively.
#The greater quantity of training sentences is taken, the more accurate results can be observed ( an accuracy has improved from  0.702839 to 0.724707).
nltk.tag.brill.demo(num_sents=400, max_rules=100, min_score=3, error_output='errors.out', rule_output='rules.yaml', randomize=False, train=0.6, trace=3)
nltk.tag.brill.demo(num_sents=600, max_rules=200, min_score=3, error_output='errors.out', rule_output='rules.yaml', randomize=False, train=0.6, trace=3)
#Now I changed the parameter "train" from 0.3 to 0.6, in order to get the greater amount of the corpus for training the tagger.
#An accuracy has improved from 0.702839 to 0.741859 with 400 sentences and 100 rules, and from 0.724707 to 0.764432 for 600 sentences and 200 rules).
#I've tried to alter other parameters such as "min_score," and "trace." but it hasn't changed an accuracy a lot.
