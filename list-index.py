import random

myComplements = ["gorgeous", "lovely", "sweet", "rad", "rightious", "breathtaking", "fantastic", "amazing", "beautiful", "the best"]
myInsults = ["horrid", "nasty", "ratty-looking", "ugly", "gross", "the worst", "dirty", "sussy", "rotten"]
mySubjects = ["hat", "nose", "eyes", "hips", "shoes", "smile", "boyfriend", "mouth", "personality", "face", "shirt"]

def RandomPhrase():
    int1 = random.randrange(0, 9)
    int2 = random.randrange(0, 9)

    newPhrase = myComplements[int1] + " " + mySubjects[int2]
    print(newPhrase)

RandomPhrase()