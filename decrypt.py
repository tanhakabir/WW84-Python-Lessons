# define a power (function) that finds the truth by shifting the letter by the specified amount
def lassoLetter( letter, shiftAmount ):
    # use the ord power to translate the letter to a special number called its ASCII code 
    # and associate it codename letterCode
    letterCode = ord(letter.lower())
    
    # shift the ASCII code to find the true letter's ASCII code
    # (my team says that ASCII codes are in order, starting with the code for the letter a)
    trueLetterCode = ord("a") + ((letterCode - ord("a"))+shiftAmount) % 26
   
    # now reveal the true letter by using the chr power to translate back from ASCII
    # "return" this as a result of invoking the power lassoLetter
    return chr(trueLetterCode)

# define a power (function) that finds the truth
# by shifting all the letters in a word by the specified amount
def lassoWord( word, shiftAmount ):
    # this codename (variable) will be updated to store the true phrase after shifting
    trueWord = ""
    
    # for each letter in the word
    for letter in word:
        # invoke the power (function) lassoLetter to reveal the true letter
        # and update the codename trueWord
        trueWord = trueWord + lassoLetter( letter, shiftAmount )

    # return the truth
    return trueWord

# try out the power on the phrase
print( "Shifting WHY by 13 gives: \n" + lassoWord( "WHY", 13 ) )
print( "Shifting oskza by -18 gives: \n" + lassoWord( "oskza", -18 ) )
print( "Shifting ohupo by -1 gives: \n" + lassoWord( "ohupo", -1 ) )
print( "Shifting ED by 25 gives: \n" + lassoWord( "ED", 25 ) )


score = 0
response1 = input( "Which date will Diana be waiting to meet you?\n (A) Jan 4, 1984\n (B) Dec 4, 1984\n (C) Feb 4, 1984\n (D) Jul 4, 1984\n" )


if "B" in response1.upper():
    score -= 5
elif "D" in response1.upper():
    score += 10
elif "A" in response1.upper():
    score += 5
    
response2 = input( "On July 4th, you head to:\n (A) The Grand Canyon\n (B) Washington DC\n (C) The Empire State Building\n (D) The corner coffee shop (with a nagging feeling that there was something special about today)\n" )


if "B" in response2.upper():
    score += 10
elif "D" in response2.upper():
    score -=20


if score == 20: 
    print( "You save the day! You meet the mysterious donor while others learn about the behavior of the\n\"pecan\" at its keeper talk. The donor reveals the amulet's true power and how to use it for\ngood, letting you save the good citizens of Themyscira from the latest threat!" )
elif score > 0:
    print( "Wonder Woman saves the day! You got a little lost along the way, but luckily Wonder Woman\nwas able figure out the truth behind the note in time. She meets the mysterious donor, who\nreveals the amulet's true power and how to use it for good. You arrive in time to see\nWonder Woman save the good citizens of Themyscira from the latest threat!" )
else: 
    print( "What are you doing having a latte and a scone when the good citizens of Themyscira are under attack?!")
