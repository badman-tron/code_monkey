#Code Monkey is a series of simple bioinformatics analysis python scripts made by Mitchell Bartolo 2014

print "Welcome to Code Monkey"

seq = raw_input('Please enter your DNA sequence:')
seq = seq.upper() #ensure sequence is upper case so analysis scripts work

#the different kinds of analysis available
analysis_selection = true
while analysis_selection = true 
  print '1 transcribe''\n''2 translate''\n''3 reverse compliment''\n''4 calulate GC content''\n''5 nucleotide count''\n''6 total basepair''\n''7 enter a new sequence''\n''8 help''\n''9 quit'
analysis = raw_input('Enter the number corresponding to the desired analysis: ')  

if analysis == '1':
  print 'transcribe'

elif analysis == '2':
  print 'translate'

elif analysis == '3':
  print 'reverse compliment'

elif analysis == '4':
  print 'calculate GC content'

elif analysis == '5':
  print 'nucleotide count'

elif analysis == '6':
  print 'The sequence is',len(seq),'nucleotides long.'
  break


elif analysis == '7':
  print 'please enter your new sequence'


elif analysis =='8':
  print 'there is no help'    

elif analysis =='9':
  print 'see you next time'

else:
  print "please make a valid selection"

further_analysis = raw_input(would you like to perform more analysis? (y/n))
  

"""
#Nucleotide count
#This code will count the number of each kind of nucleotide in the sequence

if analysis == 5:
	print "NUCLEOTIDE COUTER"

a_count = 0
c_count = 0
g_count = 0
t_count = 0

for char in seq:
    if char == 'A':
       a_count +=1
       
for char in seq:
    if char == 'C':
       c_count +=1

for char in seq:
    if char == 'G':
       g_count +=1      
       
for char in seq:
    if char == 'T':
       t_count +=1 

print "A: %s \nC: %s \nG: %s \nT: %s" % (a_count, c_count, g_count, t_count)


#This code will determine the length of the sequence
#when raw imput = #

print 'The sequence is',len(seq),'nucleotides long.'


#this code will get reverse compliment
#when raw imput = #

def complement(s): 
    basecomplement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} 
    letters = list(s) 
    letters = [basecomplement[base] for base in letters] 
    return ''.join(letters)

def revcom(s):
    return complement(s[::-1])

#print(seq)

print(complement(seq[::-1]))
print(revcom(seq))



#This script will run after a specific analysis has been completed
#Print (randomqutoe)
sel = raw_input('would you like to perform another kind of analysis? (y/n)')

while sel !='y' and choice !='n':
    sel = raw_input("Sorry, I didn't catch that. Enter again: ")



# a selection of gatacca quotes, only show quotes after the analysis has been performed

1 = You want to know how I did it? This is how I did it, I never saved anything for the swim back.
2 = No, no. I got the better end of the deal. I only lent you my body. You lent me your dream.
3 = For someone who was never meant for this world, I must confess I'm suddenly having a hard time leaving it. Of course, they say every atom in our bodies was once part of a star. Maybe I'm not leaving... maybe I'm going home.
4 = There's no gene for fate.
5 = For future reference, right-handed men don't hold it with their left. Just one of those things.
6 = I belonged to a new underclass, no longer determined by social status or the color of your skin. No, we now have discrimination down to a science.
7 = "I not only think that we will tamper with Mother Nature, I think Mother wants us to." - Willard Gaylin
8 = They used to say that a child conceived in love has a greater chance of happiness. They don't say that anymore.
9 = There's more vodka in this piss than there is piss.
10 = We were just wondering if, if it is good to just leave a few things to, to chance?
11 = "Unacceptable risk of heart failure." I think that's what the manual says. The only trip I'll take in space is around the sun on this satellite right here.
12 = Well... I guess we can rule out suicide.
13 = The only way you're going to see the inside of a spaceship is if you were cleaning it.
14 = Jerome Morrow was never meant to be one step down on the podium.
"""