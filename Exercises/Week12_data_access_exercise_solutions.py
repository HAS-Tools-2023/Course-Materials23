# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os
import dataretrieval.nwis as nwis
import matplotlib.pyplot as plt
import json 
import urllib.request as req
import urllib

# %%
#____________________________
# Exercise 1: 
#____________________________
# 1. Write a function that takes the following arguments as inputs: 
# - USGS Station ID
# - Start Date of desired observations
# - End Date of desired observations
# And returns a dataframe with the USGS streamflow for the desired location and date range. 
def get_streamflow(siteID, start_date, end_date):
    url2 = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=" + siteID + \
      "&referred_module=sw&period=&begin_date=" + start_date + "&end_date=" + end_date
    data = pd.read_table(url2, skiprows=30, names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'], parse_dates=['datetime'], index_col=['datetime']) 
    return data

#%%
# 2. Select two other gauges on the Verde River (https://maps.waterdata.usgs.gov/mapper/index.html) and use your function to download the data for all three gauges for the past year (The two you select plus 09506000). 
start = '2023-01-01'
end = '2023-11-13'

camp_verde = get_streamflow(siteID='09504950', start_date=start, end_date=end)
clarkdale = get_streamflow(siteID='09504950', start_date=start, end_date=end)
paulden = get_streamflow(siteID='09503700', start_date=start, end_date=end)

#%%
# 2BONUS: make a list of stream gauge sites and use a for loop to get the streamflow data for them

site_list=['09504950','09504950', '09503700']
i=0
for s in site_list:
    print(s)
    temp_data=get_streamflow(s, start_date=start, end_date=end)
    if i ==0:
        flow = temp_data['flow']
    flow=pd.concat(flow, temp_data['site_no'])

#%%
#3. Make a timeseries plot showing the data from all 3 gauges on a single plot. 
ax = plt.axes()
ax.plot(camp_verde['datetime'], camp_verde['flow'], color= 'red', linestyle = 'dashed', label = 'Camp Verde')
ax.plot(clarkdale['datetime'], clarkdale['flow'], color= 'blue', linestyle = 'dashed', label = 'Clarkdale')
ax.plot(paulden['datetime'], paulden['flow'], color= 'green', linestyle = 'dashed', label = 'Paulden')
ax.set(title="Observed Flow", xlabel="Date",
       ylabel="log(Streamflow [cfs])",
       yscale='log')
ax.legend()


# %%
#____________________________
# Exercise 2:
#____________________________

#1. Download the dataset from the class notes and determine what (1) type of python object the station observations are and (2) what all variables are included in the observations. 

# First read in the data
mytoken = ''
base_url = "http://api.mesowest.net/v2/stations/timeseries"
args = {
    'start': '202301010000',
    'end': '202311150000',
    'obtimezone': 'UTC',
    'vars': 'air_temp',
    'stids': 'QVDA3',
    'units': 'temp|F,precip|mm',
    'token': mytoken} 

apiString = urllib.parse.urlencode(args)
fullUrl = base_url + '?' + apiString
response = req.urlopen(fullUrl)
responseDict = json.loads(response.read())

dateTime = responseDict['STATION'][0]['OBSERVATIONS']['date_time']
airT = responseDict['STATION'][0]['OBSERVATIONS']['air_temp_set_1']

# Now we can combine this into a pandas dataframe
data = pd.DataFrame({'Temperature': airT}, index=pd.to_datetime(dateTime))
data_daily = data.resample('D').mean()
plt.plot(data_daily)

# %%
#2. Modify the API call to return accumulated precipitation instead (variable name = 'precip_accum', set the units to 'metric') and make a plot of the daily max accumulated precipitation
mytoken = ''

args = {
    'start': '202301010000',
    'end': '202311150000',
    'obtimezone': 'UTC',
    'vars': 'precip_accum',
    'stids': 'QVDA3',
    'units': 'metric',
    'token': mytoken} 


apiString = urllib.parse.urlencode(args)
fullUrl = base_url + '?' + apiString
response = req.urlopen(fullUrl)
responseDict = json.loads(response.read())

dateTime = responseDict['STATION'][0]['OBSERVATIONS']['date_time']
precip = responseDict['STATION'][0]['OBSERVATIONS']['precip_accum_set_1']

units = responseDict['UNITS']

data = pd.DataFrame({'Precip': precip}, index=pd.to_datetime(dateTime))
data_daily = data.resample('D').max()

plt.plot(data_daily)