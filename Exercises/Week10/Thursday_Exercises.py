## Exercises for thursday's class

# Exercise 1
# modify the following to create a pandas dataframe where the column 'datetime' is a datetime object. You should do this two ways: (1) by modifying the read.table function arguments directly. (2) keeping the read.table line I have below the same and modifying the dataframe after the fact. 
# How can you check to confirm that what you did worked? 
data = pd.read_table('streamflow_demo.txt', sep='\t',skiprows=30, names=['agency_cd', 'site_no',
                            'datetime', 'flow', 'code'])



# Exercise 2: 

#2.1: Read the 'daymet.csv' file in as a data frame using the 'date' column as the index and making sure to treat that column as a datetime object. 

#2.2: Explore this dataset and report what variables it contains, what date ranges are covered and the frequency of the data. 


#2.3  Make a scatter plot of day length (dayl) vs maximum temperature.


#2.4 Make with a lines for the monthly average of `tmax (deg c)` for all months after jan 2015.  Add shading to the plot extending to the monthly minimum and maximum of `tmax (deg c)` for the same period.

