import random

# DONE(1) Lists
brandList = [
        "Acura",
        "Honda",
        "BMW",
        "Ferrari",
        "Ford",
        "Toyota",
        "Audi",
        "Dodge",
        "Cadillac",
        "Chevy"
        ]

doorNumberList = [2, 4, 5]
wheelDriveList = [2, 4]
engineSizeList = ["1L", "1.6L", "2L", "3L"]

defectList = [
        "that only drives in reverse.",
        "with heavy fire damage.",
        "that occasionally explodes.",
        "modified to use only three wheels.",
        "made of 100% beef.",
        "that runs only on uranium."
        ]


# Letzgo. How do you work with Lists all of different lengths?
# We need a HELPER function to return the size of each List.

# TODO(3) Define a Random Number Generator function that requires one parameter
#
def GetRandomInt(listSize):
        # !!! Start here. Copy this pattern.
        randomInt = random.randint(0,listSize)
        return randomInt



# TODO(5) Define a function that requires one PARAMETER. 
# You'll pass in your dictionary when it's called. 

# TODO(6) Your function will print random values from of each list.
# HINT: Start by printing a random value of one list.

# TODO(7) Add more values to some of your lists, so they're unequal.
# Now, it shouldn't matter how many lists you have, or how many values each list has. 

print("yay ☺")