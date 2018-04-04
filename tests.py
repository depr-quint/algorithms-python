import random, sys, time
from numbers import sort

# create an array with length n
def randomArray(n):
    a = [random.randint(0, n) for x in range(n)]
    if (length < 100):
        print("~ to sort:", a)
    return a

# check if s is an integer
def isInteger(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

algorithms = {"insertion", "selection", "merge", "quick", "tim", "bubble", "shell", "bucket"}

# get sys.argv input for the length
length, sorts = 20, {}
if (len(sys.argv) > 1):
    if (len(sys.argv) == 2):
        if (isInteger(sys.argv[1])):
            length = int(sys.argv[1])
            print("~length: %d\n" % length)
            sorts = algorithms
        else:
            print("~ 1st argument invalid, must be an integer")
    elif (len(sys.argv) == 3):
        if (sys.argv[1] in algorithms):
            sorts = {sys.argv[1]}
        else:
            print("~ 1st argument invalid, must be a sorting algorithm")
        if (isInteger(sys.argv[2])):
            length = int(sys.argv[2])
            print("~length: %d\n" % length)
        else:
            print("~ 2nd argument invalid, must be an integer")
    else:
        print("~ can't use a 3rd argument")

for s in sorts:
    print("~ " + s + " sort:")
    test = randomArray(length)
    start = time.time()
    if (s == "bucket"):
        exec("sort." + s + "(test, 10)")
    else:
        exec("sort." + s + "(test)")
    print("~ time: %.8f" % (time.time() - start))
    if (length < 100):
        print("~ sorted:", test, "\n")
    else: print("")