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
        "made of 100% beef."
        ]

# TODO(4) a dictionary of lists (as values).
dictionaryOfCarAttributes = {
        # Key        Value (an Array)
        "carBrands": brandList,
        "carDoors" : doorNumberList,
        "carWheelDrive:": wheelDriveList,
        "carEngineSize": engineSizeList
        }


# TODO(3): Random Number Generator, takes one argument.
def GetRandomListIndex(listSize):
        # randomInt = random.randint(0,10) # HOW DO WE MAKE THIS ADAPT TO DIFFERENT SIZE LISTS?***
        # !!! Start here. Note this pattern.

        randomInt = random.randint(0,listSize-1)
        return randomInt

# TODO(4): The function Len() returns a Lenth.
# 
# print(len(brandList))
# print(brandList)


# TODO(): Test your random number generator with a print.
# by calling print, then enter a list name, but add square brackets [] (An index number)
# Then, call your function in the square brackets.
# Finally, add the argument len() that contains your list name again.
#print(brandList[GetRandomInt(len(brandList))])



# TODO() Define a function that requires one PARAMETER. 
# This function will print random values from of each list.
# You'll pass in your dictionary when it's called. 
def PrintARandomCarDescription(dictionaryFullOfCarAttributes):
        # create a new LOCAL variable and fetch each of your random attributes.
        brand = brandList[GetRandomListIndex(len(brandList))]
        door = doorNumberList[GetRandomListIndex(len(doorNumberList))]
        wheelDrive = wheelDriveList[GetRandomListIndex(len(wheelDriveList))]
        engineSize = engineSizeList[GetRandomListIndex(len(engineSizeList))]
        defect = defectList[GetRandomListIndex(len(defectList))]

        print(doorNumberList + "-door, " + wheelDrive + "-wheel drive" + brand + " with " +  defect)               


# TODO(7) Add more values to some of your lists, so they're unequal... and call your Function!
# !!! This isn't good. Maybe try the dictionary. Have your function use dictionary.
# Now, it shouldn't matter how many lists you have, or how many values each list has. 

PrintARandomCarDescription()
print("yay ☺")