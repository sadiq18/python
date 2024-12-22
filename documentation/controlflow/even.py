num = input("enter an integer : ")

try:
    num = int(num)
except:
    print("invalid number")
    quit()

if num%2 == 0:
    print("Even number")
else:
    print("Odd number")
