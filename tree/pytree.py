#!/usr/bin/env python3
import subprocess
import sys
import os
import re


indent = "│   "
indent_end = "    "
branch = "├── "
branch_end = "└── "


def process_path(path):
    children = os.listdir(path)
    children = [children for children in children if children[0] != '.']
    children.sort()
    return children


def process_dir(new_path, counts, is_end, padding):
    counts[0] = counts[0] + 1
    if (is_end):
        padding = padding + indent_end
    else:
        padding = padding + indent
    print_tree(new_path, counts, padding)
    padding = padding[:-4]


def print_tree(path, counts, padding=""):
    children = process_path(path)
    for i in range(0, len(children)):
        is_end = False
        if (i == len(children) - 1):
            is_end = True
            print(padding + branch_end + children[i])
        else:
            print(padding + branch + children[i])
        new_path = os.path.join(path, children[i])
        if (os.path.isdir(new_path)):
            process_dir(new_path, counts, is_end, padding)
        else:
            counts[1] = counts[1] + 1


if __name__ == '__main__':
    if (len(sys.argv) > 2):
        print("Invalid arguments.")
        sys.exit()
    counts = [0, 0]
    path = "."
    if len(sys.argv) == 2:
        path = sys.argv[1]
    print(path)
    print_tree(path, counts)
    print()
    dir_str = "directories"
    file_str = "files"
    if (counts[0] == 1):
        dir_str = "directory"
    if (counts[1] == 1):
        file_str = "file"
    print("{} {}, {} {}".format(counts[0], dir_str, counts[1], file_str))
