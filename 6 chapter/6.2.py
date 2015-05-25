# Categorizing and Tagging Words.
# Pokotylo Olena ALs-11
# Chapter 6 (exercise 2)
# Using any of the three classifiers described in this chapter, and any features you can think of, build the best name gender classifier you can. Begin by splitting the Names Corpus into three subsets: 500 words for the test set, 500 words for the dev-test set, and the remaining 6900 words for the training set. Then, starting with the example name gender classifier, make incremental improvements. Use the dev-test set to check your progress. Once you are satisfied with your classifier, check its final performance on the test set. How does the performance on the test set compare to the performance on the dev-test set? Is this what you'd expect?
 import nltk
 def gender_features(name):
	features={}
	features['firstletter']=name[0].lower()
	features['one_lastletter']=name[-1:].lower()
	features['two_lastletters']=name[-2:].lower()
	features['three_lastletters']=name[-3:].lower()
	if len(name)>3:
		features['four_lastletters']=name[-4:].lower()
	return features

 from nltk.corpus import names
 import random
 names = ([(name, 'male') for name in names.words('male.txt')] +
             [(name, 'female') for name in names.words('female.txt')])
 random.shuffle(names)
 dev_names, train_names, test_names = names[:500], names[1000:], names[500:1000]
 train_set = [(gender_features(n), g) for (n,g) in train_names]
 devset = [(gender_features(n), g) for (n,g) in dev_names]
 test_set = [(gender_features(n), g) for (n,g) in test_names]
 classifier = nltk.NaiveBayesClassifier.train(train_set)
 errors = []
 for (name, tag) in dev_names:
	guess = classifier.classify(gender_features(name))
	if guess != tag:
		 errors.append( (tag, guess, name) )

		 
 def gender_predicting(name):
	classifier.classify(gender_features(name))
	print 'Name:', name, 'Gender:',classifier.classify(gender_features(name))

	
 def gender_predicting(name):
	classifier.classify(gender_features(name))
	print 'Name:', name, 'Gender:',classifier.classify(gender_features(name))
	print 'Evaluation of Names Classifier Performance on DevTest Data:', nltk.classify.accuracy(classifier, devset), '\n', 'Evaluation of Names Classifier Performance on Test Data:', nltk.classify.accuracy(classifier, test_set), '\n', classifier.show_most_informative_features(20)

 
 def gender_predicting(name):
	classifier.classify(gender_features(name))
print 'Name:', name, 'Gender:',classifier.classify(gender_features(name))
print 'Evaluation of Names Classifier Performance on DevTest Data:', nltk.classify.accuracy(classifier, devset), '\n', 'Evaluation of Names Classifier Performance on Test Data:', nltk.classify.accuracy(classifier, test_set), '\n', classifier.show_most_informative_features(20)

	
