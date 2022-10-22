from collections import defaultdict


def p1(a, b):
    a_intersected_b = set(item for item in a if item in b)
    a_reunited_b = set(a + b)
    a_minus_b = set(item for item in a if item not in b)
    b_minus_a = set(item for item in b if item not in a)

    return a_intersected_b, a_reunited_b, a_minus_b, b_minus_a


def p2(string):
    dictionary = defaultdict(int)
    for character in string:
        dictionary[character] += 1
    return dict(dictionary)


def p3(dictionary1, dictionary2):
    print("Hello world")


def p4(tag, content, **pairs):
    string = f'<{tag} '
    for key, value in pairs.items():
        string += f'{key}=\\\"{value}\\\"'
    string += f'>{content} </{tag}>'
    return string


def p5():
    print("Hello world")


def p6(a_list: []):
    duplicates = set()
    uniques = set()

    set_from_list = set(a_list)
    for item in set_from_list:
        a_list.remove(item)
    duplicates = set(a_list)
    uniques = set(item for item in set_from_list if item not in duplicates)
    return len(uniques), len(duplicates)


def p7(*sets):
    dictionary = {}
    if len(sets) % 2 == 1:
        print("Cannot return dictionary: set does not have an even card.")
        return
    for i in range(0, len(sets), 2):

        a_intersected_b, a_reunited_b, a_minus_b, b_minus_a = p1(list(sets[i]), list(sets[i+1]))
        dictionary[f'{sets[i]} | {sets[i+1]}'] = a_reunited_b
        dictionary[f'{sets[i]} $ {sets[i+1]}'] = a_intersected_b
        dictionary[f'{sets[i]} - {sets[i + 1]}'] = a_minus_b
        dictionary[f'{sets[i+1]} - {sets[i]}'] = b_minus_a
    return dictionary





def p8(dictionary):
    key = "start"
    visited = []

    while dictionary[key] not in visited:
        visited.append(dictionary[key])
        key = dictionary[key]
    return visited


def p9(*positional_arguments, **keyword_arguments):
    positional = set(positional_arguments)
    keyword = set(i[1] for i in list(keyword_arguments.items()))

    return len(list(a for a in positional if a in keyword))




def main():
    # p1: sets a,b -> aUb a^b a/b b/a
    a = [1, 2, 3]
    b = [2, 3, 5]
    print("(1) sets:", p1(a, b))

    # p2: string and return dict with frequency
    print("(2) number of occurences in string:", p2("Ana has apples."))

    # p3:

    # p4: build xml element:
    print("(4) build xml element:",
          p4("a", "Hello There", href=" http://python.org ", _class=" my-link ", id=" someid"))

    # p5

    # p6:
    a_list = [1, 2, 2, 3]
    print("(6) number of duplicates/uniques in list:", p6(a_list))

    # p7: sets and give them in a dictionary
    print("(7) Variable numbers of sets and returns the dictionary:", p7({1, 2}, {2, 3}))

    # p8: dictionary and iterate through it
    p8dict = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
    print("(8) Dictionary and iterate through it:", p8(p8dict))

    # p9: Write a function that receives a variable number of positional arguments and
    # a variable number of keyword arguments adn will return the number
    # of positional arguments whose values can be found among keyword arguments values.
    print("(9)", p9(1, 2, 3, 4, x=1, y=2, z=3, w=5))



if __name__ == "__main__":
    main()
