##goes through and finds which predictors are missing and copies them into an empty text file

listOfNumbers = open("firstRowNumbersOfPredictors.txt", "r") ##Generated from bash as per instructions in Readme.
empty=open("missingPredictors.txt", "w") #where we write out missing predictors.
rangeOf= open("length.txt", "r") #number of total reads
length = next(rangeOf)

temp = 1
using = next(listOfNumbers)

#goes through to length, if it finds a missing position, writes it into new file.

for x in range(0,((int(length)))):
    if (x == int(using)):
        try:
                using = next(listOfNumbers)
        except StopIteration:
                pass
    else:
        empty.write(str(x))
        empty.write("\n")
        temp = temp +1
                      
