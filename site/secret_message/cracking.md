---
layout: home
banner_image: "/site/images/ww84_edu_01_github_decode_msg.png"
---

# **Wonder Woman 1984: Decode a secret message**

---

<img width="576" alt="encryptedmessage" src="https://user-images.githubusercontent.com/12758612/86677410-6baef980-bfb0-11ea-95e1-4c766bb569f8.png">

## Okay, time to get cracking

I think the message might be encrypted with something called a “Caesar cipher,” where all the letters are shifted in the alphabet by some amount. I’ll need you to give the Python its own Golden Lasso superpower for finding the true meaning of the words "WHY", “oskza”, “ohupo”, and "ED".

Let’s start by giving the superpower to shift a single letter. You might notice some other commands in here, but we don’t have time to cover them all right now. Replace the code in your file with the following: 
```python
# define a superpower (function) that finds the truth by shifting the letter by the specified amount
def lassoLetter( letter, shiftAmount ):
    # use the ord superpower to translate the letter to a special number called its ASCII code 
    # and associate it codename letterCode
    letterCode = ord(letter.lower())
    
    # shift the ASCII code to find the true letter's ASCII code
    # (my team says that ASCII codes are in order, starting with the code for the letter a)
    trueLetterCode = ord("a") + ((letterCode - ord("a"))+shiftAmount) % 26
   
    # now reveal the true letter by using the chr superpower to translate back from ASCII
    # "return" this as a result of invoking the superpower lassoLetter
    return chr(trueLetterCode)
```
We’ll need to invoke it on every letter in a word, so let’s give the Python another superpower (and command it to use the lassoLetter superpower as part of this new one). Copy the following and put it after the lassoLetter superpower.

```python
# define a superpower (function) that finds the truth
# by shifting all the letters in a word by the specified amount
def lassoWord( word, shiftAmount ):
    # this codename (variable) will be updated to store the true phrase after shifting
    trueWord = ""
    
    # for each letter in the word
    for letter in word:
        # invoke the superpower (function) lassoLetter to reveal the true letter
        # and update the codename trueWord
        trueWord = trueWord + lassoLetter( letter, shiftAmount )

    # return the truth
    return trueWord
```
Press the Play Button, and … nothing should happen … We only endowed the Python with the superpower, but didn’t invoke it. We will test it by invoking the lassoWord superpower on the word terra—shifting by 13 should reveal the true word “green.”

```python
# try out the superpower on the phrase
print( "Shifting terra by 13 gives: \n" + lassoWord( "terra", 13 ) )
```
Press the Play Button, and you should see the truth revealed for "terra"!

<img width="958" alt="terra" src="https://user-images.githubusercontent.com/12758612/85451214-80ba7000-b54e-11ea-80c2-366bb144df7a.png">
 
## Now… command the Python to use its new superpower to reveal the truth
Modify the commands in your file to reveal the truth behind:
1.	the word “WHY” shifted by 13,
2.	the word “oskza” shifted by -18,
3.	the word “ohupo” shifted by -1, and
4.	the word “ED” shifted by 25.

Press the Play Button, and you should see the final clue to the true meeting place and time revealed.

### [Let's see if we found easter egg! >](quiz.md)
