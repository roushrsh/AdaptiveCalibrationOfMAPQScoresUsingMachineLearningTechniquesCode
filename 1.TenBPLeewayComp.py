#Import itertools to scroll through two files simultaenously
from itertools import izip

#GemResults, the true location from the mason file, and write to a file determining if it's a hit or miss
gemFile = open("mappedOutGemFile.txt", "r")
truth = open("100MSortedTruthNumberWrong.txt", "r")
oneZero = open("oneZeroWithLeeway.txt", "w")

#numberOfBP leeway that is allowed.
int bp = 10

for x, y in izip(gemFile, truth):
        x = x.strip()
        y = y.strip()

#if gem is within 10bp of the truth, then we write 1 for hit, or 0 for miss if it isn't.
        if(  (int(str((x.split('        '[0]))[2])) -bp) <= (int(str((y.split(' '[0]))[2]))+1) <=  (int(str((x.split('  '[0]))[2])) +bp)        ):

                oneZero.write("1\n")
        else:
                oneZero.write("0\n")




