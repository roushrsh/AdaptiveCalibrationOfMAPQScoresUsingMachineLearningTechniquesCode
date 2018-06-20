##Go through and re-add the values without parameters so we can evaluate the whole as one. This is the calculated values from the previous script, with scores being as they are, along with the 0's we're adding as the mapper wasn't able to map to them.
toAddTo = open("mapScoresWithoutMissing.txt", "r")
empty=open("missingPredictors.txt", "r")
finalVersion = open("finalScoresWithOver60.txt", "w")
temp = 1

using = next(empty)
scores = next(toAddTo)

rangeOf= open("length.txt", "r")
length = next(rangeOf)

##goThrough and add 0 in places where there were no predictors.
for x in range(1,((int(length))+1)):
        if ( int(using) == ((x-1))):
                finalVersion.write("0")
                finalVersion.write("\n")
                try:
                        using = next(empty)
                except StopIteration:
                        continue
        else:
                finalVersion.write(scores)
                try:
                        scores = next(toAddTo)
                except StopIteration:
                        continue

