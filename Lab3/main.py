import sys
from math import sqrt
from collections import defaultdict
from itertools import zip_longest
from itertools import groupby
import numpy as np


def p1(n):
    if n <= 0:
        return []
    if n == 1:
        return [1]

    list = [1, 1]

    if n == 2:
        return list

    for i in range(2, n):
        list.append(list[i - 1] + list[i - 2])
    return list


def p2(list):
    primes = []
    for item in list:
        is_prime = True
        for i in range(2, int(sqrt(item)) + 1):
            if item % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(item)
    return primes


def p3(a, b):
    a_union_b = set(a + b)
    a_intersect_b = set(item for item in a if item in b)
    a_minus_b = set(item for item in a if item not in b)
    b_minus_a = set(item for item in b if item not in a)
    return a_union_b, a_intersect_b, a_minus_b, b_minus_a


def p4(notes, moves, position):
    composition = [notes[position % len(notes)]]
    while len(moves):
        position += moves.pop(0)
        composition.append(notes[position % len(notes)])
    return composition


def p5(matrix):
    if len(matrix) == 0:
        return []

    for i in range(0, len(matrix[0])):
        for j in range(0, i):
            matrix[i][j] = 0
    return matrix


def p6(lists, x):
    dict = defaultdict(int)
    for list in lists:
        for item in list:
            dict[item] += 1
    return set(goodItem for goodItem in dict if dict[goodItem] == 2)


def p7(list):
    palindromes = 0
    highest_palindrome = -sys.maxsize
    for item in list:
        if str(abs(item)) == str(abs(item))[::-1]:
            palindromes += 1
            if item > highest_palindrome:
                highest_palindrome = item
    if highest_palindrome == -sys.maxsize:
        return 0, None
    return palindromes, highest_palindrome


def p8(x, list_of_strings, flag):
    to_be_returned = []
    for item in list_of_strings:
        to_be_returned_insance = []
        for letter in item:
            if (ord(letter) % x == 0) is flag:
                to_be_returned_insance.append(letter)
        to_be_returned.append(to_be_returned_insance)

    return to_be_returned


def p9(matrix):
    zipped = list(zip(*matrix))
    persons = []
    for i in range(len(zipped)):
        max_height = 0
        for j in range(len(zipped[0])):
            if zipped[i][j] <= max_height:
                persons.append((j, i))
            else:
                max_height = zipped[i][j]

    return persons


def p10(lists):
    return list(zip_longest(*lists, fillvalue=max([len(x) for x in lists])))



def p11(list):
    try:
        list.sort(key=lambda i: i[1][2])
    except:
        return "A tuple does not have a 2nd element or an element doesn't have 3 characters"

    return list


def p12(list_rhyme):
    list_rhyme.sort(key=lambda i: i[len(i) - 2] + i[len(i) - 1], reverse=True)

    to_be_returned = []
    for key, value in groupby(list_rhyme, key= lambda i: i[len(i) - 2] + i[len(i) - 1]):
        to_be_returned.append(list(value))
    return to_be_returned


def main():
    print("Hello")
    # Enter n to print first n numbers from Fibonacci
    print("(1) Output: ", p1(10))

    # give a list of numbers and return the list with only prime numbers
    prime_list = [2, 3, 5, 12, 12, 17, 18, 23]
    print("(2) Prime list: ", p2(prime_list))

    # two lists and return aUb,a^b,a-b,b-a
    a = [1, 2, 3]
    b = [2, 3, 5]
    print("(3) sets:", p3(a, b))
    # composing
    notes = p4(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2)
    print("(4) composition:", notes)
    # Matrix with 0 under main diagonal
    matrix = [[-1, 1, 2, 3],
              [4, 5, 6, 7],
              [8, 9, 10, 11],
              [13, 14, 15, 16]]
    matrix = p5(matrix)
    print("(5) matrix:")
    for i in range(0, len(matrix)):
        print(matrix[i])

    # Lists and print the items that appear exactly x times
    lists = [[1, 2, 3],
             [2, 3, 4],
             [4, 5, 6],
             [4, 1, "test"]]
    x = 2
    print("(6) lists and x = 2:", p6(lists, x))

    # list and return a tuple with no of palindromes found and greatest palindrome number
    list = [12, 1, -12221, 131]
    print("(7) list and tuple with palindromes: ", p7(list))

    # Ascii code divisibility
    x = 2
    list_of_strings = ["test", "hello", "lab002"]
    flag = False

    print("(8) list and ASCII code divisible by x:",
          p8(x, list_of_strings, flag))

    # Stadium problem
    field = [[1, 2, 3, 2, 1, 1],
             [2, 4, 4, 3, 7, 2],
             [5, 5, 2, 5, 6, 4],
             [6, 6, 7, 6, 7, 5]]
    print("(9) field problem: ", p9(field))

    # 10 tuples 
    list_of_list = [[1, 2, 3], [5, 6, 7], ["a", "b", "c"]]
    print("(10) tuples zipped: ", p10(list_of_list))

    # 11 tuples sorted based on the 3rd char of 2nd element
    list_of_tuples = [('abc', 'bcd'), ('abc', 'zza'), ('abc', 'zzb')]
    print("(11) tuples sorted by 2nd char:", p11(list_of_tuples))

    # 12 list of words and group them by rhyme
    list_rhyme = ['ana', 'banana', 'carte', 'arme', 'parte']
    print("(12) group by rhyme:", p12(list_rhyme))

if __name__ == "__main__":
    main()
