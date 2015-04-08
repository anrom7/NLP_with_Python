# Categorizing and Tagging Words.
# Pokotylo Olena ALs-11
# 5.10 (exercise 8)
# Create a dictionary e, to represent a single lexical entry for some word of your choice. Define keys like headword, part-of-speech, sense, and example, and assign them suitable values.
>>> import nltk
#create defualt dictionary
>>> books=nltk.defaultdict(list)
>>> def mydic (headword, part_of_speech, sense, example):
        movies[headword]=[part_of_speech, sense, example]
#add content to the dictioary
>>> mydic('Adventure','N','story is about a protagonist who journeys to epic or distant places to accomplish something', ' Saturday morning serials were often using many of the same thematic elements as high-budget adventure films.')
>>> mydic('Comedy', 'N', ' story that tells about a series of funny or comical events, intended to make the audience laugh', 'Chart of the top fifty comedy movies according to users of the Internet Movie Database.')
>>> mydic('Crime', 'N', 'story is about a crime that is being committed or was committed','The Guardian and Observer critics pick the best crime films ever made.')
# check dictionary content
>>> movies['Crime']
['N', 'story is about a crime that is being committed or was committed', 'The Guardian and Observer critics pick the best crime films ever made.']
>>>
