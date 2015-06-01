Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # NN - noun, NNS - plural noun, i - varuable, a,s - a list of searched word
>>> # program search 'Which nouns are more common in their plural form, rather than their singular form?'
>>> import nltk
>>> from nltk.corpus import brown
>>> s=[]
>>> a=[]
>>> for (word, tag) in brown.tagged_words(categories='news'):
	if tag=='NN':
		s.append(word)

		
>>> fdist = nltk.FreqDist(s)
>>> for (word, tag) in brown.tagged_words(categories='news'):
	if tag=='NNS':
		a.append(word[:-1])

		
>>> fdist1 = nltk.FreqDist(a)
>>> for i in fdist.keys():
	if fdist1[i]>fdist[i]:
		print (i)

		
student
tank
application
detail
hit
lieutenant
prospect
bond
contribution
letter
implement
motorist
vow
piece
payment
worker
person
force
stroke
share
spectator
error
guest
loan
fee
citizen
obstacle
minute
finance
aide
street
writer
individual
painting
decorator
hat
mine
pain
affair
duffer
soldier
cut
taxpayer
picker
item
shade
investor
voter
relationship
pocket
player
puppet
negotiation
pool
arm
month
estimate
farmer
allowance
chamber
signature
product
appeal
resource
musician
employer
parent
path
member
builder
passenger
sculpture
element
tone
senator
truck
hoodlum
fund
commitment
scholarship
dancer
method
height
string
janitor
second
sale
manufacturer
correspondent
obligation
cost
organ
golfer
call
sport
endowment
snack
rifle
language
restriction
neighbor
employee
quota
hour
nerve
grip
major
narcotic
banker
rebel
machine
folk
standard
officer
underwriter
reform
conversion
friend
official
shareholder
institution
material
competitor
dollar
cookie
Guest
tribe
legislator
arrangement
$1
flower
technique
adjustment
grant
intention
recommendation
visitor
white
raise
procedure
good
representative
dealer
wage
completion
outsider
acre
observer
Attorney
turnpike
feature
chair
adviser
wood
artist
mechanic
draft
defendant
poster
chore
price
rate
reporter
owner
change
store
newspaper
abuse
revenue
drum
teamster
step
decoration
design
bridge
resident
mile
mistake
seat
destroyer
talk
minister
motion
spot
yard
weapon
run
mail
fan
bird
appearance
toy
>>> 
