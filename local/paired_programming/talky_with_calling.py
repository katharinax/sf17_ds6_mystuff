from talky_with import talky2, talky_with2

@talky2 # i.e. talky(square)
def square(num):
    return num * num

print(square(5))

@talky_with2("Aaron")
def square(num):
    return num * num

print(square(5))
