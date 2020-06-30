<img width="576" alt="try1" src="https://user-images.githubusercontent.com/12758612/85893967-b5296880-b7a8-11ea-9c5a-0b5fbf4876a6.png">

# Where will this journey take you? Diana’s note continues… 

The Python can simulate certain parts of the future under the right circumstances! Follow these instructions and see if you could save the day, knowing the truth behind the cryptic note!

Copy the following below your decryption code:
```python
score = 0
response1 = input( "Which date will Diana be waiting to meet you?\n (A) Jan 4, 1984\n (B) Dec 4, 1984\n (C) Feb 4, 1984\n (D) Jul 4, 1984\n" )


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
    print( "You save the day! You meet the mysterious donor while others learn about the behavior of the\n\"pecan\" at its keeper talk. The donor reveals the amulet's true power and how to use it for\ngood, letting you save the good citizens of Themyscira from the latest threat!" )
elif score > 0:
    print( "Wonder Woman saves the day! You got a little lost along the way, but luckily Wonder Woman\nwas able figure out the truth behind the note in time. She meets the mysterious donor, who\nreveals the amulet's true power and how to use it for good. You arrive in time to see\nWonder Woman save the good citizens of Themyscira from the latest threat!" )
else: 
    print( "What are you doing having a latte and a scone when the good citizens of Themyscira are under attack?!")
```

Press the Play Button, and use the clues in the cryptic note to answer the questions. Click the TERMINAL area at the bottom and type the letter for your response, then hit return. Answer all the questions to glimpse your future! Did you save the day?

<img width="957" alt="messagequiz" src="https://user-images.githubusercontent.com/12758612/85894863-61b81a00-b7aa-11ea-8f3c-19e9732cff9d.png">


Check your work with the completed code [**here**](https://github.com/microsoft/WW84-Python-Lessons/blob/master/decrypt.py)!
