"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""


STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
# print(STATE_NAMES)

state = input("Enter short state: ").upper()

def main(state):
    while state != "":
        if state in STATE_NAMES:
            print(state, "is", STATE_NAMES[state])
        else:
            print("Invalid short state")
        state = input("Enter short state: ").upper()



def all_states(): # loop prints all states, im just not sure where to put it into the code.
    for i in STATE_NAMES:
        print(i, "is", STATE_NAMES[state])


main(state)
