"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

#I think this will create a list named "some_words" which contains "what", "does", "this", "line", "do"
some_words = ['what', 'does', 'this', 'line', 'do', '?']
#It created a list 

#I think this will recall a specific word in the list and print it as some text
for word in some_words:
    print(word)
#It was actually some sort of loop which printed ALL the objects in the list

#I think this will do the exact same as the last command
for x in some_words:
    print(x)
#The command printed all the objects in the list but with a different notation

#I think this will print the list in its command line notation rather than the individual words
print(some_words)
#The command printed the command line syntax of some_words

#Since some_words is 5 objects long, I think it will definitely print some words contains more than 3 words
if len(some_words) > 3:
    print('some_words contains more than 3 words')
#the command printed some words contains more than 3 words

#I think this will produce a tupel with 6 objects which describes my computer
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

usefulFunction()
#It produced a tupel of facts about the computer I'm using (processor, OS, version, node etc.)