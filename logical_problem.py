""" 
A trio of brothers had to travel 300 kms 

-> each of them can walk with 15 km/h speed
-> they had a bike that can go with speed of 60 km/h speed

-> what is the minimum time that they need to travel
"""

def calculate_time(speed: float,distance: float) -> float:
    return distance / speed

def calculate_speed(time: float,distance: float) -> float:
    return distance / time

def calculate_distance(speed: float,time: float) -> float:
    return time * speed

from sympy import symbols, Eq, solve

x,y,z = symbols("x,y,z")

eq1 = Eq((x+y+z),300)
eq2 = Eq((2*y-3*z),0)
eq3 = Eq((5*y+3*z),900)
distances = solve((eq1, eq2, eq3), (x, y, z))
print(type(distances))
time_1 = calculate_time(speed=15,distance=distances[x])
time_2 = calculate_time(speed=60, distance= distances[y]+distances[z])

print(float(time_1+time_2))
