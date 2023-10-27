print("*"*100)
print("Everything in Python is Object")

print(" i.e. Functions are objects , Classes are objects, Data Types are Objects")
print(" Any objects can be assigned to variable, passed to functions, returned by functions")

print(("Functions").center(50))
print("*functions*"*(100//len("functions")))
def function1():
    pass

print(f"id of function: {hex(id(function1))} -- contents: {function1}  -- type: {type(function1)}")

print("!"*100)
print(f"Example Function returning a function")
def square(number):
    return number ** 2

def cube(number):
    return number ** 3

def select_function(number):
    if number == 0:
        return square
    elif number == 1:
        return cube
    else:
        return square
    
result = select_function(1)(5)
print(f" result from function selection : {result}")
print("!"*100)

print("*functions*"*(100//len("functions")))