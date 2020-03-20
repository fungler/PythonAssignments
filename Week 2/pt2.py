from sys import argv
import csv
import platform
import argparse
import os.path
from os import path

import ex2

#exercise a
def write_filenames_to_file(folderpath):
    entries = os.listdir(folderpath)
    ex2.write_list_to_file('csvfile.csv', entries)

#exercise b
lst = []
def write_filenames_to_file_recursive(folderpath):

    root = folderpath
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            lst.append(os.path.join(root, name))
        for name in dirs:
            lst.append(os.path.join(root, name))
    ex2.write_list_to_file('csvfile.csv', lst)


#exercise c
def read_first_line_from_files(*files):
    print(files)
    for file in files:
        for ele in file:
            with open(ele) as f_obj:
                content = f_obj.readline()
                print(content)

#exercise d
def print_lines_with_email(*files):
    for file in files:
        for ele in file:
            with open(ele) as f_obj:
                content = f_obj.readlines()
            for line in content:
                if '@' in line:
                    print(line.rstrip())

#exercise e
def print_lines_with_markdown(*files):
    for file in files:
        for ele in file:
            with open(ele) as f_obj:
                content = f_obj.readlines()
            for line in content:
                if '#' in line:
                    lst.append(line)
    ex2.write_list_to_file('csvfile.csv', lst)

def run2():
    if args.exerciseA:
        folderpath = argv[2]
        write_filenames_to_file(folderpath)
    if args.exerciseB:
        folderpath = argv[2]
        write_filenames_to_file_recursive(folderpath)
    if args.exerciseC:
        files = argv[2:]
        read_first_line_from_files(files)
    if args.exerciseD:
        files = argv[2:]
        print_lines_with_email(files)
    if args.exerciseE:
        files = argv[2:]
        print_lines_with_markdown(files)




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="------------Handles Files - Exercise 2------------")
    parser.add_argument("-a","--exerciseA", help="takes a path to a folder and writes all filenames in the folder to a specified output file")
    parser.add_argument("-b","--exerciseB", nargs='*', help="takes a path to a folder and write all filenames recursively (files of all sub folders to)")
    parser.add_argument("-c","--exerciseC",  help="takes a list of filenames and print the first line of each")
    parser.add_argument("-e","--exerciseD",  help="takes a list of filenames and print each line that contains an email (just look for @)")
    parser.add_argument("-f","--exerciseE",  help="takes a list of md files and writes all headlines (lines starting with #) to a file Make sure your module can be called both from cli and imported to another module Create a new module that imports utils.py and test each function.")
    args = parser.parse_args()
    run2()