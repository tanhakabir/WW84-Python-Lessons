# Okay, now let’s make that Buzzfeed Quiz! 

We’ll be asking a streamlined version of this quiz. We’ll use just 3 questions and 2 options for each:
e.	Which weapon? (A) Lasso (B) No weapons
f.	Which location? (A) Hawaii (B) Themyscira
g.	What transportation? (A) Train (B) Horse

Hmm, somehow the Python needs to ask the candidate a question. We can command it to do so using the input command; this gives back (returns) the candidate’s answer, which we can store in a variable. Try replacing the commands in your file with the following. (If you’re wondering what the \n is doing, it tells the Python to put in a newline or “hit the return” key.)
```python
# ask the candidate a question
weapon = input( "Which weapon?\n(A) Lasso\n(B) No weapon, thank you\n" )

# print out which weapon they chose
print( f"You chose {weapon}.")
```
Press the Play Button, and you should see the question print out, along with the options. Try typing A and see what happens!
 
Notice that the weapon variable simply stores whatever you typed. Try typing lion instead and see what happens…
 
For now, let’s assume the candidate understands that they should type the letter of their choice (and capitalize it correctly). Then we can use a conditional to have the Python execute commands depending on what they chose. Try adding the following commands to your file:
```python
# if they chose the lasso
if weapon == "A":
    print( "Nice choice!" )
```
Press the Play Button and try entering A as your choice. What happens if you enter B instead?
 
Okay, let’s put all our questions in! Replace the commands in your script with the following. For now, we’ll just print out the responses to make sure everything is hooked up correctly.
```python
# ask the candidate a question
weapon = input( "Which weapon?\n(A) Lasso\n(B) No weapon, thank you\n" )

# ask the candidate a second question
job = input( "What’s your dream job?\n(A) Curator at the Smithsonian\n(B) Running a business\n" )

# ask the candidate a third question
value = input( "What’s more important?\n(A) Money\n(B) Love\n" )

# ask the candidate a fourth question
decade = input( "What’s your favorite decade?\n(A) 1950s\n(B) 1990s\n" )

# ask the candidate a fifth question
animal = input( "What’s your favorite big cat?\n(A) Tiger\n(B) Cheetah\n" )
```
Press the Play button and make sure your responses are recorded correctly!
 
Now it’s time to really score the quiz. With three questions and different choices, we’ll use some variables to guide our response. Add the following commands to your file.
```python
# create some variables for scoring
diane_like = 0
trevor_like = 0
max_like = 0
cheetah_like = 0

# update scoring variables based on the weapon choice
if weapon == "A":
    diane_like = diane_like + 1
    cheetah_like = cheetah_like - 1
if weapon == "B":
    pass

# update scoring variables based on the job choice
if job == "A":
    diane_like = diane_like + 2
    cheetah_like = cheetah_like + 2
if job == "B":
    max_like = max_like + 2

# update scoring variables based on the value choice
if value == "A":
    diane_like = diane_like - 1
    max_like = max_like + 2
if value == "B":
    diane_like = diane_like + 1
    trevor_like = trevor_like + 1

# update scoring variables based on the decade choice
if decade == "A":
    trevor_like = trevor_like + 2
if decade == "B":
    pass

# update scoring variables based on the animal choice
if animal == "A":
    pass
if animal == "B":
    cheetah_like = cheetah_like + 2

# print the results depending on the score
if diane_like >= 3:
    print( "Hello, Wonder Woman!" )
elif trevor_like >= 3:
    print( "Hello, Steve Trevor!" )
elif cheetah_like >= 3:
    print( "Hello, Cheetah!")
else:
    print( "Hello, Max Lord!")
```
Press the Play button and find out which Wonder Woman personality you’re most like!
 

### Credits
This lesson plan was inspired by and adapted from the “active learning module” developed by Emily Craig and Sarah Robinson while they were part of the MaGE Inclusive Peer Mentorship Program at Mount Holyoke College. 



### Extra stuff I don’t think I need
The Python puts a special meaning on the words True and False, and calls them “boolean” values. It turns out that booleans are studied in computer science (and philosophy!) and there is an entire subject called “boolean logic.” You might be comfortable with “arithmetic,” where numbers are operated on to produce other numbers; 1 + 2 is 3. The operands are the numbers 1 and 2, and the operator is the addition operator.  In boolean logic, boolean values (True or False) are operated on to produce other boolean values. We might say, “if it is cold outside AND it is raining, grab a parka.” Then both conditions must be met (must be True) for us to grab a parka. Here the operands are whether or not it is cold outside and whether or not it is raining; the AND operator
