try:
    raise Exception('abc', "test")
except Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)