predictorsFile = open("predictorsGenerated.txt", "r")
zeroOneToAdd = open("zeroOneWithoutMissingPredictors.txt", "r")

#newFile containing only the reads with predictors.
mergedPredAndZeros = open("mergedPredAndZeros.txt", "w")


from itertools import izip


for x, y in izip(predictorsFile, zeroOneToAdd):
        x = x.strip()
        y = y.strip()
        mergedPredAndZeros.write(x)
        mergedPredAndZeros.write(",")
        mergedPredAndZeros.write(y)
        mergedPredAndZeros.write("\n")

