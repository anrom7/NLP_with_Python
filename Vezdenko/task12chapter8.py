# vezzdenko julia al-12 task12 chapter8
# If the chart contains edges <i, j, A -> W1.B W2> and <j, k, B -> W3.>,
# where A and B are categories and W1, W2 and W3 are (possibly empty) sequences of categories or words,
# then add edge <i, k, A -> W1 B.W2> to the chart.

# This rule does not say whether the new edge is active or inactive,
# but then it does not need to since this is fully determined by whether W2 is empty or not.
# In a real implementation, however, it might well be convenient or efficient to add a simple flag
# to the edge data structure to signal activity or inactivity. Notice also that this rule only adds to the chart;
# it does not remove the active edge that has succeeded from the chart.
# This is as it should be since that active edge may be able to succeed in virtue of another inactive edge
# that appears in the chart at a later stage.
# If we remove it, then we run the risk that our parser will fail to find all possible parses,
# or, to put it in logician's parlance, we run the risk that our parser will exhibit incompleteness.
