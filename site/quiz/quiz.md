---
layout: home
banner_image: "/site/images/ww84_edu_02_github_program_quiz.png"
---

# **Wonder Woman 1984: Program your own personality quiz**

--- 

## Okay, now let’s make that personality quiz

We’ll be asking a streamlined version of this quiz. We’ll use just five questions and two options for each: 

Which weapon? (A) Lasso (B) No weapons 

What’s your dream job? (A) Curator at the Smithsonian (B) Running a business

What’s more important? (A) Money (B) Love

What’s your favorite decade? (A) 1950s (B) 1990s

What’s your favorite big cat? (A) Tiger (B) Cheetah

Hmm, somehow the Python needs to ask the candidate a question. We can command it to do so using the input command; this gives back (returns) the candidate’s answer, which we can store in a variable. Try replacing the commands in your file with the following. (If you’re wondering what the \n is doing, it tells the Python to put in a new line or hit the “return” key.)
```python
# ask the candidate a question
weapon = input( "Which weapon?\n(A) Lasso\n(B) No weapon, thank you\n" )

# print out which weapon they chose
print( f"You chose {weapon}.")
```

Press the Play button, and you should see the question print out, along with the options. Click in the TERMINAL area and try typing A then “enter” to see what happens.

<img width="960" alt="quizweapon" src="https://user-images.githubusercontent.com/12758612/87186135-d2c5fa00-c29f-11ea-8db7-a0e58bed61d0.png">
 
Notice that the weapon variable simply stores whatever you typed. Try typing lion instead and see what happens…

<img width="330" alt="lion" src="https://user-images.githubusercontent.com/12758612/86166879-64787f00-baca-11ea-9ebd-dcd20a74b182.png">
 
For now, let’s assume the candidate understands that they should type the letter of their choice (and capitalize it correctly). Then we can use a conditional to have the Python execute commands depending on what they chose. Try adding the following commands to your file:
```python
# if they chose the lasso
if weapon == "A":
    print( "Nice choice!" )
```
Press the Play button and try entering A as your choice.  What happens if you enter B instead?

<img width="960" alt="quizweaponAchoice" src="https://user-images.githubusercontent.com/12758612/87186265-0d2f9700-c2a0-11ea-859d-792710623259.png">
 
---

Okay, let’s put all our questions in. Replace the commands in your script with the following. For now, we’ll just print out the responses to make sure everything is hooked up correctly.
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

# print out their choices
print( f"You chose {weapon}, then {job}, then {value}, then {decade}, then {animal}.")
```
Press the Play button and make sure your responses are recorded correctly.

<img width="960" alt="quizquestions" src="https://user-images.githubusercontent.com/12758612/87186575-9a72eb80-c2a0-11ea-9b13-c3a7cd3649b3.png">
 
Now it’s time to really score the quiz. With five questions and different choices, we’ll use some variables to guide our response. Add the following commands to your file.
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
 
<img width="960" alt="quizfull" src="https://user-images.githubusercontent.com/12758612/87186738-dc9c2d00-c2a0-11ea-8bb9-fa7ef3c7a5b5.png">

Check your code with the completed quiz code [**here**](https://github.com/microsoft/WW84-Python-Lessons/blob/master/quiz.py){:target="_blank"}.

### Credits
This lesson plan was inspired by and adapted from the “active learning module” developed by Emily Craig and Sarah Robinson while they were part of the MaGE Inclusive Peer Mentorship Program at Mount Holyoke College. 
