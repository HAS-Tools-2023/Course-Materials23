## Exercises for thursday's class
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

# Exercise 1
# modify the following to create a pandas dataframe where the column 'datetime' is a datetime object. You should do this two ways: (1) by modifying the read.table function arguments directly. (2) keeping the read.table line I have below the same and modifying the dataframe after the fact. 
# How can you check to confirm that what you did worked? 
data = pd.read_table('streamflow_demo.txt', sep='\t',skiprows=30, names=['agency_cd', 'site_no',
                            'datetime', 'flow', 'code'])
print(data.info)
print(data.head())

#Method 1
data_datetime = pd.read_table('streamflow_demo.txt', sep='\t', skiprows=30, names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'], parse_dates=['datetime'], index_col='datetime')
print(data_datetime.info)
print(data_datetime.index)
print(data_datetime.head())

#Method 2
data['datetime'] = pd.to_datetime(data['datetime'])
print(data.info())
data = data.set_index('datetime')
print(data.info())
print(data.index)


# Exercise 2: 

#2.1: Read the 'daymet.csv' file in as a data frame using the 'date' column as the index and making sure to treat that column as a datetime object. 

daymet_df = pd.read_csv('daymet.csv', parse_dates=['date'], index_col=['date'])

#2.2: Explore this dataset and report what variables it contains, what date ranges are covered and the frequency of the data. 

# You can get the date ranges for the index using: 
daymet_df.info() 

# You can see the column names with either of the following tw approaches: 
daymet_df.head()
daymet_df.columns

# You can see the frequency of the data looking at the head command used above or by inspecting thi index like this: 
daymet_df.index

#2.3  Make a scatter plot of day length (dayl) vs maximum temperature. 
ax = plt.axes()
ax.scatter(daymet_df['dayl (s)'],
           daymet_df['tmax (deg c)'],  marker='o')
ax.set_xlabel('Day Length (s)')
ax.set_ylabel('Max Temp (deg c)')

plt.plot(daymet_df['dayl (s)'])

#2.4 Make a plot with lines for the monthly average of `tmax` for all months after Jan 2015.  Add shading to the plot extending to the monthly minimum and maximum of `tmax` for the same period.

#Hint - Use the pandas resample function for datetime objects and the plt.fill type for the shading.

mean_val = daymet_df.resample('M').mean()['tmax (deg c)']
min_val = daymet_df.resample('M').min()['tmax (deg c)']
max_val = daymet_df.resample('M').max()['tmax (deg c)']

mean_val_plot = mean_val[mean_val.index.year>=2015]
min_val_plot = min_val[min_val.index.year>=2015]
max_val_plot = max_val[max_val.index.year>=2015]

ax=plt.axes()
plt.plot(mean_val_plot, 'o-', color='blue', label='Mean')
plt.fill_between(max_val_plot.index, min_val_plot.values, max_val_plot.values, color='grey',  alpha=0.2, label='Max-Min')
ax.set_xlabel("Date")
ax.set_ylabel("Monthly Maximum daily temperature")
ax.legend()
