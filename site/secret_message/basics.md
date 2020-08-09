---
layout: home
banner_image: "/site/images/ww84_edu_01_github_decode_msg.png"
---

## **Secret Message inspired by WONDER WOMAN 1984, coming to theaters**

![WONDER WOMAN 1984 coming to theaters](../images/ww84_edu_00_github_coming_soon.png)

---

Let’s start by creating a folder on your computer where you can find easily it. Call it “WW84”—I created mine in my Documents folder.

<img width="588" alt="screenshot" src="https://user-images.githubusercontent.com/12758612/89684912-30099700-d8b0-11ea-952c-18ac54736ba0.png">

Then open Visual Studio Code and select "Open folder..." from the start screen; open your WW84 folder.

<img width="393" alt="screenshot" src="https://user-images.githubusercontent.com/12758612/84750307-f5e6dd80-af6f-11ea-8001-741dd19422d2.png">

---

Next create a file called "decrypt.py". 

<img width="662" alt="screenshot" src="https://user-images.githubusercontent.com/12758612/89685377-187ede00-d8b1-11ea-9965-c2d553bcbcff.png">

Also feel free to close the Welcome tab now.
**Note:** As you are coding in Python, Visual Studio Code will suggest other powers to add to Visual Studio Code, such as "Linters". You don't need these for this project, so feel free to ignore them.


The first thing we’ll do is make sure our command center works. We’ll give a simple command that tells the Python to print us a message. Copy the following command into your file:
```python
print( "Hello, Themyscira!" )
```

<img width="960" alt="screenshot" src="https://user-images.githubusercontent.com/12758612/89685504-57ad2f00-d8b1-11ea-89e4-315e4d2c99ea.png">

To have the Python follow your commands, press the green Play button in the upper right corner. You should see a message from the Python below.

<img width="960" alt="screenshot" src="https://user-images.githubusercontent.com/12758612/89685620-8d521800-d8b1-11ea-9a2f-11715b16bfb4.png">

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

<img width="960" alt="screenshot" src="https://user-images.githubusercontent.com/12758612/89685862-094c6000-d8b2-11ea-9422-2ed11d57b25b.png">
 
## Variables
It turns out that the Python has the memory of a goldfish, and we have to explicitly command it to “remember” things. It really likes being part of a secret mission, so we use “codenames” (our team calls these variables) to have it remember certain things. 

The following command tells the Python to associate the codename diana with "WONDER WOMAN 1984" using the special assignment `=` sign operator. Any time after this command, when the Python sees codename  `diana`, it will substitute in "WONDER WOMAN 1984"!
```python
# associate code name (variable) diana with
# the value "WONDER WOMAN 1984"
diana = "WONDER WOMAN 1984"
```
Try it out by replacing the commands in your file with the following. (If you’re wondering what the + sign is doing, it “glues together” phrases into a longer phrase.)
```python
# associate code name diana with
# the phrase "WONDER WOMAN 1984"
diana = "WONDER WOMAN 1984"

# print a message with the true identity of diana
print( "I believe diana is actually " + diana )
```
Press the Play Button, and you should see Diana’s identity revealed.

<img width="960" alt="screenshot" src="https://user-images.githubusercontent.com/12758612/89691707-7534c580-d8be-11ea-9a26-c7a02f0c75e9.png">
 
## Functions
We can give the Python powers (which my team calls functions), which can later be invoked. If we need to change the behavior slightly depending on the situation, we can use additional codenames (my team calls these parameters). 

Here’s how we can give the Python the power to chant. Given a phrase, it can chant it three times.
```python
# define a power (function) to chant a phrase
def chant( phrase ):
    # glue three copies together and message it
    print( phrase + phrase + phrase )
```

Try it out by replacing the commands in your file with the following to give the power and test it out.
```python
# define a power (function) to chant a phrase
def chant( phrase ):
    # glue three copies together and message it
    print( phrase + phrase + phrase )


# invoke the power chant on the phrase "WONDER WOMAN 1984! "
chant( "WONDER WOMAN 1984! " )
```
Press the Play Button, and you should see a chant.

<img width="960" alt="screenshot" src="https://user-images.githubusercontent.com/12758612/89691783-b200bc80-d8be-11ea-8c14-3cabec3fca4c.png">

Great! Now that you know the basics, let's get to decrypting the note.

### [Next step >](cracking.md)
