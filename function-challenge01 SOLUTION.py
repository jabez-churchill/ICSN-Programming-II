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

# TODO(4): a dictionary of lists (as values).
dictionaryOfCarAttributes = {
        # Key        Value (an Array)
        "carBrands": brandList,
        "carDoors" : doorNumberList,
        "carWheelDrive:": wheelDriveList,
        "carEngineSize": engineSizeList,
        "carDefect": defectList
        }

# TODO(4): The function Len() returns a Lenth.
# 
# print(len(brandList))
# print(brandList)


# TODO(3): Random (Legal) Index Generator
def GetRandomListIndex(list):
        # randomInt = random.randint(0,10) # HOW DO WE MAKE THIS ADAPT TO DIFFERENT SIZE LISTS?***
        # We're gonna change this from a random number generator, to return a legal index position.
        # !!! Start here. Note this pattern.

        randomInt = random.randint(0,len(list)-1)
        return randomInt


# TODO(): Test your random number generator with a print.
# by calling print, then enter a list name, but add square brackets [] (An index number)
# Then, call your function in the square brackets.
# Finally, add the argument len() that contains your list name again.
#print(brandList[GetRandomInt(len(brandList))])



# TODO() Define a function that requires one PARAMETER. 
# This function will print random values from of each list.
# You'll pass in your dictionary when it's called. 

# def PrintARandomCarDescription(dictionaryFullOfCarAttributes):
#         # create a new LOCAL variable and fetch each of your random attributes.

#         brand = brandList[GetRandomListIndex(brandList)]
#         door = doorNumberList[GetRandomListIndex(doorNumberList)]
#         wheelDrive = wheelDriveList[GetRandomListIndex(wheelDriveList)]
#         engineSize = engineSizeList[GetRandomListIndex(engineSizeList)]
#         defect = defectList[GetRandomListIndex(defectList)]                

#         print(doorNumberList + "-door, " + wheelDrive + "-wheel drive" + brand + " with " +  defect)               

def GetNewRandomCollection(collection: dict):
        # Declare a new empty local variable, a list to keep one random value from each category.
        newList = []

        # Grab one random value from each category.
        for category in collection.values():
                newList.append(str(category[GetRandomListIndex(category)]))

        # Declare a new local variable that will hold your output string.
        newDescription = ""
        newDescription = newList[1] + "-door, " + newList[2] + "-wheel drive " + newList[0] + " with " +  newList[3] + " engine, " + newList[4]
        return newDescription


def AnotherNewRandomCollection():
        # Declare local variables, casts all datatypes as strings, returns one string
        brand = str(brandList[GetRandomListIndex(brandList)])
        doors = str(doorNumberList[GetRandomListIndex(doorNumberList)])
        wheelD = str(wheelDriveList[GetRandomListIndex(wheelDriveList)])
        litreE = str(engineSizeList[GetRandomListIndex(engineSizeList)])
        defect = str(defectList[GetRandomListIndex(defectList)])

        # Declare a new string to Return, construct sentence with local variables
        myString = doors + "-door, " + wheelD + "-wheel drive " + brand + " with a " + litreE + " engine " +  defect

        return myString



# TODO(7) Add more values to some of your lists, so they're unequal... and call your Function!
# Now, it shouldn't matter how many lists you have, or how many values each list has. 

print(AnotherNewRandomCollection())
# print(GetNewRandomCollection(dictionaryOfCarAttributes))
print("yay ☺")
