# Birthday problem
#
# Example 3.3 How many people do we need to have in a room to make it a favorable
# bet (probability of success greater than 1/2) that two people in the room will have
# the same birthday?


year = 365          # the number of possible birthdays
down = []           # the possible sequences with no duplications
down_product = 1    # the total number of possible sequences with no duplications
people = range(18,25)    # testing for the number of people in the room being from 18 to 24
result = 0

for i in people:        # testing for the number of people in the room being from 18 to 24
    for j in range(i):
        down.append(year - j)

    for k in down:
        down_product *= k

    result = down_product / year ** i
    print("for number of people =", i)
    print("the possible sequences with no dups:", down)
    print("the total number of possible sequences with no dups:", down_product)
    print("Probability =", result)
    print()
    down = []
    down_product = 1
