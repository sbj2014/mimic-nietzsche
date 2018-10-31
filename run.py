"""
Codecademy Pro
Learn Python
Final Project
Markov Chain Text Generator
28 October 2018
"""

# import necessary code (fetch_data module, slightly modified Codecademy Markov Chain generator module)
import fetch_data
from markov_python.cc_markov import MarkovChain
from random import randint

# prepare Markov Chain generator
mc = MarkovChain()

# links to relevant works
wagnerian = {
"https://www.gutenberg.org/files/51356/51356-0.txt" : "The Birth of Tragedy",
"http://www.gutenberg.org/cache/epub/5652/pg5652.txt" : "Untimely Meditations(I)",  
"http://www.gutenberg.org/cache/epub/38226/pg38226.txt" : "Untimely Meditations(II)"
}

positivistic = {
"https://www.gutenberg.org/files/51935/51935-0.txt" : "Human, All-Too-Human (I)",
"https://www.gutenberg.org/files/37841/37841-0.txt" : "Human, All-Too-Human (II)",
"https://www.gutenberg.org/files/39955/39955-0.txt" : "The Dawn of Day",
"https://www.gutenberg.org/files/52881/52881-0.txt" : "The Joyful Wisdom",
"https://www.gutenberg.org/files/1998/1998-0.txt" : "Thus Spoke Zarathustra"
}

late = {
"http://www.gutenberg.org/cache/epub/4363/pg4363.txt" : "Beyond Good and Evil",
"https://www.gutenberg.org/files/52319/52319-0.txt" : "The Genealogy of Morals",
"https://www.gutenberg.org/files/25012/25012-0.txt" : "The Case of Wagner and Nietzsche contra Wagner",
"https://www.gutenberg.org/files/52263/52263-0.txt" : "Twilight of the Idols and The Anti-Christian",
"https://www.gutenberg.org/files/52190/52190-0.txt" : "Ecce Homo"
}

# welcome message
print
print ("Hello, welcome to the Friedrich Nietzsche quote generator.")

# determine desired activity
desired_activity = ""

while desired_activity != "1" and desired_activity != "2":
	print
	print ("What would you like to do: ")
	print ("    1) simply generate quotes")
	print ("    2) play a game")
	desired_activity = raw_input("? ")

# determine desired period
desired_period = ""
period = {}

if desired_activity == "1":
    print
    print ("OK, let's just generate some quotes.")
    while desired_period != "1" and desired_period != "2" and desired_period != "3":
	    print
	    print ("Which period of Nietzsche's work would you like to mimic:")
	    print ("    1) the Wagnerian-Schopenhauerian period")
	    print ("    2) the Positivistic period")
	    print ("    3) the Late period")
	    desired_period = raw_input("? ")

if desired_activity == "2":
    print
    print ("OK, let's play a game.")
    desired_period = str(randint(1,3))
    print ("period = " + desired_period)

if desired_period == "1":
	period = wagnerian
elif desired_period == "2":
	period = positivistic
else:
	period = late

# use method to read a string (call multiple times to add additional data)
print
print ("Accessing works... ")
for link in period:
	if desired_activity == "1":
	    print period[link] + ": " + link
	mc.add_string(fetch_data.acquire_data(link))

# set parameters of passages 
number = ""
while number != "1" and number !="2" and number != "3" and number != "4" and number != "5":
	print
	print ("How many passages would you like to generate(1-5)")
	number = raw_input("? ")
 
number = int(number)

length = 0
while length < 3 or length > 100: 
	try:	
		print
		print ("Words per passage (minimum of 3, maximum of 100):")
		length = raw_input("? ")
		length = int(length)
	except ValueError:
		print ("Sorry, that's not a valid length.")
		print ("Please, try again!")
		length = 0

print

"""
generate text from the Markov Chain (call multiple times to generate additional data) 
and convert output to the required format
"""
for current in range(number):
	while True:
		try:
			temporary = mc.generate_text(length)
			formatted = " ".join(temporary)
			print ("Passage #" + str(current+1) + ": " + formatted)
			print
			break
		except UnicodeEncodeError:
			pass

if desired_activity == "1":
	print
	print ("That's all for now!")

if desired_activity == "2":
	print
	print ("So, which Nietzschean period do you think is represented here: ")
	print ("1) the Wagnerian-Schopenhauerian period")
	print ("2) the Positivistic period")
	print ("3) the Late period")
	answer = ""
	while answer != "1" and answer != "2" and answer != "3":
		answer = raw_input("? ")
	print
	if desired_period == answer:
		print ("That's correct!")
	else:
		print ("Sorry, the correct answer is " + desired_period)
