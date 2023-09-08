# Big Ideas from Week 4: Numpy

## Some general definitions: 
-	Methods – Functions associated with a class (or object type)--- called by object.method()
-	Attributes – Variables associated with a class (or object type) – called by object.attribute
-	Functions – tools to execute a specific action called by – package.function(arguments…) 

## Numpy Arrays: 
-	Object that stores data as a grid (matrix, can have many dimensions)
-	Like lists they are composed of ordered values (elements) and can be indexed similarly
-	1D arrays may look a lot like lists but they are not the same and working with them is quite different. 
-	Unlike lists – all elements must be the same data type. Because of this we can do math on them directly (can’t do that with lists)
-	Unlike lists – Need the python package numpy to work with them
-	

## How to make them? 
-	Enter data directly for a 1D: Np.array([1,2,3])
-	Enter data directly for a 2D: np.array([[1,2,3], [4,5,6]])
-	Make a set of random numbers:  np.random.randint(10, size = (3,4)) #2d array 3 rows for columns, integers 0-10
-	Make a set of zeros or ones: np.zeros((dim1,dim2)) or np.ones((dim1,dim2,…))
-	Make a set of sequential values: np.arange(start, stop) (note: this is a 1-d array but you can use .reashape to change dimensions)
-	Read in a table of data.  More on this later 

## Useful attributes of numpy arrays:  
-	shape – size in every dimension 
-	ndim – number of dimensions 
-	size – total number of elements
-	dtype – type of elements in the array

## Some useful methods:
-	.reshape : can change the dimensions of an array
-	.concatenate: adding datat
-	Math: min, max, mean, std
-	Finding locations of min and max: argmin, argmax
-	Most of these have nan safe versions – np.nansum, np.nanmax etc. 
-	Good table here: https://jakevdp.github.io/PythonDataScienceHandbook/02.04-computation-on-arrays-aggregates.html 

## Universal functions and broadcasting with numpy arrays: 
-	Means that you can use mathematical operators and they will automatically be applied to each element without you writing a for loop x=np.arange(4), x*4 
-	Can also do this doing math between two arrays if they have the same dimensions or share a dimension see the book explanations on broadcasting (https://jakevdp.github.io/PythonDataScienceHandbook/02.05-computation-on-arrays-broadcasting.html)

## Indexing and slicing: 
-	Works like lists you specify a range of values start:stop:step
-	But for multiple dimensions you put a ‘,’ between dimensions
-	Rows are first columns are second! [row,column] or [rowstart:rowend, colstart:colend]
-	Counting rules are the same as for lists
-	: in any dimension gives you the entire dimension e.g. [:,2] gives you the third column
-	Important note: when you slice an array it does not make a copy so if you make changes on that slice it will change the original array. To get a slice that is separate from the original array you need to do .copy() example myslice = array[:2, :2].copy()
-	Can also use logical statements to subset – x[x<5] 
-	See(https://jakevdp.github.io/PythonDataScienceHandbook/02.06-boolean-arrays-and-masks.html)

## numpy functions:  called by saying np.functionname(array, arguments…)
-	Some statistics: np.mean, min, max, median… many more
o	most np functions have an axis argument if you want to summarize on just one axis (axis=0 summary of each column across all rows, axis= 1 summary of each row across all columns)
o	NOTE: min and max also exist as generic built in functions but its faster to use the numpy versions
o	NOTE2 these are also available as methods
-	Combining arrays: concatenate, vstack, hstack:
-	Dividing arrays: split, hsplit, vsplit
