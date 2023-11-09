#Setup- before you start create a new 'mapping' environment following the instructions from class and make sure you have the following packages installed
import matplotlib.pyplot as plt
import matplotlib as mpl 
import pandas as pd 
import numpy as np
import geopandas as gpd

# %%
# Exercise 1: 
# 1. Open the arizona_huc8_shapefil and the arizona_shapefile following the example we did in class. 
file =  os.path.join('../data/arizona_huc8_shapefile', 'WBDHU8.shp')
huc8 = gpd.read_file(file)


file =  os.path.join('../data/arizona_shapefile', 'tl_2016_04_cousub.shp')
state = gpd.read_file(file)

# 2. Explore their properties and attributes and be able to explain (1) what type of geometry each is, (2) how many features there are, (3) what attributes each feature has. 
huc8.head()
huc8.columns
huc8.shape #seeing how many entries there are
huc8.geom_type

state.head()
state.columns
state.shape #seeing how many entries there are
state.geom_type


# 3. Plot each dataset. You can plot them separately but also try plotting subsets and plotting them on top of each other. 

fig, ax = plt.subplots(figsize=(10, 10))
huc8.plot(ax=ax)
plt.show()

fig, ax = plt.subplots(figsize=(10, 10))
state.plot(ax=ax)
plt.show()


#%%
# Exercise 2:
# Exercise 2: 
# 1. Open the WBD_15_HU2_GDB geodatabase and select a different layer to plot than the one I showed (i.e. not HUC6)

# 2. Create a geodatabase with the two points of interest I showed (i.e. UA and the stream gauge) as well as two additional points of your choosing

#3. Make a map of your selected datasets. If you have time experiment with changing the markers and lines/fill colors on your plot 