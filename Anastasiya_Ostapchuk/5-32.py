# Anastasiya Ostapchuk
# PRLs-12
# Chapter 5, Exercise 32
# TODO: Consult the documentation for the Brill tagger demo function. Experiment with the tagger by setting different values for the parameters.

import nltk
help(nltk.tag.brill.demo)
nltk.tag.brill.demo(num_sents=500, max_rules=100, min_score=3, error_output='errors.out', rule_output='rules.yaml', randomize=False, train=0.3, trace=3)
nltk.tag.brill.demo(num_sents=1000, max_rules=200, min_score=3, error_output='errors.out', rule_output='rules.yaml', randomize=False, train=0.3, trace=3)

# I changed the number of sentences (num_sents) and maximum number of rule instances to create (max_rules), first 500 sentences and 100 rules, then with 1000 sentences and 200 rules.
# The greater quantity of training sentences is taken, the more accurate results can be observed ( an accuracy has improved from  0.714776 to 0.742791).

nltk.tag.brill.demo(num_sents=500, max_rules=100, min_score=3, error_output='errors.out', rule_output='rules.yaml', randomize=False, train=0.6, trace=3)
nltk.tag.brill.demo(num_sents=1000, max_rules=200, min_score=3, error_output='errors.out', rule_output='rules.yaml', randomize=False, train=0.6, trace=3)

# I changed the parameter "train" from 0.3 to 0.6, in order to get the greater amount of the corpus for training the tagger.
# An accuracy has improved from 0.714776 to 0.752887 with 500 sentences and 100 rules, and from 0.742791 to 0.779827 for 1000 sentences and 200 rules).
# I've tried to alter other parameters such as "min_score," and "trace." but it hasn't changed an accuracy a lot.
