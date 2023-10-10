# %%
import matplotlib.pyplot as plt
import matplotlib as mpl 
import numpy as np

# Getting help
# https://matplotlib.org
# https://matplotlib.org/gallery/index.html
# %%
# Setting styles
plt.style.use('classic')

x = np.linspace(-5 * np.pi, 5 * np.pi, 1000)
plt.plot(x,np.sin(x))

#opens up an interactive plotting window for you
plt.plot(x,np.sin(x))

# By default in vscode your plot will show up when you say plot
# but if you want it to show up when you run from command line too
# you need to say plt.show after
# you only need to  include  this once at the end of all your plotting
# not after every plot
plt.show() 

# Saving figure to file 
fig = plt.figure()
plt.plot(x, np.sin(x))
fig.savefig('test.png')



# %%
# Easy plotting 
# plt.plot and plt.scatter

#changing color and line type
plt.plot(x, np.sin(x), color= 'red', linestyle = 'dashed')
plt.plot(x, np.cos(x))

#changing the axes
plt.plot(x, np.sin(x), color= 'red', linestyle = 'dashed')
plt.plot(x, np.cos(x))
plt.xlim(-1,5)
plt.ylim(-2,2)  # can also flip  order to plot axes in reverse

# Add a title
plt.plot(x, np.sin(x), color= 'red', linestyle = 'dashed')
plt.plot(x, np.cos(x))
plt.title("my plot")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.xlim(-1,5)
plt.ylim(-2,2)  # cal also flip  order to plot axes in reverse

# Add a legend
plt.plot(x, np.sin(x), color= 'red', linestyle = 'dashed', label = 'sinx')
plt.plot(x, np.cos(x), label='cosx')
plt.title("my plot")
plt.xlabel("y")
plt.ylabel("sin(x)")
plt.xlim(-1,5)
plt.ylim(-2,2)  # cal also flip  order to plot axes in reverse
plt.legend()

# Changing this to points rather than lines
# Others to try; 'O, ., , , x, +, v, ^, <, >, s, d
plt.plot(x, np.sin(x), 'p', color= 'red')

# can combine with a line too
plt.plot(x, np.sin(x), 'd', color= 'red', linestyle = 'solid')

# and  then you could go all sorts of crazy
# for all the details do help(plt.plot())
plt.plot(x, np.sin(x), '-p', color= 'gray', 
        markersize=4, linewidth=1, 
        markerfacecolor='purple', markeredgecolor='black',
        markeredgewidth= '0.5')


#A better way to make scatter plots
# This is more powerful becauase you  can change the 
# properties of each point individually 

plt.scatter(x, np.sin(x), marker='o')

#for example having the color change with the x value
plt.scatter(x, np.sin(x), c=x, marker='o')

# or the size change with some random number
size=1000 * np.random.rand(len(x))
plt.scatter(x, np.sin(x), c=x, s=size,  marker=',')

# %%
# other kids of plots
x=np.linspace(0,10,50)
dy = 0.8
y=np.sin(x) + dy*np.random.randn(50)
plt.errorbar(x,y, yerr=dy, fmt='.k')

# or plot the error continuously as a line
plt.plot(x,y , 'or-')
plt.fill_between(x, y-dy, y+dy, color='grey',  alpha=0.2)

# histograms
x1=np.random.normal(0,0.8,10000)
x2=np.random.normal(-2,1,10000)
x3=np.random.normal(3,2,10000)

plt.hist(x1, bins=40, alpha=0.5, histtype='stepfilled',
        color='steelblue', edgecolor='purple')
plt.hist(x2, bins=40, alpha=0.5, histtype='stepfilled',
        color='green', edgecolor='purple')    
plt.hist(x3, bins=40, alpha=0.5, histtype='stepfilled',
        color='red', edgecolor='purple')   


# and we could combine the redundant stuff like this
kwargs = dict(bins=40, alpha=0.5, histtype='stepfilled',
         edgecolor='purple')
plt.hist(x1, **kwargs, color='blue')
plt.hist(x2, **kwargs, color='green')
plt.hist(x3, **kwargs, color='red')


# %%
# Figures and axes 
%matplotlib inline
fig = plt.figure(figsize=(6,6))
ax = plt.axes()
ax.plot(x, np.sin(x), color= 'red', linestyle = 'dashed', label = 'sinx')
ax.plot(x, np.cos(x), label='cosx')
ax.set_title("my plot")
ax.set_xlabel("y")
ax.set_ylabel("sin(x)")
ax.set_xlim(-1,5)
ax.set_ylim(-2,2) 
ax.legend()

# We can combine them nicely though like this
ax = plt.axes()
ax.plot(x, np.sin(x), color= 'red', linestyle = 'dashed', label = 'sinx')
ax.plot(x, np.cos(x), label='cosx')
ax.set(title="my plot", xlabel="y", ylabel="sin(x)",
             xlim=(-1,5), ylim=(-2,2)) 
ax.legend()

# %%
# Alternate matplotlib style
# Style 1: 
# creating figue and Axes objects for a figure with 
# two subplots 
fig,ax = plt.subplots(2,1)
# then we refer to these  objects when we want to do the plotting
ax[0].plot(x, np.sin(x))
ax[1].plot(x, np.cos(x))


# Style 2: 
# State type approach -- You activate a subplot and then 
# plot things to it
plt.figure()
plt.subplot(2,1,1)
plt.plot(x,np.sin(x))
plt.subplot(2,1,2)
plt.plot(x, np.cos(x))


# Another example witha biger grid
fig,ax = plt.subplots(2,2)
ax = ax.flatten() #necessary because of the structure of the ax 
# then we refer to these  objects when we want to do the plotting
ax[0].plot(x, np.sin(x))
ax[1].plot(x, np.cos(x))
ax[2].plot(x, np.sin(x))
ax[3].plot(x, np.cos(x))


#Accomplishing the same thing as the previous one
# but without the ax.flatten command
fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(2,2)
ax1.plot(x, np.sin(x))
ax2.plot(x, np.cos(x))
ax3.plot(x, np.sin(x))
ax4.plot(x, np.cos(x))
# %%
