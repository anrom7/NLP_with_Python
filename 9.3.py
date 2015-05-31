#Shepelevych, PRLs-11
import nltk
# consider two feature structures on my ouw
fs1 = nltk.FeatStruct("[A = [D = d]]")
fs2 = nltk.FeatStruct("[A = [D = d], C = [F = [D = d]]]")
# subsume our feature structures If fs1 subsumes fs2 ,then fs2 must have all the paths and path equivalences of fs1, and may have additional paths and equivalences as well
fs1.subsumes(fs2)
True
# use the unify() method to merge information from two feature structures fs1 and fs2
def subs():
	if fs1.subsumes(fs2):
		print fs1.unify(fs2)
	elif fs2.subsumes(fs1):
		print fs1.unify(fs2)
	else:
		print "This two structures are not incommensurable"
