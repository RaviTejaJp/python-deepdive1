print("*"*100)
print(("Checking *is* operator").center(50))

print("is"*50)
print(("Checking with immutable objects").rjust(40))

print("FYI : We can not count of address of immutable \
objects like string being same implicitly in some \
conditions (like Very big string).")

a = "Hello"
b = "Hello"
print(a is b)


x = 3
y = 3
print(x is y)

print("Example: This immutable objects will have different addresses as they are big")
a = "Hello"*1000
b = "Hello"*1000
print(a is b)
print("is"*50)

print("*"*100)
print(("Checking *==* operator").center(50))

print("=="*50)
print(("Checking with immutable objects").rjust(40))

a = "Hello"
b = "Hello"
print(a == b)


x = 3
y = 3
print(x == y)

print("Example: This immutable objects will have different addresses as they are big but as values are same we get true")
a = "Hello"*1000
b = "Hello"*1000
print(a == b)
print("=="*50)
print("*"*100)
