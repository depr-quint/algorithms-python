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

# get sys.argv input for the length
if (len(sys.argv) > 1 and isInteger(sys.argv[1])):
    length = int(sys.argv[1])
else:
    length = 20
    if (len(sys.argv) > 1):
        print(sys.argv[1], "is not an integer\n")
print("~length:", length)

#----- Selection Sort -----#
print("Selection Sort:")
test = randomArray(length)
s = time.time()
sort.selection(test)
print("~ time: %.8f" % (time.time() - s))
if (length < 100):
    print("~ sorted_:", test, "\n")

#----- Insertion Sort -----#
print("Insertion Sort:")
test = randomArray(length)
s = time.time()
sort.insertion(test)
print("~ time: %.8f" % (time.time() - s))
if (length < 100):
    print("~ sorted_:", test, "\n")

#----- Merge Sort -----#
print("Merge Sort:")
test = randomArray(length)
s = time.time()
sort.merge(test)
print("~ time: %.8f" % (time.time() - s))
if (length < 100):
    print("~ sorted_:", test, "\n")

#----- Quick Sort -----#
print("Quick Sort:")
test = randomArray(length)
s = time.time()
sort.quick(test)
print("~ time: %.8f" % (time.time() - s))
if (length < 100):
    print("~ sorted_:", test, "\n")

#----- Tim Sort -----#
print("Tim Sort:")
test = randomArray(length)
s = time.time()
sort.tim(test, 32)
print("~ time: %.8f" % (time.time() - s))
if (length < 100):
    print("~ sorted_:", test, "\n")
