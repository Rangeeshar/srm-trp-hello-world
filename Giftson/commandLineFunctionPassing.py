""" Simple Python program to use command line argument to call a function with parameters """
import sys

# function conPrint to print the 3rd argument as the output
def conPrint():
    print(sys.argv[2])


# directly calling the 2nd argument as a function using globals()
if __name__ == "__main__":
    if len(sys.argv) > 2:
        globals()[sys.argv[1]]()
    else:
        print("Parameters are not provided")
