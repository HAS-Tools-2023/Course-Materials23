# Week 3: Python skills week 1 - Lists<!-- omit in toc -->
____

- [To Do List](#to-do-list)
- [Resources](#resources)
- [Training Activities](#training-activities)
- [Assignment 3: Lists and conditionals](#assignment-3-lists-and-conditionals)
    - [Rules for this week:](#rules-for-this-week)
    - [Submission instructions:](#submission-instructions)
    - [Assignment questions](#assignment-questions)
- [GitHub Cheat Sheet assignment:](#github-cheat-sheet-assignment)

___
## To Do List
1. Submit your [third streamflow forecast](#assignment-3-lists-and-conditionals) and assignment by **noon on Monday** following the instructions in the.
2. Complete the [required training Activities](#required-training-activities) by **next Tuesday**, get through as much as you can before class **Thursday**
3.  Submit your [GitHub CheatSheet](#github-cheat-sheet-assignment) by class **next Thursday**.

___
## Resources
Check out the following guides in the **cheatsheets** folder to help remind you of the content we cover this week:
  - python_basics.pdf
  - python_conditionals.pdf

___
## Training Activities
- Work through the following sections of Intro to Earth Data Science covering python fundamentals and Python Environments. There are quite a few this week so I recommend you start early. I recommend starting a separate .py file for working through the lessons and typing the commands as you go.
- **NOTE:** For some of the activities in chapter 17 you will need to install the package **earthpy** you should do this from terminal (either your stand alone terminal application or the terminal in VS code). First make sure that you have your *hastools* environment activated before you do the install by typing `conda activate hastools` installing pip by typing `conda install pip`, then you can install the package by typing `pip install earthpy`.
  - **Chapter 10: Getting started with Python variables and Lists**
    - Lesson 3: [Lists](https://www.earthdatascience.org/courses/intro-to-earth-data-science/python-code-fundamentals/get-started-using-python/lists/)
    - Lesson 4: [Operators](https://www.earthdatascience.org/courses/intro-to-earth-data-science/python-code-fundamentals/get-started-using-python/python-operators/)
    - (Optional) Lesson 5: [Exercises](https://www.earthdatascience.org/courses/intro-to-earth-data-science/python-code-fundamentals/get-started-using-python/python-fundamentals-exercises/)
  - **Chapter 17: Conditional Statements**
    - Lesson 1: [Intro to conditional statements](https://www.earthdatascience.org/courses/intro-to-earth-data-science/write-efficient-python-code/conditional-statements/)
    - Lesson 2: [Alternative and multiple conditions](https://www.earthdatascience.org/courses/intro-to-earth-data-science/write-efficient-python-code/conditional-statements/alternative-multiple-conditions/)
  - **Chapter 18: Loops**
    - Lesson 1: [intro to loops](https://www.earthdatascience.org/courses/intro-to-earth-data-science/write-efficient-python-code/loops/) (NOTE: for this one you can focus mainly on the for loop section. Don't worry about the while loop section.
    - Lesson 4: [list comprehensions](https://www.earthdatascience.org/courses/intro-to-earth-data-science/write-efficient-python-code/loops/list-comprehensions)

___
## Assignment 3: Lists and conditionals
This week you will be generating your forecast by using conditional statements in python to look at the historical streamflow and make forecast. You should write a script to subset the data however is most useful to you using conditionals and calculate the properties of this subset that will help you make your decision. You should use the HW3 starter code to see some examples of how to get started and for the setup of the variables you will need.
- **Remember** you should copy the starter code into your own repo and not work with it directly on the course materials repo).

#### Rules for this week:
- You can calculate min, max, mean and standard deviation but nothing more complicated than that at this point
- The only dataset you can use is the historical observed streamflow (Station 09506000 Verde River Near Camp Verde, refer to previous weeks for download instructions if needed. )
- You can use the streamflow data up to the Saturday before the forecast is due for making your decisions.

#### Submission instructions:
This week you should submit the following (for more details on submitting through GitHub refer to previous weeks instructions):
1. Your streamflow forecast values in the forecast repo in the csv with your name
2. Your assignment summary (see instructions below). This should be named with the same convention  as always 'lastname_HWx.md' and saved in the submission folder of your homework repo.  It should include (1) an appropriate header, (2)answers to all of the questions listed below and (3) a summary of how you made your forecast decision.
3. The python script you wrote to do your homework.  Just copy this script into the submission folder with the name 'lastname_HWx.py'

#### Assignment questions
**In addition to providing a summary of the forecast values you picked and why** include the following analysis in your homework submission.
1. Describe the variables `flow`, `year`, `month`, and `day`. What type of objects are they? What data types are they composed of? How long are they?
2. How many times was the daily flow greater than your prediction in the month of September (express your answer in terms of the total number of times and as a percentage)?
3. How would your answer to the previous question change if you considered only daily flows in or before 2000? Same question for the flows in or after the year 2010? (again report total number of times and percentage)
4. How does the daily flow generally change from the first half of September to the second?

___
## GitHub Cheat Sheet assignment (Due Thursday September 14):
- Over the course of the semester you will be creating a series of Cheat Sheets' to summarize the different concepts we cover. You can refer to the Cheat Sheets in the `Content` Folder for examples.
- It is entirely up to you though what yours should look like and note that you already have the ones I provided you so it doesn't need to be a duplicate of that. The point is for you to have a concise guide in your own words that will be helpful to you and that you can refer back to.
- This might take the form of a word document, a powerpoint slide, or even a hand written or drawn diagram, a jupyter notebook or pythhon script (when we get to those) or something more creative that I'm not thinking of yet :)
- In general I'm looking for something the equivalent of 1-2 pages long.
- All Cheat Sheet assignments will be graded pass/fail. If I determine yours needs work you will be able to resubmit the following week with a revised version.
- This week your Cheat Sheet should cover at a minimum:
  1. What is GitHub and what is Git (and how are they different)
  2. What is a repo and why is it different from a folder
  3. The difference between local, remote, origin
  2. Ways to get your own version of a repo and how they are differnt (Clone, Fork)
  3. How to add changes to your repo: Staging, committing and pushing  
  3. How to get the latest remote chagnes locally: Pulling vs fretching 
  3. Branchess -- what they are and why we use them
  4. What is a pull request and why would we use it
