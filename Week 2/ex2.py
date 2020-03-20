import sys
import getopt
from module import listdir

#1a
def print_file_content():
    for line in open("read.csv"):
        print(line)

#print_file_content()

#1b
def write_list_to_file(output_file, *lst):
    f2w = open(output_file, "w")

    for arg in lst:
        f2w.write(arg)
    
    f2w.close()

write_list_to_file("hello.txt", "Hej ", "med ", "dig ")

def read_csv():

    pathToFile = None
    shouldWrite = None
    buffer = ""
    argv = sys.argv[1:]

    try:
        opts, args = getopt.getopt(argv, "p:fh", ["path=", "file=", "help"])
    except getopt.GetoptError as error:
        print(error)
        opts = []


    for opt, arg in opts:

        if opt in ['--help']:
            print("usage: --path to choose what file to read from. example: --path hello.txt")
            print("usage: --file (OPTIONAL) to choose what file to read to. example: --file output")
            break

        if opt in ['--path']:
            pathToFile = arg

        elif opt in ['--file']:
            shouldWrite = arg


    if shouldWrite != None:
        try:
            for line in open(pathToFile, "r+"):
                buffer += line

            write_list_to_file(shouldWrite + ".txt", buffer)
        except Exception as error:
            print(error)
    else:
        try:
            for line in open(pathToFile, "r+"):
                print(line)
        except Exception as error:
            print(error)
        


    #with open(input_file) as f:
    #    for i, line in enumerate(f):             
    #        print(str(i) + " = " + str(line.split()))

read_csv()

#opgave 2

print(listdir("C:\\Users\\Martin\\Desktop\\ex2\\week2"))