class Robot:
    
    def __init__(self, name, age, color) -> None:
        self.name = name
        self.age = age
        self.color = color

    def PrintGreeting(self):
        print("Hi! My name is " + self.name)


# Instantiate two new unique objects from the Robot class:
b1 = Robot("Botty Botparts", 112, (100,149,237))
b2 = Robot("Robota Rodshaft", 3, (191,62,255))

# Call an objects member function (method), 
# which includes a Data Member (property).
# Each object will print the same greeting with it's own uniqe name.
b1.PrintGreeting()
b2.PrintGreeting()