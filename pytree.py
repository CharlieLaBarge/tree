#!/usr/bin/env python3
import subprocess
import sys
import os
import re
import string

root_dir = ""

# YOUR CODE GOES here

# Set the root_dir that the command is going to be called on
if len(sys.argv) == 1:
    root_dir = "."
    print(root_dir)
else:
    root_dir = str(sys.argv[1])
    print(root_dir)


def sortRight(string_list):
    new_list = []

    for astring in string_list:
        new = ""
        for i, c in enumerate(astring):
            if str(c).isalnum():
                new = new + c
        new_list.append(new.lower())

    mapping = dict(zip(new_list, string_list))
    new_list.sort()

    new_new_list = []
    for i in new_list:
        new_new_list.append(mapping.get(i))

    return new_new_list


def printTree(root_dir, level, current_indent):
    dirlist = os.listdir(root_dir)

    numfiles = 0
    numdirs = 0

    newdirs = []
    for i, name in enumerate(dirlist):
        if not (name[0] == '.'):
            newdirs.append(name)

    dirlist = newdirs

    treelen = len(dirlist)
    dirlist = sortRight(dirlist)

    index = 0
    for name in dirlist:
        indent = current_indent
        if not (name[0] == "."):  # if the file is not hidden
            if not (os.path.isdir(root_dir + "/" + name)):
                numfiles += 1

                if (index != treelen - 1):  # for every line except the last one
                    print(indent + "\u251c\u2500\u2500 " + name)
                else:
                    print(indent + "\u2514\u2500\u2500 " + name)
            else:
                numdirs += 1

                if (index != treelen - 1):  # for every line except the last one
                    print(indent + "\u251c\u2500\u2500 " + name)
                    indent = indent + "\u2502   "
                else:
                    print(indent + "\u2514\u2500\u2500 " + name)
                    indent = indent + "    "

                new_numdirs, new_numfiles = printTree(root_dir + "/" + name, level + 1, indent)

                numfiles += new_numfiles
                numdirs += new_numdirs

        index += 1

    return numdirs, numfiles

numdirs, numfiles = printTree(root_dir, 0, "")
print("\n" + str(numdirs) + " directories, " + str(numfiles) + " files")
