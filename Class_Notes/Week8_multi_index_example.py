#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#%% Import the flow data to use
data = pd.read_table("./streamflow_demo.txt",  sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'])
data[["year", "month", "day"]] = data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

# %%
# OPTION1: This takes the max of every column 
all_max = data.groupby(data.month).max()
#Then we can grab out the flow like this:
all_flow=all_max['flow']

#and we can plot it like this
#note for the x values we refer to this as index not 'month' and the flow values are 'values' because there is no column name any more
f, ax = plt.subplots()
ax.bar(all_flow.index,
       all_flow.values,
       color="purple")

# You could also plot it like this
# Here I'm using 'all_max' and the plotting the flow column as opposed to plotting the 'values' of all_flow 
f, ax = plt.subplots()
ax.bar(all_max.index,
       all_max.flow,
       color="purple")

#%%
#OPTION 2: This just takes the max of the flow column by adding the 'flow' column specification to the grouby call
groupby_flow_max = data.groupby(data.month)["flow"].max()

f, ax = plt.subplots()
ax.bar(groupby_flow_max.index,
       groupby_flow_max.values,
       color="purple")

#%%
#OPTION 3: Use the describe function on the flow column which will calculate many statistics all at once including the max
# NOTE if you inspect this object you will see it has multople headers now
flow_describe = data.groupby(["month"])[["flow"]].describe()
#This doesn't work
flow_describe['max']
#to see why lets look at the column names for flow_decribe
print(flow_describe.columns)
#Note that there are two levels to this flow and then each of the values we want. 
# To get out the value we want we have to say 
flow_describe['flow', 'max']

# Alternatively we could get rid of this heirarchy like this: 
flow_describe.columns = flow_describe.columns.droplevel(0)
print(flow_describe.columns)
#After doing the drop level command we can now do this and it will work: 
flow_describe['max']

#now we can plot it. Note that fore the x values we are using '.index' because the months are now the index of our dataframe
ax.set(title="Bar Plot of Seasonal Monthly Precipitation in mm")
f, ax = plt.subplots()
ax.bar(flow_describe.index,
       flow_describe["max"],
       color="purple")


#%%
#OPTION 4: The same as option 3 but this time applied to all the columns not just flow
all_describe = data.groupby(["month"]).describe()
all_describe.columns

# what happens if we do the same type of consolidation we did before? This does not work very well. Why? 
all_describe.columns = all_describe.columns.droplevel(0)

## instead we could keep the heirarcy in place and 
all_describe = data.groupby(["month"]).describe()
all_describe.columns
all_describe['flow', 'max']

f, ax = plt.subplots()
ax.bar(all_describe.index,
       flow_describe['flow', 'max'],
       color="purple")
