def adder(n):
    def inner(x):
        return x+n
    return inner

adders = []
for i in range(0,5):
    adders.append(adder(i))

for item in adders:
    print(item(10))
    
adders_2 = []
for i in range(0,5):
    adders_2.append(lambda x: x + i)

for item in adders_2:
    print(item(10))