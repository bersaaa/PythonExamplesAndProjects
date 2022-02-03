""" Making an equilateral triangle with '*' """
number=10
for i in range(number):
    print(" "*(number-1-i)+"* "*(i+1))

""" Examples of the use of *kwargs and *args kakas are given below. """
# *args for variable number of arguments
def even(*args):
    print([f'{n} is even' for n in args if n % 2 ==0])
    
even(1,2,3,4,5,6,7,8,9)

# *kwargs for variable number of keyword arguments

def test2(**kwargs):
    print(sum(kwargs.values()))

test2(a = 1 , b = 3 , c = 5 , d = 7)

"""
Make a decorator from the time library with sleep. then check which one works faster between try except and while true with this decarator and get the output.
"""

import time 

def sleep(func):
    def wrapper(*args):
        time.sleep(0.5)
        return func(*args)
    return wrapper
    

def benchmark(func):
    @sleep
    def wrapper(*args,**kwargs):
        timeStart=time.time()
        result=func(*args,**kwargs)
        deltatime=time.time() - timeStart
        print(f'{deltatime:.20f}')
        return result
    return wrapper

@benchmark

def tamBolenleriBul(sayi):
    tamBolenler = []
    for i in range(2,sayi):
        if (sayi % i == 0):
            tamBolenler.append(i)
            
    return tamBolenler

print(tamBolenleriBul(100))

"""
Create a set with 1000 elements, a dictionary with 1000 elements, a list with 1000 elements.
Write and write the program that calculates the mean for these three different variables.
Show it with your program time decorator that will show which one is running faster.
"""

tuple_a = set((i for i in range(1000)))
a = iter(set([i for i in range(2000)]))
dict_a = dict(zip(a,a))

list_a = [i for i in range(1000)]

@benchmark
def average_tuple(nums):
    return (sum(int(x) for x in tuple_a)/len (tuple_a))

print("Tuple")
print(average_tuple(tuple_a))

@benchmark
def average_list(lst):
    return sum(lst)/len(lst)
print("List")
print(average_list(list_a))

@benchmark
def average_dict(b):
    filtered_vals=[v for _ , v in b.items() if v != 0]
    return sum(filtered_vals)/len(filtered_vals)

print("Dict")
print(average_dict(dict_a))


