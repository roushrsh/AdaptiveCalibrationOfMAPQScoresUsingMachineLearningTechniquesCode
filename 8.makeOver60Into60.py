#Just goes through and makes all over 60s into 60s. This is a seperate script for it to be cleaner, and in case you don't want to have scores stuck at 60. Can easily be any range.
listOfScores = open("finalScoresWithOver60.txt", "r")
finalScores60Max = open("finalScores60Max.txt", "w")


for x in listOfScores:
        if (int(x) > 60):
                finalScores60Max.write("60\n")
        else:
                finalScores60Max.write(x)

