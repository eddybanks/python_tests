import numpy as np;
import random;

# parity check matrix
p = np.matrix( ((0,0,1,1), (0,1,0,1), (0,1,1,0), (0,1,1,1), (1,0,0,1), (1,0,1,0),
                (1,0,1,1), (1,1,0,0), (1,1,0,1), (1,1,1,0), (1,1,1,1)) )

# parity check transposed
pt = p.transpose()

# identity matrix
I = np.matrix( (np.identity(11)) ).astype(int)
II = np.matrix( (np.identity(4)) ).astype(int)
# generator matrix
g = np.concatenate( (II, p), axis=0 ).astype(int)
h = np.concatenate( (p, I), axis=1 ).astype(int)

print("Identity matrix: \n", I)
print("Generator matrix: \n", g)
print("Parity matrix: \n", p)
print("Parity transpose matrix: \n", pt)
print("Hamming matrix: \n", h)


def encode(m):
    # convert the input into a vector or (11x1 matrix)
    m = [int(i) for i in m]
    m = np.matrix( m ).transpose()

    # mod2 dot product of generator matrix and message
    c = np.remainder(np.dot(g, m), 2)

    # convert codeword to string
    codeword = []
    for i in range(c.size):
        codeword.append(c.item(i))
    codeword = ''.join(str(int(i)) for i in codeword)

    print("Encoded codeword: \n", codeword)

def encoder():
    # getting message to be encoded
    m = input("Enter message to be encoded: ")
    encode(m)

def compare(errpos, h):
    number = 0
    result = 0
    for i in h.transpose():
        number+=1
        if (i == errpos).all(1):
            result = number
            break
        else:
            result = -1

    return result


def decode(r):

    # convert the input into a vector
    r = [int(i) for i in r]
    r = np.matrix( r ).transpose()

    # mod2 product of parity check matrix,h and received code, r to find error vector
    err = np.remainder(np.dot(h, r), 2)

    # convert error vector to string
    errpos = []
    for i in range(err.size):
        errpos.append(err.item(i))
    errpos = ''.join(str(int(i)) for i in errpos)
    #print("Error vector: \n", err)

    #compare error vector with hamming code to find error position
    x = compare(err.getT(), h) - 1
    #print(x)

    if x == -2:
        print("No error found")
    else:
        code = []
        for i in range(r.size):
            code.append(r.item(i))
        predec = ''.join(str(int(i)) for i in code)
        code = predec[:x] + str((int(predec[x]) + 1)%2) + predec[x:]
        print("The decoded codeword: \n", code)
        #print("The original codeword: \n", code[:4])


def decoder():
    # get message to be decoded
    r = input("Enter codeword to be decoded: ")
    decode(r)

def channel(code, prob):

    # convert code into vector
    code = [int(i) for i in code]
    code = np.matrix( code ).transpose()

    # corrupt code with noise in channel according to a given probability
    corruption = np.random.choice(2, code.size, p=[1-prob, prob])
    corruption = np.matrix( corruption ).transpose()
    corrupted_code = np.remainder(code + corruption, 2)

    # convert vector into string
    num = []
    for i in range(code.size):
        num.append(corrupted_code.item(i))
    corrupted_code = ''.join(str(int(i)) for i in num)

    #print(code)
    #print(corruption)
    #print(num)

    print("Corrupted code: ", corrupted_code)
    return corrupted_code


def BSC():
    # convert the input into a vector or (11x1 matrix)
    code = input("Enter codeword to be corrupted: ")
    prob = float(input("Enter probability, p: "))
    decode(channel(code, prob))


def GraphFunc():
    randnum = []
    code = input("Enter codeword to be corrupted and tested: ")
    for i in range(20):
        randnum.append(random.uniform(0,0.5))

    for i in range(len(randnum)):
        decode(channel(code, randnum[i]))

    print(randnum)


choice = 0
while choice != 4:
    choice = input("Enter '1' to encode, '2' to decode, '3' for BSC, '4' for graph plot and '5' to exit: ")
    choice = int(choice)
    if choice == 1:
        encoder()
    elif choice == 2:
        decoder()
    elif choice == 3:
        BSC()
    elif choice == 4:
        GraphFunc()
