def talky2(some_function):
    def wrapper(*args, **kwargs):
        print("Oh hi!")
        print("The result sure is", str(some_function(*args, **kwargs)) + "!")
    return wrapper


def talky_with2(name):
    def peudo_decorator(some_function):
        def wrapper(*args, **kwargs):
            print("Oh hi", name +"!")
            print("The result sure is", str(some_function(*args, **kwargs)) + "!")
        return wrapper
    return peudo_decorator

if __name__ == "__main__":
    talky2()
    talky_with2()
