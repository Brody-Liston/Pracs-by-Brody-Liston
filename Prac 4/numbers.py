
def main():
    list_of_numbers = []
    num_numbers = 5

    print ("Input 5 Numbers ")

    for number in range(1, num_numbers + 1):
        given_numbers = float(input("Enter Numner {:} ".format(number,)))
        list_of_numbers.append(given_numbers)

main()