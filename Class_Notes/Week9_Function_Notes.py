import numpy as np
import matplotlib.pyplot as plt

#%%
# This is a function that prints a statment. We define it like this: 
def my_function():
  print("Hello from a function")

#and we use it like this: 
my_function()

# %%
#The function above didn't really do anything and it didn't have any arguments. Here is a function that has arguments

# Here I define it
def add_two(a,b):
  answer=a+b
  return(answer)

# and here I use it and save the output as a variable
my_sum = add_two(4,6)


# %%
# I can also write functions that return more than one thing

def two_outputs(a,b):
  ans1=a+b
  ans2=a*b
  return ans1, ans2

#We can use it like this: 
my_two=two_outputs(5,5)

#if you inspect my_two you will see it has two entries. we could also store this as two separate things like this: 

my_one, my_two = two_outputs(5,5)

# %%
# You can also have your return statement change based on different conditions
def my_abs(number):
    if number > 0:
        return number
    elif number < 0:
        return -number

my_abs(-15)
my_abs(15)

# %%
# And you can have your inputs have default values in case so the user doesn't always have to enter them all
def add_two(a, b=1):
  answer = a+b
  return(answer)

#Since b defaults to 1 if I just give it one value as input it will do 5 +1
add_two(5)

# I can still define b to be whatever I want though if I give the function two inputs
add_two(5, 3)

#%%
# A little tricker we can also write a function to create a figure like this
x = np.linspace(-5 * np.pi, 5 * np.pi, 1000)

def plot_sin(x):
    fig = plt.figure()
    plt.plot(x, np.sin(x))
    plt.show()
    return fig


fig = plot_sin(x)
fig.savefig('test.png')



