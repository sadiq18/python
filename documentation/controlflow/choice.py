

input = int(input("enter number : "))

match input:
    case 0:
        print("zero")
    case 1:
        print("One")
    case 2:
        print("Three")
    case _:
        # underscore repersent default
        print("more")