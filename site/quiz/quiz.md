---
layout: lesson
banner_image_top: "/site/images/ww84_edu_02_github_program_quiz.png"
banner_image_bottom: "/site/images/ww84_edu_github_title_card.png"
---

# **Super Quiz inspired by WONDER WOMAN 1984, coming to theaters**

![WONDER WOMAN 1984 coming to theaters](../images/ww84_edu_github_title_card.png)

--- 

## Okay, now let’s make that personality quiz

We’ll be asking a streamlined version of this quiz. We’ll use just five questions and two options for each: 

1. Which weapon? (A) Lasso (B) No weapons 
1. What’s your dream job? (A) Curator at the Smithsonian (B) Running a business
1. What’s more important? (A) Money (B) Love
1. What’s your favorite decade? (A) 1910s (B) 1980s
1. What’s your favorite big cat? (A) Tiger (B) Cheetah

We'll use these questions to determine which of the following four you are most like:

- Wonder Woman
- Barbara Minerva
- Steve Trevor
- Max Lord

---

Hmm, somehow the Python needs to ask the candidate a question. We can command it to do so using the input command; this gives back (returns) the candidate’s answer, which we can store in a variable. Try replacing the commands in your file with the following. (If you’re wondering what the \n is doing, it tells the Python to put in a new line or hit the “return” key.)
```python
# ask the candidate a question
weapon = input( "Which weapon?\n(A) Lasso\n(B) No weapon, thank you\n" )

# print out which weapon they chose
print( f"You chose {weapon}.")
```

Press the Play button, and you should see the question print out, along with the options. Click in the TERMINAL area and try typing A then “enter” to see what happens.

<img width="960" alt="screenshot" src="https://user-images.githubusercontent.com/12758612/89688177-81b52000-d8b6-11ea-98b1-b84b9e5f305e.png">
 
Notice that the weapon variable simply stores whatever you typed. Try typing lion instead and see what happens…

<img width="282" alt="screenshot" src="https://user-images.githubusercontent.com/12758612/89688296-b45f1880-d8b6-11ea-9611-d155de306764.png">
 
For now, let’s assume the candidate understands that they should type the letter of their choice (and capitalize it correctly). Then we can use a conditional to have the Python execute commands depending on what they chose. Try adding the following commands to your file:
```python
# if they chose the lasso
if weapon == "A":
    print( "Nice choice!" )
```
Press the Play button and try entering A as your choice. Be sure to type in a capital A.

<img width="960" alt="screenshot" src="https://user-images.githubusercontent.com/12758612/89688477-1fa8ea80-d8b7-11ea-8db1-e2315b82357f.png">

What happens if you enter B instead? Can you add another print out for the choice B?
 
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
decade = input( "What’s your favorite decade?\n(A) 1910s\n(B) 1980s\n" )

# ask the candidate a fifth question
animal = input( "What’s your favorite big cat?\n(A) Tiger\n(B) Cheetah\n" )

# print out their choices
print( f"You chose {weapon}, then {job}, then {value}, then {decade}, then {animal}.")
```
Press the Play button and make sure your responses are recorded correctly.

<img width="960" alt="screenshot" src="https://user-images.githubusercontent.com/12758612/89688563-4f57f280-d8b7-11ea-9e69-1538ebaf90e8.png">
 
Now it’s time to really score the quiz. With five questions and different choices, we’ll use some variables to guide our response. We'll add and subtract points from each of the four characters depending on what you choose to answer. At the end we'll tally up all the points and tell you which character you are most like. Add the following commands to your file.
```python
# create some variables for scoring
diana_like = 0
trevor_like = 0
max_like = 0
barbara_like = 0

# update scoring variables based on the weapon choice
if weapon == "A":
    diana_like = diana_like + 1
    barbara_like = barbara_like - 1
if weapon == "B":
    pass

# update scoring variables based on the job choice
if job == "A":
    diana_like = diana_like + 2
    barbara_like = barbara_like + 2
if job == "B":
    max_like = max_like + 2

# update scoring variables based on the value choice
if value == "A":
    diana_like = diana_like - 1
    max_like = max_like + 2
if value == "B":
    diana_like = diana_like + 1
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
    barbara_like = barbara_like + 2

# print the results depending on the score
if diana_like >= 3:
    print( "You're most like Wonder Woman!" )
elif trevor_like >= 3:
    print( "You're most like Steve Trevor!" )
elif barbara_like >= 3:
    print( "You're most like Barbara Minerva!")
else:
    print( "You're most like Max Lord!")
```
Press the Play button and find out which WONDER WOMAN 1984 personality you’re most like!
 
<img width="960" alt="screenshot" src="https://user-images.githubusercontent.com/12758612/89692637-1e7cbb00-d8c1-11ea-85e6-c6bab0eac44c.png">

Check your code with the completed quiz code [**here**](https://github.com/microsoft/WW84-Python-Lessons/blob/master/quiz.py){:target="_blank"}.

### Credits
Special thanks to [Audrey St. John from Mount Holyoke College](https://www.mtholyoke.edu/people/audrey-stjohn){:target="_blank"} for this lesson, which was inspired by and adapted from the “active learning module” developed by Emily Craig and Sarah Robinson for the [MaGE](https://sites.google.com/a/mtholyoke.edu/mage/){:target="_blank"} inclusive peer mentoring program at Mount Holyoke College.


## Let us know how we can make this lesson better

We would love to hear from you in this 3 minute survey.

### [Open survey >](https://www.research.net/r/2DCM2MY){:target="_blank"}