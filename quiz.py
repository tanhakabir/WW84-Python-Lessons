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