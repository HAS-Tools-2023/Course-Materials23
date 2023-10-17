# Week 8: Python skills week 6
This week is the grand finale of our first python section. 
____
## Table of Contents:
1. [ To Do List](#todo)
1. [ Resources](#resources)
2. [Assignment](#assignment)

___
<a name="todo"></a>
## To Do List
1. Create your forecasting code following the instructions below. **Do not** submit your forecast to the competition this week.  

2. Fill out the midcourse evaluation before class **next Monday**. You can access it [here](https://forms.gle/Jf1emk4wHzwwc7Af6)

___
<a name="Training Resources"></a>
## Resources
- Chapter 1 of Intermediate to Earth Data Science: Time Series Data in Python
  - [Lesson 1](https://www.earthdatascience.org/courses/use-data-open-source-python/use-time-series-data-in-python/introduction-to-time-series-in-pandas-python/): Intro to Timeseries
  - [Lesson 2](https://www.earthdatascience.org/courses/use-data-open-source-python/use-time-series-data-in-python/date-time-types-in-pandas-python/): Dates in Python
  - [Lesson 3](https://www.earthdatascience.org/courses/use-data-open-source-python/use-time-series-data-in-python/date-time-types-in-pandas-python/subset-time-series-data-python/): Subset Time Series Data
  - [Lesson  4](https://www.earthdatascience.org/courses/use-data-open-source-python/use-time-series-data-in-python/date-time-types-in-pandas-python/resample-time-series-data-pandas-python/): Resample Time series Data
  - [Lesson 5](https://www.earthdatascience.org/courses/use-data-open-source-python/use-time-series-data-in-python/date-time-types-in-pandas-python/customize-dates-matplotlib-plots-python/): Customize Dates on Plots

- Optional: do the [Time series challenge](https://www.earthdatascience.org/courses/use-data-open-source-python/use-time-series-data-in-python/date-time-types-in-pandas-python/time-series-exercise/) from this chapter.
- Official datetime documentation in the Python library [docs](https://docs.python.org/3/library/datetime.html)
- Chapter 3 of Python Data Science Handbook [Working with timeseries](https://jakevdp.github.io/PythonDataScienceHandbook/03.11-working-with-time-series.html)

___
<a name="assignment"></a>
## Assignment 8: Forecast script
This week you will be creating a script to generate your forecast. You will not be submitting your forecast this week because a partner in class will run your script and use it to generate your forecast for the forecast competition. 

#### Scripting Assignment
- You will create a python script using all of the things we have done up until now that will generate: 
  1. A printed statement that says `1 week forecast = xxx, 2 week forecast = xxx` Where `xxx` are your forecast numbers that you would like entered into the forecast competition. 
  2. Two graphs (or one multi-panel graph) that somehow illustrates your forecasted values relative to historical streamflow values (up to you what you define as 'historical' could be just the last year or just octobers or everything whatever is most informative to you). This could be points added to a timeseries or lines on a histogram. However you want to make it as long as your week 1 and week 2 forecasts are shown in relation to the past streamflow. 
   
- You can choose to calculate your forecast however you would like and you can use numpy arrays or dataframes to do it the only requirement is that it must be a calculated number (e.g. the mean of all October flow) as opposed to a hard coded number (e.g. forecast=7). 

- At some point in your script (plotting or forecast generation) you should use the timeseries functionality we learned this week.
  
- Although you aren't submitting your forecast to the competition this week you should download the streamflow and have a streamflow file located with your script so that anyone can run your script and get the outputs without needing to download or move data. 

#### Written Assignment
Your submission folder should include a markdown file that contains the following:
1. Your forecast numbers and a brief summary of how you generated them.
2. The two graphs you created along with an explanation on what each shows and how it supports your forecast decision. 
3. A reflection on things that are going well and issues that you are having. 


#### Submission Instructions
- Submit both your python script and markdown file to your submissions folder.
- Double check before you submit that the script can run directly from this folder and that you have the path to your data and functions setup correctly so your partner will be able to generate your forecast. 

