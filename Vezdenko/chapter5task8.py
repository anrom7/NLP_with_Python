# vezdenko julia al-12 , chapter 5 , task 8
import nltk
flowers=nltk.defaultdict(list)
def mydict(headword, part_of_speech, sense, example):
    flowers[headword]=[part_of_speech, sense, example]# I created a dictionary 'mydict' with the following keys: headword, part_of_speech, sense, example


    mydict ('daisy', 'N', 'a small low-growing European plant, having a rosette of leaves and flower heads of yellow central disc flowers and pinkish-white outer ray flowers;', 'I like daisies the most.')
    mydict ('daffodil', 'N', 'a widely cultivated Eurasian amaryllidaceous plant, having spring-blooming yellow flowers;', 'Breeders have developed some daffodils with double, triple, or ambiguously multiple rows and layers of segments, and several wild species also have known double variants.')
    mydict ('freesia', 'N', 'a plant with pleasant-smelling yellow, white, pink, or purple flowers;', 'The plants commonly known as freesias, with fragrant funnel-shaped flowers, are cultivated hybrids of a number of Freesia species.')# I defined needed keys and assigned them trheir meanings.
