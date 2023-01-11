import math;

#DECLARE
listOfCompliments[];
listOfInsults[];
listOfSubjects[];

#INITIALIZE
listOfCompliments = ["gorgeous", "lovely", "sweet", "rad", "rightious", "breathtaking", "fantastic", "amazing", "beautiful", "the best"]
listOfInsults = ["horrid", "nasty", "ratty-looking", "ugly", "gross", "the worst", "dirty", "sussy", "rotten"]
mySubjects = ["hat", "nose", "eyes", "hips", "shoes", "smile", "boyfriend", "mouth", "personality", "face", "shirt"]

void GeneratePhrase(){
    int int1 = random.range(0,9);
    int int2 = random.range(0,9);
    string myResult = listOfCompliments[int1] + " " + listOfSubjects;
    Console.WriteLine("hello");
}

GeneratePhrase();
