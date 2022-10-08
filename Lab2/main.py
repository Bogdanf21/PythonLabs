import collections
from functools import reduce

import re


# p1 ##########################
def GCD(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def problem1GCD():
    numbers = input("Enter the numbers: ").split(" ")
    numbers = map(int, numbers)
    gcd = reduce(GCD, numbers)
    print(gcd)


# p2 ###########################
def problem2Vowels():
    string = input("Enter string: ")
    vowels = [letter for letter in string if letter in ["a", "e", "i", "o", "u"]]
    print("Number of vowels: ", len(vowels))


# p3 ##############################
def problem3(haystack, needle):
    print(haystack.count(needle))


# p4 #############################
def problem4(string):
    newString = ''.join(['_' + c.lower() if c.isupper() else c for c in string])
    newString = newString[1:len(newString)]
    print(newString)


# p5 ##############################
def problem5(matrix):
    if not matrix:
        return []
    startrow, endrow, startcol, endcol = 0, len(matrix[0]) - 1, 0, len(matrix[0]) - 1
    array = []
    while startrow <= endrow or startcol <= endcol:

        #
        # start row = 1
        # end row = 2
        # start col = 0
        # end col = 1

        # r
        for i in range(startcol, endcol + 1):
            array.append(matrix[startrow][i])
        startrow += 1
        # d
        for i in range(startrow, endrow + 1):
            array.append(matrix[i][endcol])
        endcol -= 1

        # l
        for i in range(endcol, startcol - 1, -1):
            array.append(matrix[endrow][i])
        endrow -= 1
        # u
        for i in range(endrow, startrow - 1, -1):
            array.append(matrix[i][startcol])
        startcol += 1
    print(array)


# p6 ##############################
def problem6(number):
    string = str(number)
    if string == string[::-1]:
        print("True")
    else:
        print("False")


# p7 ##############################
def problem7(string):
    number = int(re.search("[1-9]+[0-9]*", string).group(0))
    print(number)


# p8 ##############################
def problem8(number):
    numberof1 = 0
    while number >= 1:
        if number % 2:
            numberof1 += 1
        number //= 2
    print(numberof1)


# p9 ##############################
def problem9(string):
    keys = collections.defaultdict(int)
    for letter in string:
        keys[letter] += 1
    print("Most used letter is: ", max(keys, key=keys.get))


# p10 ##########################
def problem10(string):
    words = [word for word in string.split(" ") if len(word) > 0]
    print(len(words))


def main():
    # problem1GCD()
    # problem2Vowels()
    # problem3("hello world", "o")
    # problem4("TodayIsCamelCase")
    problem5([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13,14,15,16]])
    # problem6(156651)
    # problem7("hello0123o123")
    # problem8(256)
    # problem9("Hello")
    # problem10("HI I AM    ")


if __name__ == "__main__":
    main()
