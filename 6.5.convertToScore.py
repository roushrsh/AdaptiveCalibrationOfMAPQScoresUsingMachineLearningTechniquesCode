predictorScores = open("DeepPercentsOrXGBoost.txt", "r")
writeTo = open("a.txt" ,"w")

import numpy as np
import re


def mapScore(p):
        return int(round(-10*np.log10(1-p)))

for x in predictorScores:
	num = float(x.translate(None,"[]"))
        if (float(num) == 1.0):
                writeTo.write("60")
                writeTo.write("\n")
        else:
                value = mapScore(float(str(num)))
                writeTo.write(str(value))
                writeTo.write("\n")


