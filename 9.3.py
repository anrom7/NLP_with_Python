import nltk
fs1=nltk.FeatStruct(TENSE='past', NUM='sg')
fs2=nltk.FeatStruct(TENSE='past', NUM='sg', GND='fem', ARG=fs1)
print fs1
print fs2
print fs1.subsumes (fs2) #перевіряємо чи fs1 включає у собі fs2
print fs2.subsumes (fs1) #перевіряємо чи fs2 включає у собі fs1
# у цій функції ми робимо дві структури,але лише у випадку, якщо fs1 включає в себе fs2
def subs (fs1, fs2):
	if fs1.subsumes (fs2):
		print fs1.unify(fs2)
	elif fs2.subsumes (fs1):
		print fs2.unify(fs1)
	else: print "None"
