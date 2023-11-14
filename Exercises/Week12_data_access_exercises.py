# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os
import dataretrieval.nwis as nwis

# %%
# Exercise 1: 
# 1. Write a function that takes the following arguments as inputs: 
# - USGS Station ID
# - Start Date of desired observations
# - End Date of desired observations
# And returns a dataframe with the USGS streamflow for the desired location and date range. 

# 2. Select two other gauges on the Verde River (https://maps.waterdata.usgs.gov/mapper/index.html) and use your function to download the data for all three gauges for the past year (The two you select plus 09506000). 


#3. Make a timeseries plot showing the data from all 3 gauges. 

