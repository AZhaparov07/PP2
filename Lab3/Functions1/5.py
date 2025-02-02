import itertools
def permutationsofword():
    word = input("Write a string: ")
    permutations = itertools.permutations(word)
    for i in permutations:
        print("".join(i))
permutationsofword()