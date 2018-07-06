XGBoostScores = open("finalScores60MaxXG.txt", "r")
withRegularization = open("finalScores60MaxWithRegularization.txt", "r")
mergedResult = open("MERGED.txt", "w")

from itertools import izip

for x, z in izip(XGBoostScore, withRegularization):
        x = x.strip()
        z = z.strip()
        if (int(x) > 21):
                mergedResult.write(z)
                mergedResult.write("\n")
        else:
                mergedResult.write(x)
                mergedResult.write("\n")

