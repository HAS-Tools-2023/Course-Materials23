# Week 5: Python skills week 3
This week we will continue working with numpy and practicing with if statements and for loops. 
____
## Table of Contents:
1. [ To Do List](#todo)
2. [ Training Activities](#training)
3. [ Forecast Assignment](#assignment)

___
<a name="todo"></a>
## To Do List
1. Submit your fifth streamflow forecast by **noon on Monday** 
2. Submit your homework by **noon on Wednesday** Note that there is an extension on this homework as we don't have class next Tuesday. 

___
<a name="training"></a>
No new training materials this week just review the materials that have been provided so far and catch up. 
___
<a name="assignment"></a>
## Assignment 5: Numpy and loops
We are still in the exploratory data phase. You can start from the same starer code as we used last week.  

#### Forecast Rules for this week:
- You must use the numpy array *flow_data* created at the top of the starter code as the basis for your analysis (i.e. don't use lists again)

- You can do any mathematical operation you would like on the dataset as long as you only use the numpy package to do so.  

- The only dataset you can use is the historical observed streamflow (Station 09506000 Verde River Near Camp Verde, refer to previous weeks for download instructions if needed. )

- You can use the streamflow data up to the Saturday before the forecast is due for making your decisions.

#### Submission instructions:
This week you should submit the following (for more details on submitting through GitHub refer to previous weeks instructions):

1. Your streamflow forecast values in the forecast repo in the csv with your name due by Monday 

2. Your assignment summary (see instructions below). This should be named with the same convention  as always 'lastname_HWx.md' and saved in the submission folder of your homework repo.  It should include
  1. An appropriate header,
  2. A summary of your forecast and how you made it
  3. Answers to all of the questions listed below
  4. A refection on how things are going for you this week. Things you are getting, things you aren't. Things you hope we'll cover. 

3. The python script you wrote to do your homework.  Just copy this script into the submission folder with the name 'lastname_HWx.py'. Note even if you have a free pass on the write up this week you should still complete all the exercises and submit your python script. 


#### Assignment 
1. Copy the top of your starter code from week 4 to read in your streamflow file and create a numpy array called `flow_data` that has four columns (year, month, day, flow) and a row for every day. 
   
2. Create a new numpy array that has the same four columns as flow_data  but includes only the data for the five year period from **1/1/2015-12/31/2019**. Call your new array `flow_5yr`. For all subsequent questions we will just use `flow_5yr` for our analysis. Print out the dimensions of `flow_5yr` along with the average flow in this five year period (i.e. just one number averaged across the entire timeseries). Provide both these values in your markdown write up. 
   - **BONUS:** Show how you can do this with 1 line of code, 2 lines of code and using a for loop
- 
3. Convert the daily average flow from cubic feet per second to cubic feet. Do this two ways, (1) without using a for loop,  and (2) with using a for loop. Save this a a variable called `flow_daily`.  Report the first 5 daily flow values in your markdown as well as the total flow in cubic feet over the entire time period. 
   
4. Create a time series of monthly average flow from the daily flow values (i.e. I'm looking for a timeseries that is 60 months long). You should store this in a numpy array called `flow_monthly` that has 60 rows and three columns. The first column should be year, the second month and the third should be flow. Print out the first five rows of this array and report them in your markdown file. 
   - **HINT**: To fill in the year and month columns I recommend you use the functions `np.arange`, `np.tile` and `np.repeat`. 
   - 

5. Don't forget to provide a reflection in your markdown file for the week on what was hard and what was easy and if there was anything you couldn't do. 
