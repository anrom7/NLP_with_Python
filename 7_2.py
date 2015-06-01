#Anna Karbivska, ALs-11
#7.9.2
#Write a tag pattern to match noun phrases containing plural head nouns, e.g.,
#many/JJ researchers/NNS, two/CD weeks/NNS, both/DT new/JJ positions/NNS. Try
#to do this by generalizing the tag pattern that handled singular noun phrases.

import nltk, re, pprint
sentence = [("Many","JJ"), ("researchers","NNS"), ("developed","VBD "), ("both","DT"),
            ("new","JJ"), ("positions","NNS"), ("two","CD"), ("weeks","NNS"), ("ago","RB")]#create sentence
grammar = "NP: {<DT>*<CD>*<JJ>*<NN.*>+}" #create ragular expression
cp = nltk.RegexpParser(grammar) #create a chunk parser test it on our example sentence
result = cp.parse(sentence)#test chunk parser on my sentence
print result #print result
