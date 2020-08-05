---
layout: home
banner_image: "/site/images/ww84_edu_01_github_decode_msg.png"
---

# **Secret Message inspired by WONDER WOMAN 1984, coming to theaters**

---

<img width="576" alt="encryptedmessage" src="https://user-images.githubusercontent.com/12758612/86677410-6baef980-bfb0-11ea-95e1-4c766bb569f8.png">

## Where will this journey take you? Diana’s note continues… 

The Python can simulate certain parts of the future under the right circumstances. Follow these instructions and see if you can discover the hidden location and meeting time, knowing the truth behind the cryptic note.

Copy the following below your decryption code:
```python
score = 0
response1 = input( "Which date will you time travel to for the secret location?\n (A) Jan 4, 1984\n (B) Dec 4, 1984\n (C) Feb 4, 1984\n (D) Jul 4, 1984\n" )


if "B" in response1.upper():
    score -= 5
elif "D" in response1.upper():
    score += 10
elif "A" in response1.upper():
    score += 5
    
response2 = input( "On July 4th, you head to:\n (A) The Grand Canyon\n (B) The White House\n (C) The Empire State Building\n (D) The corner coffee shop (with a nagging feeling that there was something special about today)\n" )


if "B" in response2.upper():
    score += 10
elif "D" in response2.upper():
    score -=20


if score == 20: 
    print( "You discovered the easter egg location! You cracked the cryptic note and found the true meaning behind \"oskza ohupo\"!" )
elif score > 0:
    print( "Whoops! You got a little lost along the way, try decrypting the note again!" )
else: 
    print( "What are you doing having a latte and a scone when you're supposed to be at the easter egg location?!")
```

Press the Play Button, and use the clues in the cryptic note to answer the questions. Click the TERMINAL area at the bottom and type the letter for your response, then hit return. Answer all the questions to glimpse your future. Did you save the day?

<img width="957" alt="messagequiz" src="https://user-images.githubusercontent.com/12758612/85894863-61b81a00-b7aa-11ea-8f3c-19e9732cff9d.png">


Check your work with the completed code [**here**](https://github.com/microsoft/WW84-Python-Lessons/blob/master/decrypt.py){:target="_blank"}.

**Credits**: Special thanks to [Audrey St. John from Mount Holyoke College](https://www.mtholyoke.edu/people/audrey-stjohn){:target="_blank"} for this lesson!

## Let us know how we can make this lesson better

We would love to hear from you in this 3 minute survey.

### [Open survey >](https://www.research.net/r/2DCM2MY){:target="_blank"}
