hex_colour = {"f0f8ff": "AliceBlue", "f5f5dc": "Beige", "000000": "Black", "ffebcd": "BlanchedAlmond",
                  "8a2be2": "BlueViolet", "5f9ea0": "CadetBlue", "d2691e": "Chocolate", "ff7f50": "Coral",
                  "6495ed": "CornflowerBlue", "b8860b": "DarkGoldenrod"}

def main():
    hexadecimal = input("Enter hexadecimal: ").lower()
    while hexadecimal != "":
        if hexadecimal in hex_colour:
            print(hexadecimal, "is", hex_colour[hexadecimal])
        else:
            print("Invalid hexadecimal")
        hexadecimal = input("Enter hexadecimal: ").lower()




def all_colour(hexadecimal): # loop prints all colour, im just not sure where to put it into the code.
    for i in hex_colour:
        print(i, "is", hex_colour[hexadecimal])


main()
