import sys

# print(len(sys.argv))

if len(sys.argv) == 1:
    print("Please provide your name in command")
elif len(sys.argv) == 2:
    first_name = sys.argv[1]
    print("Hello " + first_name + "!!!")
else:
    first_name = sys.argv[1]
    second_name = sys.argv[2]
    print("Hello " + first_name + " " + second_name + "!!!")