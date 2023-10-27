print("*"*50)
print(("Shared reference of mutable object").center(50))
a = [1,2,3]
b = [1,2,3]

print(a is b)
print(f" id of a is {hex(id(a))} -- content is {a}")
print(f" id of b is {hex(id(b))} -- content is {b}")


x = [1,2,3]
y = x

print(y is x)
print(f" id of x is {hex(id(x))} -- content is {x}")
print(f" id of y is {hex(id(y))} -- content is {y}")

print("*"*50)
print(("Shared reference of mutable object").center(50))
a = 1
b = 1

print(a is b)
print(f" id of a is {hex(id(a))} -- content is {a}")
print(f" id of b is {hex(id(b))} -- content is {b}")


x = 1
y = x

print(y is x)
print(f" id of x is {hex(id(x))} -- content is {x}")
print(f" id of y is {hex(id(y))} -- content is {y}")
print("*"*50)