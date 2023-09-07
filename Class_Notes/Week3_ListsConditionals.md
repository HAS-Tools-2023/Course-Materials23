# Big Ideas from Week 3: Lists operators, conditional statements and loops

## What is python: 
-	Interpreted language: means we don’t have to compile our scripts. Other examples – R, Matlab.  Compiled languages: C, Fortran
-	Object oriented: we make objects and those have methods and characteristics associated with them. We will learn about data types – lists dataframes and the methods that are unique to them. 
-	 High level – we are working with human readable code that can function across compute enviroments. 
-	Free and open source – community can contribute packages. 

## Ways to run python: 
-	Command line directly
-	write a script and run from command line
-	IDE
-	Jupyter notebooks
-	Other integrations – like QGIS, Atom etc

## Variables: 
-	Can be anything, just set it with the ‘=’ and then you can use it. 
-	No spaces in names, try to keep them short but specific
-	Use ‘_’ to create multi word variable names. 
-	Walk through setting and using a variable and seeing it in vs code. 

## Basic Data Types: 
Use the function `type` to see what kind of data something is:
- `bool`: Boolean values, basically just True or False - same concept as binary, named after George Boole
- `int`: Integers, or whole numbers
- `float`: Floating point numbers, or real numbers (those which decimals)
- `str`: Strings, or text data

There are many more complicated data types such as lists and dictionaries but we'll get into these later

## Operators
Operators: Symbols that carry out a specific operation
-	Arithmetic, (*,/, +, -, **)
-	assignment (+=, *=)
-	comparison (<, >, =, !=), 
-	Identity (is, is not) 
-	Membership (in)
-	Logical (AND, OR)

## Lists: 
Lists are a type of python object. It has its defined structure and methods associated with it. 
- Contain mixture of data types (int,  floats, str)
-	Can also make lists of lists
-	Make them using []
-	Entries are called items
-	Indexing starts counting at 0!
- Slicing – you can get a range start:stop
- **NOTE: stop is not included in the slice the slice is start:(stop-1)
- If you skip the start or stop values this gives you everything from the beginning to the start or from the stop to the end 
– values means to use position relative to the end not the start

Working with lists: 
- Grabbing something out: list[i]
- Adding something to a specific location in a list: list.insert(0, newitem)
- Adding something to the end: list.append(newitem)
- Using the + operator: mylist = [newitem] + mylist
- List.xxx are methods associated with the object type list

## Conditionals: Tests whether a condition exists before executing code
-	If, else, elseif (do an in class walkthrough of this one) 
-	Note: Indentation matters
-	If statements can use logical operators to contain multiple conditions 
-	Draw out the ven diagram of multiple conditions (and = both, or = at least one condition met, not = not met (combine and or or with not to get just one condition)

## For Loops:
For Loops: 
-	For x in list:
-	Range(x) – automatically creates a range of integers from 0 to n for iterating  (note it only iterates to n-1)
-	List comprehensions: when we put a for loop inside a list, basicall a much shorter way of writing loops and conditionals for lists [operation for value in list]

