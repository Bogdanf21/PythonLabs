from os import listdir
from os.path import isfile, join, isdir
import sys

path_argv = sys.argv[1]


def p4(path):
    set_ = set()
    queue = [path]
    while len(queue):
        directory = queue.pop(0)
        for f in listdir(directory):
            if isfile(join(directory, f)):  # and len(f.split(".")) > 1:  Pe linux pocneste pentru ca am si file-uri care nu-s directoare si totusi n-au extensie :(
                set_.add(f.split(".").pop())
            else:
                queue.append(join(directory, f))
    theList = list(set_)
    theList.sort()
    return theList

print("(4) :", p4(path_argv))

