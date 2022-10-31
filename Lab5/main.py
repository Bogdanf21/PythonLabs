import os
from collections import defaultdict
from os import listdir
from os.path import isfile, join, isdir


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
        elif isdir(path):
            tuples = []
            queue = [path]

            while queue:
                extensions = defaultdict(int)
                a_path = queue.pop(0)
                for f in listdir(a_path):
                    abs_path = join(a_path, f)
                    if isdir(abs_path):
                        queue.append(abs_path)
                    elif isfile(abs_path):
                        extension = path[path.rfind(".") + 1:]
                        extensions[extension] += 1

                for key in extensions.keys():
                    tuple = (key, extensions[key])
                    tuples.append(tuple)

            return tuples


    except FileNotFoundError as e:
        print(e)
    except NotADirectoryError as e:
        print(e)


def p5(target, to_search):
    try:
        if type(to_search) is not str:
            raise AttributeError("Argument is not a string")
        files = [target]
        valid_files = []

        if isfile(target):
            with open(target, 'r') as file:
                while line := file.readline().rstrip():
                    if to_search in line:
                        return [target]
        elif isdir(target):
            while files:
                root = files.pop(0)
                for f in listdir(root):
                    abs_path = join(root, f)
                    if isfile(abs_path):
                        with open(abs_path, 'r', errors="ignore") as file:
                            while line := file.readline().rstrip():
                                if line.find(to_search) != -1:
                                    valid_files.append(abs_path)
                                    break
                    else:
                        files.append(abs_path)
        else:
            raise ValueError("Target is neither a file or directory")
        return valid_files
    except FileNotFoundError as e:
        print(e)
    except AttributeError as e:
        print(e)
    except ValueError as e:
        print(e)


def p6(target, to_search, cb):
    try:
        if type(to_search) is not str:
            raise AttributeError("Argument is not a string")
        files = [target]
        valid_files = []

        if isfile(target):
            with open(target, 'r') as file:
                while line := file.readline().rstrip():
                    if to_search in line:
                        return [target]
        elif isdir(target):
            while files:
                root = files.pop(0)
                for f in listdir(root):
                    abs_path = join(root, f)
                    if isfile(abs_path):
                        with open(abs_path, 'r', errors="ignore") as file:
                            while line := file.readline().rstrip():
                                if line.find(to_search) != -1:
                                    valid_files.append(abs_path)
                                    break
                    else:
                        files.append(abs_path)
        else:
            raise ValueError("Target is neither a file or directory")
        return valid_files
    except FileNotFoundError as e:
        cb(e)
    except AttributeError as e:
        cb(e)
    except ValueError as e:
        cb(e)


def p7(path):
    try:
        if not isdir(path):
            raise NotADirectoryError("This is not a directory")

        to_be_returned = {"full_path": os.path.abspath(path), "file_size": os.stat(path).st_size}
        extension = path[path.rfind(".") + 1:]
        if len(extension) != len(path):
            to_be_returned["file_extension"] = extension
        to_be_returned["can_read"] = os.access(path, os.R_OK)
        to_be_returned["can_write"] = os.access(path, os.W_OK)
        return to_be_returned
    except NotADirectoryError as e:
        print(e)
        return None


def callback(e):
    print("There has been an exception: ", e)


def p8(dir_path):
    try:
        if not isdir(dir_path):
            raise NotADirectoryError("This is not a directory")
        queue = [dir_path]
        files = []
        while queue:
            path = queue.pop(0)
            for f in listdir(path):
                abs_path = join(path, f)
                if isfile(abs_path):
                    files.append(abs_path)
                elif isdir(abs_path):
                    queue.append(abs_path)
        return files

    except NotADirectoryError as e:
        print(e)
        return []


def main():
    print("Hello")
    print("(1) Extensia fisierelor: ", p1("/home/bogdan"))
    print("(2) Fisierele din dir/fisier care incep cu A:", p2("/home/bogdan", "Downloads/"))
    print("(3) Daca e un fisier tail pe ultimele 20 caractere:", p3("/home/bogdan/Downloads/test.txt"))
    print("(5)", p5("/home/bogdan/Downloads/", "xyz"))
    print("(6) p5 cu callback:")
    p6("/home/bogdan/Download", "xyz", callback)
    print("(7)")
    print(p7("/home/bogdan/Download"))
    print("(8)")
    print(p8("/home/bogdan/Documents/GitHub/PythonLabs"))


if __name__ == "__main__":
    main()
