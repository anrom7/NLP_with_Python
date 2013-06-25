#presented by Volkov Mark PRLc 11
# Chapter 8, Ex.18
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
	
	
