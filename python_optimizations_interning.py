import sys
print("Python preloads certain range of integers and when we try to create them instead of creating them we get referenced to them")
print("Example: Python preloads integers [-5,256]")
a= -5
b = -5
print(a is b)

a= -6
b = -6
print(a is b)

a= 256
b = 256
print(a is b)

a = 257000000099999999999
b = 257000000099999999999
print(a is b)

# String Interning

print("="*80)
print("String Interning")
a = "abcdefghijklmnopqrstuvwxyz"
b = "abcdefghijklmnopqrstuvwxyz"
print(a is b)

x = "@2_ abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ again"
y = "@2_ abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ again"
print(x is y)