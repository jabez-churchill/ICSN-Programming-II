myComplements = ["gorgeous", "lovely", "sweet", "rad", "rightious", "breathtaking", "fantastic"]
myInsults = ["horrid", "nasty", "ratty-looking", "ugly", "gross", "the worst", "dirty", "sussy", "rotten"]
mySubjects = ["hat", "nose", "eyes", "hips", "shoes", "smile", "boyfriend", "mouth", "personality"]

def RandomPhrase():
    newPhrase = myComplements[-1] + " " + mySubjects[-1]
    print(newPhrase)

RandomPhrase()