try:
    raise KeyboardInterrupt("testing-2")
except:
    print("handled")
finally:
    print("final")


try:
    raise KeyboardInterrupt("testing")
finally:
    print("Bye")
    quit() # don't let stack traced print

print("Unreachable code")
