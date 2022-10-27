from os import listdir
from os.path import isfile, join


def p1(path):
    try:
        files = list(set(f.split(".").pop() for f in listdir(path) if isfile(join(path, f)) and len(f.split('.')) > 1))
        files.sort()
        return files
    except FileNotFoundError as e:
        print(e)
        return []
    except NotADirectoryError as e:
        print("Is not a directory: ", path)
        return []


def p2(path, file):
    files = []
    root = join(path, file)
    try:
        for f in listdir(root):
            abs_path = join(root, f)
            if isfile(abs_path) and len(f) > 0 and f[0] == 'A':
                files.append(abs_path)
        return files
    except FileNotFoundError as e:
        print(e)
        return []
    except NotADirectoryError as e:
        print("Is not a directory: ", join(path, file))
        return []

def p3(path):
    try:
        if isfile(path):
            with open(path, 'r') as f:
                lines = f.readlines()
                last = lines.pop()[::-1]
                last = last[0:20:1]
                last = last[::-1]
                return last
        else:
            tupleCount = 0

            for f in listdir(path):
                print("helio")

    except FileNotFoundError as e:
        print(e)



def main():
    print("Hello")
    print("(1) Extensia fisierelor: ", p1("/home/bogdan"))
    print("(2) Fisierele din dir/fisier care incep cu A:", p2("/home/bogdan", "Downloads/"))
    # print("(3) Daca e un fisier tail pe ultimele 20 caractere:", p3("/home/bogdan/Downloads/test.txt"))

if __name__ == "__main__":
    main()
