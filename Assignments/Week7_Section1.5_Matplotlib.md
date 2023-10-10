# Week 7: Python skills week 5
This week we are going to continue using Pandas DataFrames and we will be focusing on plotting with matplotlib.
____
## Table of Contents:
1. [ To Do List](#todo)
1. [ Resources and Training](#resources)
2. [ Forecast Assignment](#assignment)

___
<a name="todo"></a>
## To Do List
Submit your streamflow forecast and assignment by **5pm on Monday** following the instructions in the [ Forecast Assignment](#assignment).

___
<a name="resources"></a>
## References
- There are two images in the Cheet_sheets folder that covers the major plotting commands: `matlotlib_commands.png` and `matlotlib_commands2.png`

- You should also check out the [matplotlib website](https://matplotlib.org/) I especially recommend the [plot gallery](https://matplotlib.org/gallery/index.html) as a good place to get started.

- [Python Data Science Handbook Chapter 4](https://jakevdp.github.io/PythonDataScienceHandbook/) (sections of this chapter are also assigned in the required training).
    - [Simple Line Plots](https://jakevdp.github.io/PythonDataScienceHandbook/04.01-simple-line-plots.html)
    - [Simple Scatter Plots](https://jakevdp.github.io/PythonDataScienceHandbook/04.02-simple-scatter-plots.html)
    - [Visualizing  Errors](https://jakevdp.github.io/PythonDataScienceHandbook/04.03-errorbars.html)
    - [Histograms, Binning and Density](https://jakevdp.github.io/PythonDataScienceHandbook/04.05-histograms-and-binnings.html)
    - [Customizing  Plot Legends](https://jakevdp.github.io/PythonDataScienceHandbook/04.06-customizing-legends.html)
    - [Customizing Colorbars](https://jakevdp.github.io/PythonDataScienceHandbook/04.07-customizing-colorbars.html)
    - [Multiple Subplots](https://jakevdp.github.io/PythonDataScienceHandbook/04.08-multiple-subplots.html)
    - [Customizing  Matplotlib: Configurations and Stylesheets](https://jakevdp.github.io/PythonDataScienceHandbook/04.10-customizing-ticks.htmll)
___
<a name="assignment"></a>
## Assignment 7: Plotting
This week we don't have a starter code. Use your starter code from last week to read the streamflow data into your python script as a pandas dataframe and work from there. 

#### Forecast Rules for this week:
- You must use the pandas dataframe *data* created at the top of the starter code as the basis for your analysis.

- You can do any mathematical operation you would like on the dataset as long as you only use the numpy or pandas package to do so.  

- The only dataset you can use quantitatively is the historical observed streamflow (Station 09506000 Verde River Near Camp Verde, refer to previous weeks for download instructions if needed. )

- You can use the streamflow data up to the Saturday before the forecast is due for making your decisions.

#### What to submit:
1. Your streamflow forecast values in the forecast repo in the csv with your name

2. Your assignment summary. This should be named with the same convention  as always `lastname_HWx.md` and saved in the submission folder of your homework repo.  

3. The python script you wrote to do your homework.  Just copy this script into the submission folder with the name `lastname_HWx.py`. **NOTE:** *Even if you have a free pass on the written assignment for this week you should still create 5 graphs and include them in your markdown you just can skip the reflections*


#### Assignment
1. Summarize your forecast and for the week and how you came up with it
2. Create 5 plots that summarize the streamflow data and help you make your forecast. You can plot anything that you want as long as you meet the following requirements: 
   - You must have 3 different types of plots (e.g. line, scatter, histogram, bar..)
   - You must have one multi panel plot (note that counts as one plot regardless of the number of subplots you have)
   - All plots must have a legend, title, and appropriate axis labels
   - One of your plots should include at least two items (e.g. two different lines, a line and some dots, a filled area and a line)
3. For each of your plots copy the image into your markdown and include a sentence describing the plot and explaining why you chose to plot what you did. 
4. Write a short reflection on your progress so far: 
   - Favorite things you have learned or are feeling more confident about. 
   - Things you are still confused/struggling with

