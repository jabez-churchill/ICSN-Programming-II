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


# Letzgo.
# How do you work with Lists if they're all different lengths?

# TODO(0): Practice! Get familiar with a couple of new functions.
# LEN() = Length. RETURNS the size of a List, string, or other countable data type.
# STR() = String casting. Casting converts other data types to a string.


# TODO(1): Make a "helper function" that TAKES one list, and RETURNS a value using a random index position.
    # Get a random number, make sure it's a legal index number by using len()
    # Get a random list value (string)
    # Return the value, but cast it as a string.

# Test: Print your function, pass in a list.


# TODO(2): Declare your main function that Returns a new random car configuration.
        # Grab a random value for each category using your Helper Function.
        # Declare a string, build your output sentence.
        # Return the completed string.


# Test by printing your new main Function.