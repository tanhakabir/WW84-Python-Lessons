---
layout: home
banner_image: "/site/images/ww84_edu_01_github_decode_msg.png"
---

# **Secret Message inspired by WONDER WOMAN 1984, coming to theaters**

---

Let’s start by creating a folder on your computer where you can find easily it. Call it “wonder-woman”—I created mine in my Documents folder.

<img width="590" alt="folderdocu" src="https://user-images.githubusercontent.com/12758612/84749733-372abd80-af6f-11ea-93ad-5e8876e980d5.png">

Then open Visual Studio Code and select "Open folder..." from the start screen; open your wonder-woman folder.

<img width="393" alt="openflder" src="https://user-images.githubusercontent.com/12758612/84750307-f5e6dd80-af6f-11ea-8001-741dd19422d2.png">

---

Next create a file called "decrypt.py". 

<img width="450" alt="decrypt" src="https://user-images.githubusercontent.com/12758612/85449971-2ec51a80-b54d-11ea-974b-73f0338ef725.png">

Also feel free to close the Welcome tab now.
**Note:** As you are coding in Python, Visual Studio Code will suggest other powers to add to Visual Studio Code, such as "Linters". You don't need these for this project, so feel free to ignore them.


The first thing we’ll do is make sure our command center works. We’ll give a simple command that tells the Python to print us a message. Copy the following command into your file:
```python
print( "Hello, Themyscira!" )
```

<img width="769" alt="print" src="https://user-images.githubusercontent.com/12758612/85450157-5ae09b80-b54d-11ea-9583-71f8318581a9.png">

To have the Python follow your commands, press the green Play button in the upper right corner. You should see a message from the Python below.

<img width="768" alt="printresult" src="https://user-images.githubusercontent.com/12758612/85450248-6fbd2f00-b54d-11ea-9b24-3692e6aa97ac.png">

## Basics

Before you can uncover the true meaning of the note, let’s walk you through the basics for commanding the Python. If you already know how to use variables, functions, and conditionals, you can skip to the next part.

### [Skip basics >](cracking.md)

## Comments
First, we can write comments to ourselves that the Python will ignore. On any line where we use the `#` symbol, the Python ignores everything after.
Try adding the following to your file:
```python
# this is a comment that won’t be interpreted as a command
```
Press the Play Button, and you should see the same behavior as before.

<img width="768" alt="comment print" src="https://user-images.githubusercontent.com/12758612/85450509-b01cad00-b54d-11ea-9c3d-96a0a168964e.png">
 
## Variables
It turns out that the Python has the memory of a goldfish, and we have to explicitly command it to “remember” things. It really likes being part of a secret mission, so we use “codenames” (our team calls these variables) to have it remember certain things. 

The following command tells the Python to associate the codename diana with "Wonder Woman" using the special assignment `=` sign operator. Any time after this command, when the Python sees codename  `diana`, it will substitute in "Wonder Woman"!
```python
# associate code name (variable) diana with
# the value "Wonder Woman"
diana = "Wonder Woman"
```
Try it out by replacing the commands in your file with the following. (If you’re wondering what the + sign is doing, it “glues together” phrases into a longer phrase.)
```python
# associate code name diana with
# the phrase "Wonder Woman"
diana = "Wonder Woman"

# print a message with the true identity of diana
print( "I believe diana is actually " + diana )
```
Press the Play Button, and you should see Diana’s identity revealed.

<img width="764" alt="varname" src="https://user-images.githubusercontent.com/12758612/85450603-ca568b00-b54d-11ea-8278-3d89e7395201.png">
 
## Functions
We can give the Python superpowers (which my team calls functions), which can later be invoked. If we need to change the behavior slightly depending on the situation, we can use additional codenames (my team calls these parameters). 

Here’s how we can give the Python the superpower to chant. Given a phrase, it can chant it three times.
```python
# define a superpower (function) to chant a phrase
def chant( phrase ):
    # glue three copies together and message it
    print( phrase + phrase + phrase )
```

Try it out by replacing the commands in your file with the following to give the superpower and test it out.
```python
# define a superpower (function) to chant a phrase
def chant( phrase ):
    # glue three copies together and message it
    print( phrase + phrase + phrase )


# invoke the superpower chant on the phrase "Wonder Woman! "
chant( "Wonder Woman! " )
```
Press the Play Button, and you should see a chant.

<img width="767" alt="chant" src="https://user-images.githubusercontent.com/12758612/85450673-db070100-b54d-11ea-81f4-548cf7bdb17f.png">

Great! Now that you know the basics, let's get to decrypting the note.

### [Next step >](cracking.md)
