#Chapter 8
#Exercise 18
#Author Sofiya Zaliska ALs-11
#Compare the performance of the top-down, bottom-up, and left-corner parsers
#using the same grammar and three grammatical test sentences. Use timeit to log
#the amount of time each parser takes on the same sentence. Write a function that
#runs all three parsers on all three sentences, and prints a 3-by-3 grid of times, as
#well as row and column totals. Discuss your findings.
def test():
  import nltk
	grammar1 = nltk.parse_cfg("""
	
	""")
	sr_parse = nltk.Shift Reduce Parser(grammar1)

	sent = "Lee ran away home".split()
	return sr_parse.parse(sent)

if __name__=='__main__':
	from time it import Timer
	t = Timer("test()", "from __main__ import test")
	print t.time it(500)/500

def test():
	import nltk
	grammar1 = nltk.parse_cfg("""
	
	""")
	rd_parser = nltk.Recursive Descent Parser(grammar1)

	sent = "Lee ran away home".split()
	t=rd_parser.n best_parse(sent)

if __name__=='__main__':
	from time it import Timer
	t = Timer("test()", "from __main__ import test")
	print t.time it(500)/500
	
