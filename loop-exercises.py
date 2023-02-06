studentList = [
    "Ernie", 
    "Nine", 
    "Orion",
    "Jamie", 
    "Plaoh",
    "Vegas",
    "Mew",
    "Namwhan", 
    "Palm", 
    "JR",
    "Boss",
    "Bank",
]
# TODO(FINAL): Make a list of all student names...
# Stop the loop and print the INDEX POSTION of YOUR NAME on the list

studentDictionary = {
    "Ernie": "Male", 
    "Nine": "Male", 
    "Orion": "Male",
    "Jamie": "Male", 
    "Plaoh": "Male",
    "Vegas": "Male",
    "Mew": "Female",
    "Namwhan": "Female", 
    "Palm": "Female", 
    "JR": "Male",
    "Boss": "Male",
    "Bank": "Male",
}

while(True):
    nameToCheck = input("Type a nickname... ")
    for studentName in studentDictionary:
        if





# Let's play with LOOPS (Iterators)
# ??? Loops work with any "iteratable" data types... Let's see how they work.


# TODO(1): declare a new string, assign a sentence to it (write whatever).
# TODO(2): declare a new int variable, assign a zero to it. 

sequenceOfLetters = "var is a stupid variable name."
vowelCounter = 0

# TODO(3): Print out each letter in the string.

# for letter in sequenceOfLetters:
#     print(letter)

vowels = ["a", "e", "i", "o", "u"]

# TODO(4): Find the number of VOWELS in your string.
for letter in sequenceOfLetters:
    if(letter in vowels):
        vowelCounter = vowelCounter + 1

print(vowelCounter)


