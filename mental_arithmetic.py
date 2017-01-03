import random
import matplotlib.pyplot as plt

count = []
options = '1'
rand_nums = []

def generate_rand():
    rand_num = random.randint(1,17)
    rand_nums.append(rand_num)
    arr = []
    print()
    print("-" * 50)
    print("The random number is", rand_num)
    i = 100
    while(i >= 0):
      arr.append(i)
      i -= rand_num

    for i in range(len(arr)):
        if(i%5 == 0):
            print()

        print("%d" % arr[i], end="\t")
    print("\n")
    print("-" * 50)


def record_count():
    record = input("How long did it take: ")
    count.append(float(record))
    print("-" * 50)


def plot_graph():
    plt.plot(rand_nums, count, 'ro')
    plt.xlim(0,18)
    plt.ylim(0,110)
    plt.show()


def show_counts():
    print("-" * 50)
    print("  Random Number        Count")
    print("-----------------    ---------")
    for i in range(len(count)):
        print("\t" + str(rand_nums[i]) + "\t\t" + str(count[i]))
    print("-" * 50)


while(options != '4'):
    print("Enter one of the options below")
    print("1: Generate random numbers, 2: Plot Graph, 3: Show Counts, 4:Exit Program")
    options = input()
    if(options == '1'):
        generate_rand()
        record_count()
    elif(options == '2'):
        plot_graph()
    elif(options == '3'):
        show_counts()
