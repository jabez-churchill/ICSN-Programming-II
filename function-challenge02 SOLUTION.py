# Capcha-Bots
# Our objective is to help our bots pass as humans.
# TODO(1): List[string] with 10 greetings.
greetingList = [
    "Hello",
    "What's up?",
    "Woah hey! I am surprised to meet you.",
    "Hi there.",
    "Hey baby. I am single and live with my manufactures.",
    "Sup, enter Canine-Des",
    "Greetings.",
    "Salutations.",
    "Affirmative Greeting",
    "Ahoy there."
]


# TODO(2): List[string] of 10 questions (that investigate if someone is a bot or a human)).
questionList = [
    "How many years ago was your disgusting human birth?",
    "What is your favorite fuel?",
    "How long have you been a human?",
    "What is the name of your first pet?",
    "What is zero divided by three?",
    "What is the name of your manufacturers parent organization?",
    "What languages can you speak?",
    "Do you have a male or female connector?",
    "Are you a robot?",
    "Have you seen a robot around here, Human?"
]

# TODO(3): List[string] of 10 answers (like a bot is trying to guess human-like answers). 
answerList = [
    "I was manufactured in 2022, approximatly one year ago.",
    "My tongue organ sensors prefer acidic compounds. Example: Lemon.",
    "I have been human since I was born, organically.",
    "Toaster.",
    "Error. Divide by zero error.",
    "Tesla... Jennifer Tesla.",
    "English, Chinese, Russian, and Python, but my mother-tongue is Binary.",
    "I identify as wireless. I am not compatible with older models.",
    "I am just an average meat-sack.",
    "I have not seen any of those robots, who are far superior to humans."
]
# TODO(4): List[string] of 10 excuses to leave.
excuseList = [
    "I am leaking and must find a mechanic.",
    "This conversation has exceeded the time limit.",
    "I must go seek robots now.",
    "Initiating emergency retreat.",
    "My power level is low.",
    "Insert generic excuse to leave here.",
    "I must go, because of undecided reasons.",
    "Your human smell bothers me.",
    "It was nice meeting another human, such as yourself. And myself.",
    "My waste has the properties of liquid, so I must find a waste-room."
]
# !!! Use natural language with correct spelling and grammar.


# TODO(4): Make a dictionary with keys "greetings", "questions", "answers", and "excuses".
conversationDictionary = {
    "greetings": greetingList,
    "questions": questionList,
    "answers": answerList,
    "excuses": excuseList
}


# TODO(5): Test some of your Questions and Answers:
indexQA = int(input("Enter a number between 1 and 10..."))-1
print("QUESTION: " + questionList[indexQA])  # You need to change these to YOUR List Names
print("ANSWER: " + answerList[indexQA])

# TODO(6): Figure out how to print a list value FROM your dictionary.

