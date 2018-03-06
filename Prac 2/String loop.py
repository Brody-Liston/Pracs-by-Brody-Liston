
numbers = [0, 50, 100,]
# Another (nicer) version of the above loop using the enumerate function
for i, number in enumerate(numbers):
     print("Number {0} is {1:>3}".format(i + 1, number))