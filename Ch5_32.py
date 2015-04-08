#Ivanna Rurych, AL-12
#chapter 5, Ex. 32
#task:Consult the documentation for the Brill tagger demo function, using help(nltk.tag.brill.demo). Experiment with the tagger by setting different values for the parameters. Is there any trade-off between training time (corpus size) and performance?
import nltk
print(help(nltk.tag.brill.demo)) #Consult the documentation for the Brill tagger demo function
brill_demo=nltk.tag.brill.demo(num_sents=40, max_rules=35,  min_score=2, trace=5, train=0.9) # Experiment with the tagger
print (brill_demo)
