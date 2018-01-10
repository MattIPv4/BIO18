def generateAlphabet():
    return list(map(chr, range(65, 91))) # Generates alphabet (uppercase)

def generateDial(n):
    alphabet = generateAlphabet()
    dial1 = alphabet.copy()
    dial2 = {} # Will hold new dial
    n = n % len(dial1) # Ensure n is a valid index
    current = 0 # Will hold out last position

    for _ in range(len(dial1)): # Loop through every letter in dial1

        index = n + current - 1 # Start from where we were before, add n
        index = index % len(dial1) # Ensure valid index
        current = index # Save our position for next loop

        letter = dial1[index] # Find the letter
        dial1.remove(letter) # Remove from dial1
        dial2[alphabet[_]] = letter # Add to dial2

    return dial2

def encrypt(n, word):
    dial = list(generateDial(n).values()) # Get a list of dial values
    dial6 = dial[0:6] # Save the first 6
    alphabet = generateAlphabet() # Get an alphabet for lookup
    enc = [] # Will hold our message

    for char in word: # Loop over each chat
        alphabetIndex = alphabet.index(char) # Find its alphabet index
        dialChar = dial[alphabetIndex] # Lookup that index on the dial
        enc.append(dialChar) # Save the encoded char
        dial = [dial[((f+1)%len(dial))] for f in range(len(dial))] # Shift dial by 1

    return ["".join(dial6), "".join(enc)]

def partatest():
    print("\n-- 2(a) --")
    n = None
    while not n or n < 1 or n > 1000000:
        n = int(input("n: "))

    w = None
    while not w or len(w) < 1 or len(w) > 8:
        w = input("word: ").upper()

    print("\n{}\n{}".format(*encrypt(n, w)))

def partbtest():
    print("\n-- 2(b) --")
    print("".join(generateDial(1000000000).values()))

def partctest():
    print("\n-- 2(c) --\n(Brute force, takes some time...)")

    result = None
    alphabet = "".join(generateAlphabet())
    test = False
    n = -1

    def uniquetest(string):
        return sorted(set(list(string))) == sorted(list(string))

    while not test and n < 1000000:
        n += 1
        result = encrypt(n, alphabet)
        test = uniquetest(result[1])

    if test:
        print(n, result)
    else:
        print(test)

# 2(a)
#   Demonstrates the program in operation with user inputs.
partatest()

# 2(b)
#   Returns the second dial order for n = 1,000,000,000
partbtest()

# 2(c)
#   Brute force test (do not suggest running)
#   partctest()
#   Result = False
#     (No value of n between 0 and 1,000,000 generates a unique encoding of the alphabet)

# 2(d)
#   Unsure