# Chapter 8
# Exercise 10
# Author Svitlana Syytsia
'''
Use the graphical chart-parser interface to experiment with different rule invocation
strategies. Come up with your own strategy that you can execute manually
using the graphical interface. Describe the steps, and report any efficiency improvements
it has (e.g., in terms of the size of the resulting chart). Do these improvements
depend on the structure of the grammar? What do you think of the
prospects for significant performance boosts from cleverer rule invocation
strategies?
'''
print "The Task:"
print "Use the graphical chart-parser interface to experiment with different rule invocation strategies. Come up with your own strategy that you can execute manually using the graphical interface. Describe the steps, and report any efficiency improvements it has (e.g., in terms of the size of the resulting chart). Do these improvements depend on the structure of the grammar? What do you think of the prospects for significant performance boosts from cleverer rule invocation strategies?"
print "The Answer:"
print "I have used graphical chart parser and experimented with different rule invocation strategies. I have experimented with Top Down and Bottom Up strategies. Using Top Down strategy the parser makes a huge number of predictions and when the prediction is not true it destroys the part of tree even if this part of tree is correct. During Top Down Parsing input's overall structure is decided (or guessed at) first, before dealing with mid-level parts, leaving the lowest-level small details to last. A top-down parse discovers and processes the hierarchical tree starting from the top, and incrementally works its way downwards and rightwards. Top-down parsing eagerly decides what a construct is much earlier, when it has only scanned the leftmost symbol of that construct and has not yet parsed any of its parts.  The Bottom Up strategy identifies and processes the text's lowest-level small details first, before its mid-level structures, and leaving the highest-level overall structure to last. "
print "I think performance depends more on strategy than on structure of grammar."
