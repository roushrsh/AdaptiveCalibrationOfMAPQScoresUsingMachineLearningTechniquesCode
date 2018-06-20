#makes a OneZero list without the position of our missing predictors for later teaching our algorithms

#files as mentioned previously
zerosOnes = open("oneZeroWithLeeway.txt", "r")
missingPredictors = open("missingPredictors.txt", "r")
zeroOneWithoutMissingPredictor = open("zeroOneWithoutMissingPredictor.txt", "w")
rangeOf= open("length.txt", "r")
length = next(rangeOf)

lineOfPredictor = next(missingPredictors)       #Goes to next item
lineOfZeroOnes = next(zerosOnes)

for x in range(1,((int(length))+1)):
        if (x == int(lineOfPredictor)):
                try:
                        lineOfPredictor = next(missingPredictors)
                except StopIteration:                           #need to throw exception in case it can't
                        pass
                try:
                        lineOfZeroOnes = next(zerosOnes)
                except StopIteration:
                        pass
        else:
                zeroOneWithoutMissingPredictor.write((lineOfZeroOnes))
                try:
                        lineOfZeroOnes = next(zerosOnes)
                except StopIteration:
                        pass

