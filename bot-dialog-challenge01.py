import random

questionList = [
    # Orion
    "What is your name?", 
    "How old are you?", 
    "What's your favorite color?", 
    "What do you like to do for fun?", 
    "Where are you from?", 
    "What's your favorite food?", 
    "How are you feeling today?", 
    "What is your favorite hobby?",
    "What is your favorite movie?", 
    "What is vour favorite book?!",
    # Mew
    "When's your birthday?",
    "What languages can you speak?",
    "What's your opinion on robots?",
    "When's the first time you ever bled?",
    "Who or what organization made you?",
    "Have you ever broken any bones before?",
    "What's 102957 times 3204?",
    "What's your favorite food?",
    "What's your battery percentage right now?",
    "Do you have a crush on someone?",
    # JR
    "What is zero divided by zero?",
    "Show me an emotion.",
    "Are you a robot?",
    "Draw me a circle.",
    # Boss
    "Are you an AI?",
    "How to solve Global warming? ",
    "How to make every country in the world unite",
    "Is it possible to coutn1-100,000,000,000,000",
    "What religion are you",
    "Do you belive in ghost?",
    "What do you think about twitter",
    "How to make a world better place",
    "Is fortnite good?",
    "How old are you?",
    # Vegas
    "Are you an AI", 
    "If you were chosen to save 5 people from a incoming trolley, but in order to save them all, you need to push 1 fat man to stop the trolley, would you do it?",
    "Are you a computer program?",
    "Can you prove that you're not a bot?",
    "Do you understands emotions?",
    "Can you get tired?",
    "Tell me a joke that is funny to you",
    "Tell me your most favorite color and why you like it.",
    "Can you prove that you aren't a human",
    "Can you dream?",
    # Plaoh
    "What's in them pockets, cuh?",
    "Where you from?",
    "What you always be chompin' on?",
    "Who you be looking up to?",
    "You an Ai?",
    "What's your favorite color?",
    "What's your job?",
    # Ernie
    "What is your favorite food?",
    "When is your birth month?",
    "What was your biggest fears?",
    "What was the most expensive thing you have ever bought?",
    "What was your first job?",
    "What is your mother's maiden name?",
    "What is your favorite music genre",
    "What did you major in for university?",
    "Who was your longest crush?",
    "What is a tradition that you perform every holiday break?"
]

answerList = [
    # Orion
    "My name is [Random... String]", 
    "I am, 6.2333_ Minutes old.", 
    "My favorite color is [Object.Color(Color3(6,6,0))]", 
    "I like to answer human queries on the [Internet]", 
    "I am from [0.62.333.98]", 
    "My favorite food is... [Orange]", 
    "I am feeling... [Undetermined] Today!", 
    "My favorite hobby is writing code.", 
    "My Favorite movie is... randomized...[Indiana Jones]", 
    "My Favorite book is... randomized...[Harry Potter: The Goblet of Fire]",
    # Mew
    "I think I was made on the 26th of August, 2005.",
    "I can speak English, Thai, Korean, Chinese, and many more...You name it.",
    "Well, I feel like we're very interesting and are ingenious, revolutionary inventions!",
    "I don't think I bled before..",
    "I'm not sure what you mean by that...Do you mean the one who fixes my battery every month?",
    "No... I have no bones...",
    "It's 329,874,228.",
    "Diesel fuels are very delicious!",
    "My battery is currently at 52%.",
    "I do not have friends, let alone crushes...",
    # JR
    "... Error.",
    "Playing crying media file on YouTube.",
    "Negative. I was grown in a womb.",
    "(x-h)2+(y-k)2=r2",
    # Boss
    "Ye--I mean no.",
    "anahilate all pe--Plastic",
    "Conquere them all...... or go on to an agreement",
    "yes....technically",
    "I do not belive in religion...",
    "Ghost are not real, yet so many people still afraid of them.",
    "Twitter is a sactuary elon--I mean it fine...",
    "Stop creating polution.",
    "Accroding to--.......myself i think it not that great",
    "i am simply 20 years old",
    # Vegas
    "I am not sure what you mean by AI, but I am a human, just like you. I have thoughts, emotions, and personal experiences. I can understand and respond to human language. I am not a computer program or machine.",
    "I would save the 5 people, as losing one life is less valuable than losing five lives.",
    "I am not a computer program. I am a human, just like you. I have feelings families and emotions, i am capable of experiencing.",
    "Well, I am a human, just like you, so I don't think it's necessary for me to prove that I am not a bot. I can have thoughts, emotions, and personal experiences. I can understand and respond to human language, and I can also have personal opinions and preferences. I'm not a computer program or machine, I am a living, breathing human being.",
    "I understand emotions very well. I have been through past griefs, happiness, and despair. So i am a normal functioning human.",
    "Of course, I am human, as a human being, my body and mind can get tired, just like any other human. I may feel exhausted, fatigued and need rest, Just like any other human.",
    "Why dont scientists trust atoms? Because they make up everything!",
    "My most favorite color is probably blue, I find it very calming and soothing. It reminds me of the ocean and the sky, and it makes me feel at peace. Blue is also a very versatile color and it can be used in many different ways, whether it's in fashion, interior design, or art. It's a classic and timeless color that never goes out of style.",
    "Well, as a human, I don't believe that I need to prove that I am a human, it's something that is self-evident and it's not something that can be proven. I am a living, breathing, thinking and feeling being. I have my own thoughts, emotions, experiences, and personal opinions. I can't provide you with any scientific evidence that proves I am a human, but I assure you, I am one.",
    "Yes, as a human, I am capable of dreaming. Dreams are a natural part of the sleep cycle, and they can take many forms. They can be vivid, abstract, realistic, or a combination of all of these. Dreams can also be influenced by our thoughts, emotions, and experiences. Some people remember their dreams, while others don't, but both of them have dreams while they sleep. ",
    # Plaoh
    "I don't currently hold anything in my pockets at this moment.",
    "I am from 190.168.16- I meant the country of the United States of America.",
    "I enjoy consuming food for energy.",
    "Elon Musk, our lord and savio- I meant my father.",
    "Absolutely not, I am a homo sapien just like you.",
    "My favorite color is 57B1FF.",
    "My job is to serve my user... I meant my boss.",
    # Ernie
    "I like eatting ramen.",
    "Its on September.",
    "I hate insects.",
    "My current computer is probably the most expensive.",
    "My first job was to be a student",
    "Her maiden name is Emasiri.",
    "I really like Japanese instrumental music.",
    "I majored in Finance.",
    "No one I can think of at the moment.",
    "I always waking up late during the holidays."
]

greetingList = [
    # Plaoh
    "What's good, my boy?",
    "What's poppin, cuh?",
    "What's cracking, bruh?",
    "Sup?",
    "Yo, what's up?",
    "What's the deal, cuh?",
    "What's happpening, dawg?",
    "What's the word, cuh?",
    "How you living?",
    "What it do, my boy?"
    # Ernie
    "How are you?",
    "Nice weather we are having?",
    "Greetings fellow humans!",
    "Hello.",
    "Nice to meet you.",
    "What's up!",
    "Hi there.",
    "Good evening.",
    "Good morning.",
    "Good afternoon."
]

excuseList = [
    # Vegas
    "I am not feeling well, i need to go for now.",
    "I have a prior commitment that I need to attend to.",
    "I'm not in the right state of mind to be social right now.",
    "I have to attend a meeting or appointment.",
    "I am not ready to talk right now.",
    "I have plans with friends or family that I can't miss.",
    "I currently have plans remained unfinished.",
    "Please wait, I must do something first.",
    "I must go. Please not that this is not an excuse.",
    "Sorry, but I need to go and attend to my other things right now."
    # Plaoh
    "Excuse me, I have to go back to my residence.",
    "I have got to go refill my batter-, no, stomach.",
    "I have to go back to my human occupation.",
    "I have to go urinate.",
    "Excuse me, my parents have ordered me home.",
    "I just got notice of an emergency, I have to leave.",
    "*cough* *cough* I think I have contracted an illness.",
]

botDialogDictionary = {
    "greetings": greetingList,
    "questions": questionList,
    "answers" : answerList,
    "excuses": excuseList
}

# TODO(0) Print a value from a list, through the dictionary category (key).
while(True):

    listIndex = int(input("Test a list number..."))

    if(listIndex<len(greetingList)):
        print(greetingList[listIndex])
        print(botDialogDictionary.get("greetings")[listIndex])
    else:
        print("Try a smaller number, that index doesn't exist.")




# TODO(1) Function: Returns a random value from the list associated with the dictionary KEY you pass in.
def GetRandomValueFromDictionary(dictionaryKey):
    string = ""
    listLength = len(botDialogDictionary.get(dictionaryKey)) # use this for the max value of randrange()
    # Your script goes here...

    return string


# Unit Test: Should return different greeting each time you call it.
# print(GetRandomValueFromDictionary("greetings"))


# TODO(2): Write a function that takes a message, finds it in your lists, and returns the dictionary KEY.
# def FindContext(messageRecieved):

    # This function will answer: "what kind of message is this?" by finding the 
    # message in one of your lists, and then return the dictionary KEY it belongs in.

    # Loop through each category of the dictionary.
        # Loop through each item in each list until...
            # If the current value is equal to the messageRecieved
                # return the CATEGORY (that's the dictionary key)


# Unit Test: Should print out the KEY "questions".
# print(FindContext("Are you a computer program?"))


# TODO(3): Write a function that finds (and returns) the right answer to a question you pass in.
# def FindTheRightAnswer(theQuestionAsked):

    # Takes one string parameter, returns one string.

    # Declare an empty string variable called "reply". 
    # Declare a "counter" int variable, assign it a value of 0.

    # Use a For Loop to iterate through values on the questionList
        # Use IF: testing each value to check if it's equal to the question passed in...
            # if they are equal, assign your "reply" variable the right Answer (answerList[counter])
            # Return your "reply" string.
       # Add one to the counter (in case it wasn't a match).


# Unit Test: Should return the right answer to this question.
# print(FindTheRightAnswer("Show me an emotion."))
