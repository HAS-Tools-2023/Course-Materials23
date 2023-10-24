# Week 9: Python skills week 7
This week we are going to be working on making our code cleaner and easier to interpret.
____
## Table of Contents:
1. [ To Do List](#todo)
1. [ Setup Instructions](#setup)
1. [ Resources](#resources)
1. [ Training Activities](#training)
1. [ Forecast Assignment](#assignment)
1. [ Cheat Sheet Assignment](#cheatsheet)
___
<a name="todo"></a>
## To Do List
1. Setup linting in VSCode following the [setup](#setup) instructions. If possible test this out **before class on Thursday** so you can get help if needed.  

2. Revise your code following the comments you got from your partner and what we learned in class this week. Submit your final draft as well as a write up by **noon on Monday**  
   
3. Create your numpy and Pandas Cheat Sheet to be submitted by **noon on Monday**

4. Submit your forecast to the competition by **noon on Monday**.
___
<a name="setup"></a>

## Setup Instructions

Linters are tools that check the format of your code. In this case we will use the Flake8 tool to check our codes for PEP8 compliance. This is just one choice. There are lots of different tools you can use for this.

1. Access your command pallet in VS Code:
`Ctrl+Shift+P`(windows) `Cmd+Shift+P` (mac)
2. Type `Python: Select Linter` and choose `Flake8` from the dropdown menu
3. You will likely be prompted to install this at this point say yes and choose `conda` if it asks whether you want to install with pip or conda.
4. Next go back to your command pallet the same way you did at the start and type `Python: Enable Linting` and turn your linter on.
5. Now if you save changes to your file the linter should run automatically. If it's working, you will see red underlines where there are PEP8 issues in the code. Also you will see numbers appear in the bottom bar of your window noting how many issues you have (in this case 26 errors and 11 warnings)
![](assets/Week7_Python_Skills5-7d29dcca.png)
6. You can click on the warnings in the bottom bar and this will bring up a detailed list of problems you can check out like this:
![](assets/Week7_Python_Skills5-8cfe656d.png)
You can click on these items to be taken to the place in the code where they appear. If you fix issues and re-save your file you should see the errors you just fixed disappear from your list.
- **Note**: You can also run your linter any time by typing `Python: Run Linting` from the command pallet.
- For more info on  linting in VSCode check out this [link](https://code.visualstudio.com/docs/python/linting).

___
<a name="training"></a>
## References
- [Pep 8 Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
- [Tutorial on Python Functions](https://365datascience.com/python-functions/)

- Chapter 16 of Intro to Earth Data Science
  - [Lesson 1](https://www.earthdatascience.org/courses/intro-to-earth-data-science/write-efficient-python-code/intro-to-clean-code/): Introduction to Writing Clean Code and Literate Expressive Programming
  - [Lesson 2](https://www.earthdatascience.org/courses/intro-to-earth-data-science/write-efficient-python-code/intro-to-clean-code/python-pep-8-style-guide/): Introduction to PEP 8 Style Guide
  - [Lesson 3](https://www.earthdatascience.org/courses/intro-to-earth-data-science/write-efficient-python-code/intro-to-clean-code/expressive-variable-names-make-code-easier-to-read/): Writing expressive code
  - [Lesson  4](https://www.earthdatascience.org/courses/intro-to-earth-data-science/write-efficient-python-code/intro-to-clean-code/dry-modular-code/): Writing modular code

- Chapter 19 of Intro to Earth Data Science
    - [Lesson 1](https://www.earthdatascience.org/courses/intro-to-earth-data-science/write-efficient-python-code/functions-modular-code/): Introduction to functions
    - [Lesson  2](https://www.earthdatascience.org/courses/intro-to-earth-data-science/write-efficient-python-code/functions-modular-code/write-functions-in-python/): Writing functions in python.
    - [Lesson 3](https://www.earthdatascience.org/courses/intro-to-earth-data-science/write-efficient-python-code/functions-modular-code/write-functions-with-multiple-and-optional-parameters-in-python/): Writing multi-parameter functions
___
<a name="assignment"></a>
## Assignment 9: Making our scripts nice!
This week we will be working from the script you submitted for assignment 8 and cleaning it up to be submitted as your first graded script.

#### Forecast Rules for this week:
You will follow the same rules as last week and will just be revising your script. 

#### Coding Assignment:
This week you will be revising the code you submitted for the previous assignment to make it easier to read and so that someone else will be able to run your forecast.  You should refer to the evaluation rubric in the starter code folder for complete details on how your script will be evaluated in peer review.

- Revise your script based on the feedback you got in class on Tuesday and what we learned in class this week. 
- Your script must meet all the requirements form last week (i.e. a printed forecast output and two graphs). 
- In addition you should update your script so that it **uses at least one function** that is written by you. The function must have doc strings included. 
- You should also apply a linter to your script to be sure you are following pep8 standards
- Review your naming conventions and commenting throughout your code to make sure its easy to follow. 
- As with last week make sure that you have the required input files uploaded with your script so that I can run it. 
- Refer to the rubric in the grading folder to see how your script will be evaluated. 


#### Written Assignment: 
Provide a markdown file with a short reflection on:  
1. How you generated your forecast
2. How you made your script better this week
3. What you chose to put in a function and why
4. Remaining questions you have or thing you think could be better about your script but you don't know how. 

___
<a name="cheatsheet"></a>
Create a `cheat sheet`` on Pandas and Numpy covering the following: 
#### Numpy: 
  - The general purpose of the numpy library
  - What numpy array's are and what kinds of things they can (and can't contain)
  - Various approaches for how to slice a numpy array (e.g. grabbing out a row, column, range of values)
  - How to create a numpy array from scratch (please show at least 2 options)
  - List 5-6 helpful numpy functions and what they do

#### Pandas
  - The general purpose of the Pandas library
  - What makes a pandas data frame is different from a numpy array
  - An explanation of what the 'index' of a dataframe and why its different from other columns
  - How to setup a pandas dataframe by reading a file
  - How to se the index of a pandas dataframe
  - How to slice a pandas dataframe: 
    - using loc and iloc to get rows 
    - grabbing out columns by name or number
  - 5-6 helpful pandas functions or methods that you can use to inspect your dataframe (list each and explain what it does)