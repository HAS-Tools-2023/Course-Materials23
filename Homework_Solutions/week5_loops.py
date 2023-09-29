# Starter code for Homework 4

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week2.txt'
filepath = os.path.join('../data', filename)
print(os.getcwd())
print(filepath)

# %%
# DON'T change this part -- this creates the lists you 
# should use for the rest of the assignment
# no need to worry about how this is being done now we will cover
# this in later sections. 

#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=31,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

# Make a numpy array of this data
flow_data = data[['year', 'month','day', 'flow']].to_numpy()

# Getting rid of the pandas dataframe since we wont be using it this week
del(data)

# %%
# 1. Create a new numpy array that has the same four columns as flow_data (i.e. year, month, day, flow) but includes only the data for 1/1/2015-12/31/2019. Call your new array flow_5yr. Print out the dimensions of flow_5yr along with the total flow in this period

#Option 1 Using 2 lines of code
pick_list = (flow_data[:, 0] >= 2015) & (flow_data[:, 0] <= 2019)
flow_5yr = flow_data[pick_list, :]
print("The dimensions of flow_5yr are", flow_5yr.shape, "and the total flow is", np.sum(flow_5yr[:,3]))

#Option 2 Using 1 lines of code
flow_5yr2 = flow_data[(flow_data[:, 0] >= 2015) & (flow_data[:, 0] <= 2019), :]
print("The dimensions of flow_5yr are", flow_5yr.shape,
      "and the total flow is", np.sum(flow_5yr[:, 3]))

#Option 3 usnig a for loop
flow_5yrloop=np.zeros((len(flow_5yr[:,1]),4))
nday=len(flow_data[:,1]) #count up the number of rows in flow_data
j=0

for i in range(nday):
    if flow_data[i,0]>= 2015 and flow_data[i,0]<=2019:
        flow_5yrloop[j,] = flow_data[i, :]
        j=j+1
print("The dimensions of flow_5yr are", flow_5yr.shape, "and the total flow is", np.sum(flow_5yr[:,3]))  


# 2. Convert the daily average flow from cubic feet per second to cubic feet. Do this two ways, first without using a for loop and second with using a for loop. Save this a a variable called flow_daily and print out the total flow for the entire time period. 

#First without a loop
flow_daily = flow_5yr[:,3]*60*60*24
print("The total flow in cubic feet is",  np.sum(flow_daily))

#Now with a loop (note I'm showing two ways of doing this here)
nday=len(flow_5yr[:,1])
flow_daily=[] #example 1 just creating a blank array and I will add to it as I go
flow_daily2=np.zeros(nday) #example 2 making an array of zeros that I will insert numbers into
for i in range(nday):
    flow_daily = np.append(flow_daily, flow_5yr[i, 3]*60*60*24)
    flow_daily2[i]=flow_5yr[i,3]*60*60*24
  
print("The total flow in cubic feet is",  np.sum(flow_daily))


# 3. Create a time series of monthly average flow from the daily flow values (i.e. I'm looking for a timeseries that is 60 months long (12 months & 5 years)). You should store this in a numpy array that has 60 rows and three columns. The first column should be year, the second month and the third should be flow. 

# HINT1: I would first create an array that has just the months and year values in it an then loop over that to fill in the flow values
#You can create values from 1-12 and repeate those values 5 times to fill in the months using the functions np.arange and np.tile
flow_monthly = np.zeros((60, 3))
months = np.tile(np.arange(1, 13, 1), 5)

# You can then repeat each of the year values 12 times using the function np.arrange and np.repeat
years=np.repeat(np.arange(start=2015, stop=2020, step=1),12)

flow_monthly[:,0]=years
flow_monthly[:,1]=months
nmonth=60

for m in range(nmonth):
    ytemp= flow_monthly[m,0]
    mtemp= flow_monthly[m,1]
    ipick=(flow_data[:,0]==ytemp) & (flow_data[:,1]==mtemp)
    flow_monthly[m,2]=np.mean(flow_data[ipick, 3])
    print('Step', m, 'Year=', ytemp, "Month=", mtemp, "flow", flow_monthly[m,2])

flow_monthly 

