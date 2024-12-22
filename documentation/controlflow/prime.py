import sys

if len(sys.argv) == 1:
    print("invalid argument")
    quit()

input = int(sys.argv[1])

for x in range(2, int(input**0.5)+1):
    if(input % x == 0):
        break
else:
    print(str(input) + " is a prime number")