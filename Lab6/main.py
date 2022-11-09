import utils as ut
import app

anonymous = lambda *x, **y: sum(i for a, i in y.items())
anonymous_check = lambda input_string: list(i for i in input_string if i in "aeiou")


def not_anonymous(*x, **y):
    return sum(i for a, i in y.items())


def check_if_vowel(input_string):
    vowels = "aeiou"
    letters_found = []
    for letter in input_string:
        if letter in vowels:
            letters_found.append(letter)
    return letters_found


def ex4(*arguments, **keyword_arduments):
    valid_dictionaries = []
    for possible_dictionary in arguments:
        add = False
        if type(possible_dictionary) is dict:
            if len(possible_dictionary) >= 2:
                for key, value in possible_dictionary.items():
                    if type(key) is str and len(key) >= 3:
                        add = True
        if add:
            valid_dictionaries.append(possible_dictionary)
    for key, possible_dictionary in keyword_arduments.items():
        add = False
        if type(possible_dictionary) is dict:
            if len(possible_dictionary) >= 2:
                for (key_second, value) in possible_dictionary.items():
                    if type(key_second) is str and len(key_second) >= 3:
                        add = True
        if add:
            valid_dictionaries.append(possible_dictionary)
    return valid_dictionaries


def ex5(given_list, numbers_found):
    for item in given_list:
        if type(item) is int or type(item) is float:
            numbers_found.append(item)
        if type(item) is dict:
            for key, value in item.items():
                if type(key) is int or type(item) is float:
                    numbers_found.append(item)
                if type(value) is int or type(value) is float:
                    numbers_found.append(value)
                if type(value) is dict or type(value) is list or type(value) is set:
                    ex5(value, numbers_found)
        if type(item) is list or type(item) is set:
            for i in item:
                if type(i) is int or type(i) is float:
                    numbers_found.append(i)
                if type(i) is dict or type(i) is list or type(value) is set:
                    ex5(i, numbers_found)


def ex6(given_list):
    odd_position = 0
    even_position = 0
    tuples = []
    while len(tuples) != len(given_list) / 2:
        while given_list[odd_position] % 2 == 0:
            odd_position += 1
        odd_number = given_list[odd_position]
        while given_list[even_position] % 2 != 0:
            even_position += 1
        even_number = given_list[even_position]
        tuples.append((even_number, odd_number))
        odd_position += 1
        even_position += 1
    return tuples



def print_arguments(function):
    print(function)


def multiply_by_two(x):
    return x * 2


def add_numbers(a, b):
    return a + b


def ex9(pairs):
    output = []
    for item in pairs:
        partial_dict = {}
        partial_dict['sum'] = item[0] + item[1]
        partial_dict['prod'] = item[0] * item[1]
        partial_dict['pow'] = item[0] ** item[1]
        output.append(partial_dict)
    return output


if __name__ == '__main__':
    # 1
    x = int(input("Insert number : "))
    print("(1.a) --> ", ut.process_item(x))
    print("(1.b)")
    app.run()
    # 2
    print("(2): ", {anonymous(1, 2, c=3, d=4)})
    print(f"(2 not anonymous)", not_anonymous(1, 2, c=3, d=4))
    # 3
    output = check_if_vowel("Programming in Python is fun")
    print("(3) function:", output)
    output2 = anonymous_check("Programming in Python is fun")
    print("(3) anonymous function:", output2)
    output3 = [i for i in "Programming in Python is fun" if i in "aeiou"]
    print("(3) list comprehension", output3)
    # 4
    print(ex4({1: 2, 3: 4, 5: 6}, {'a': 5, 'b': 7, 'c': 'e'}, {2: 3}, [1, 2, 3], {'abc': 4, 'def': 5}, 3764,
              dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'}, test={1: 1, 'test': True}))
    # 5
    numbers_found = []
    ex5([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0], numbers_found)
    print("(5)", set(numbers_found))
    # 6
    print("(6)", ex6([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))
    # 9
    print(ex9([(5, 2), (19, 1), (30, 6), (2, 2)]))
