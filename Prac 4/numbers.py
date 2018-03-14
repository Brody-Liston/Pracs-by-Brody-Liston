
def main():
    list_of_numbers = []
    num_numbers = 5

    print ("Input 5 Numbers ")

    for number in range(1, num_numbers + 1):
        given_numbers = float(input("Enter Numner {:} ".format(number,)))
        list_of_numbers.append(given_numbers)
    facts(list_of_numbers)



def facts(list_of_numbers):
    print("The first number is {}".format(int(list_of_numbers[0])))
    print("The last number is {}".format(int(list_of_numbers[-1])))
    print("The smallest number is {}".format(int(min(list_of_numbers))))
    print("The largest number is {}".format(int(max(list_of_numbers))))
    print("The average of the numbers is {}".format(float(sum(list_of_numbers)/len(list_of_numbers))))


main()