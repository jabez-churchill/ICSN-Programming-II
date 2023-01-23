import random

# DONE(1) Lists
brandList = [
        "Jaguar",
        "Ferrari",
        "Volkswagen",
        "Suzuki",
        "Audi",
        "Volvo",
        "Mitsubishi",
        "Chevrolet",
        "Chrysler",
        "Cadillac",
        "Corvette",
        "Honda",
        "BMW",
        "Ford",
        "Dodge",
        "Porsche",
        "Kia",
        "Saab",
        "Subaru",
        "Lexus",
        "Tesla",
        "Hyundai",
        "Mazda",
        "Jeep",
        "Rolls-Royce",
        "Mercedes-Benz",
        "Nissan",
        "Lamborghini"
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


# Letzgo. How do you work with Lists if they're all different lengths?

# TODO(0): Get familiar with functions: len() and str().
# LEN() = Length. Let's use len() to return the size of a List.
# CASTING. To ensure that our return value is the Data Type what we need (a string).



# TODO(1): Make a "helper function" that TAKES one list, and RETURNS a value using a random index position.
def randomAttributeGrabber(attributeList: list):
    # Get a random number, make sure it's a legal index number by using len()
    randomIndexNumber = random.randrange(0, len(attributeList))
    # Get a random list value (string)
    randomStringFromList = attributeList[randomIndexNumber]
    # Return the value, but cast it as a string.
    return str(randomStringFromList)

# Test: Print your function, pass in a list.
print(randomAttributeGrabber(brandList))

# TODO(2): Declare your main function that Returns a new random car configuration.
        # Grab a random value for each category using your Helper Function.
        # Declare a string, build your output sentence.
        # Return the completed string.

def BuildRandomCar():
    carBrand = randomAttributeGrabber(brandList)
    carDoors = randomAttributeGrabber(doorNumberList)
    carWheelD = randomAttributeGrabber(wheelDriveList)
    carEngineL = randomAttributeGrabber(engineSizeList)
    carDefect = randomAttributeGrabber(defectList)

    newCarDescription = ""
    newCarDescription = carDoors + "-door, " + carWheelD + "-wheel drive " + carBrand + " with a " + carEngineL + " engine " +  carDefect
    return newCarDescription

# Test by printing your new main Function.
print(BuildRandomCar())