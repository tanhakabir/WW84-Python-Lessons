---
layout: home
banner_image: "/site/images/ww84_edu_02_github_program_quiz.png"
---

# **Super Quiz inspired by WONDER WOMAN 1984, coming to theaters**

---

Let’s start by creating a folder on your computer where you can find easily it. Call it “wonder-woman”—I created mine in my Documents folder.

_**Note:** If you already followed the previous lesson where you decoded a secret message, you can use the same folder as before._

<img width="590" src="https://user-images.githubusercontent.com/12758612/84749733-372abd80-af6f-11ea-93ad-5e8876e980d5.png">

Then open Visual Studio Code and select "Open folder..." from the start screen; open your wonder-woman folder.

<img width="393" src="https://user-images.githubusercontent.com/12758612/84750307-f5e6dd80-af6f-11ea-8001-741dd19422d2.png">

---

Let's create a file called "quiz.py".

<img width="379" src="https://user-images.githubusercontent.com/12758612/87181544-5d562b80-c297-11ea-94d2-160200065753.png">

Feel free to close the Welcome tab now.

_**Note:** As you are coding in Python, Visual Studio Code will suggest other powers to add to Visual Studio Code, such as "Linters". You don't need these for this project, so feel free to ignore them._


The first thing we’ll do is make sure our command center works. We’ll give a simple command that tells the Python to print us a message. Copy the following command into your file:
```python
print( "Hello, Themyscira!" )
```

To have the Python follow your commands, press the green Play button in the upper right corner. You should see a message from the Python below.

<img width="958" src="https://user-images.githubusercontent.com/12758612/87182261-a9ee3680-c298-11ea-9e5e-83fe9cba3a87.png">

## Basics

Before you dive into the full personality quiz, let’s walk you through the basics for commanding the Python. If you already know how to use variables, functions, and conditionals, you can skip to the next part.

### [Skip basics >](quiz.md)

## Comments
First, we can write comments to ourselves that the Python will ignore. On any line where we use the # symbol, the Python ignores everything after.

Try adding the following to your file:
```python
# this is a comment that won’t be interpreted as a command
```
Press the Play button, and you should see the same behavior as before.

<img width="960" alt="screenshot" src="https://user-images.githubusercontent.com/12758612/87182464-07828300-c299-11ea-8243-bae8f7c901b4.png">
 
## Variables
If you want the Python to remember something, you can command it to “write it down” using a variable. 

The following command tells the Python to remember the value 1984 using a variable named “year” with the special assignment = sign operator. Any time after this command, when the Python sees “year”, it will substitute the current value.
```python
# use a variable named year to “remember” the value 1984
year = 1984
```
Try it out by replacing the commands in your file with the following. The print command can, if you put an f before what you want printed, use curly braces {} to surround a variable name -- this will make the Python print out the value of the variable.
```python
# use a variable named year to “remember” the value 1984
year = 1984

# print a message to see what year it is
print( f"The year is {year}..." )
```
Press the Play Button, and you should see the year print out.

<img width="960" alt="screenshot" src="https://user-images.githubusercontent.com/12758612/87184110-449c4480-c29c-11ea-8df1-c68452776388.png">

We can update the value of a variable using the same assignment (= sign) operator. The Python will figure out the right-hand side before storing it in the variable. Since “year” already has a value, this command will ask the Python to first substitute the current value of “year” (which is 1984), add 36 to it, then store that value in the variable “year”. This effectively overwrites the value that was written down originally. Try it out by replacing the commands in your file with the following.
```python
# use a variable named year to “remember” the value 1984
year = 1984
        
# print a message to see what year it is
print( f"The year is {year}..." )

year = year + 36

# print a message to see what year it is now
print( f"The year is now {year}..." )
```
Press the Play Button, and you should see the years print out.

<img width="960" alt="screenshot" src="https://user-images.githubusercontent.com/12758612/87184499-f471b200-c29c-11ea-8054-920ed9f8febf.png">
 
## Conditionals
The Python can perform commands depending on some condition. We’re used to conditionals in the real world: “If you’ve been lassoed, then you must tell the truth.” The keyword here is if, which is followed by a condition, where we check whether or not the lasso of truth is around you. When the condition is met (thanks a lot, Wonder Woman), the subsequent command must be followed (the whole truth and nothing but the truth). The Python only expects a condition to either be met or not—it’s either true or false.


To get a little more comfortable, consider the following strategy that Diana uses for how to spend a day _(the following is not code, it's just plain text to explain a scenario)_:
```
if it’s raining cats and dogs
find a cat
if the cat is hangry
        find some milk
        give the milk to the cat
    else
        pet the cat until it purrs or scratches you
else
be happy that it’s not raining animals
    frolic outside
```

Now, how could this play out? It could be the case that:
- It’s raining cats and dogs.
- The cat you find is hangry (hungry + angry).

In this scenario, Diana does three things:
- She finds a cat.
- She finds some milk.
- She gives the milk to the cat.

What if instead:
- It’s not raining cats and dogs?

In this scenario, Diana does two things:
- She is happy that it’s not raining animals.
- She frolics outside.

There are a few more possible scenarios, but let’s move on to how we can use conditionals to command the Python in our year example.

The Python expects a particular “syntax” (formulation of the commands). We won’t go into depth here; instead, just try out this example by adding the following to your file. (If you’re wondering what the == is doing, that is how we test if two numbers are equal; remember that a single = means assignment of a variable, so the Python would be confused).
```python
# if we're in 1984
if year == 1984:
    print( "I left you a message on your answering machine!" )
# if we're in 2020
if year == 2020:
    print( "I left you a voicemail!" )
```
Press the Play button, and you should see the state-of-the-art in messaging.

<img width="960" alt="screenshot" src="https://user-images.githubusercontent.com/12758612/87185607-ea50b300-c29e-11ea-9179-10408fae8568.png">

### Booleans (extra)
The Python puts a special meaning on the words “true” and “false,” and calls them boolean values. It turns out that booleans are studied in computer science (and philosophy) and there is an entire subject called boolean logic. You might be comfortable with arithmetic, where numbers are operated on to produce other numbers; 1 + 2 is 3. The operands are the numbers 1 and 2, and the operator is the addition operator.  In boolean logic, boolean values (True or False) are operated on to produce other boolean values. We might say, “if it is cold outside AND it is raining, grab a parka.” Then both conditions must be met (must be True) for us to grab a parka. Here the operands are whether or not it is cold outside and whether or not it is raining; the AND operator

---

Now that we have the handle on some of the basics, let’s move on to making the quiz.

### [Next step >](quiz.md)
