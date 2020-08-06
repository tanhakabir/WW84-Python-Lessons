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
    print( "Hello, Wonder Woman!" )
elif trevor_like >= 3:
    print( "Hello, Steve Trevor!" )
elif barbara_like >= 3:
    print( "Hello, Barbara Minerva!")
else:
    print( "Hello, Max Lord!")