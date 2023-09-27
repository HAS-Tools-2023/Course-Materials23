## Week6: Pandas DataFrames

### Series vs Dataframes: 
Basically the same but series are 1D (like a 1D numpy array but with an index that you can customize)  and dataframes have more than one colum

### What’s cool about dataframes: 
-	Tabular format of rows and columns
-	We can have columns with different kinds of data
-	Columns have names and we can access data this way 
-	They have row indices too
-	Good for maintaining relationships across data and 
-	Two ways to index and slice data; (1) using the index numbers like we did before, (2) using names
-	Can handle no data as blanks, NAs or what ever other signifier you want. 

### Some Key Methods: 
-	Head – see the first n rows
-   Tail – see the last n rows
-	Info – Get the details like size and names
-	Describe – provides summary statistics on all numeric columns
-	Median, mean, sum  – 
-	Sort_values – can sort your dataframe according to a specific column
-	Groupby – lets you group by one of the columns and then you can do operations from there. 

### Attributes: 
-	Columns: column names
-	Shape: just the shape
-	Index: returns the index
-	Dtypes: data types 

### How to index and slice pandas dataframes: 
-	Location based: 
    - Using iloc (think index location – locating things by the index #)
    - Same rules as for numpy indexing start:stop:step
    - Mydataframe.iloc[Rowselection, columnselection]
-	Label-based: 
    - To grab out specific rows: use loc and the names of the labels rather than index number
-	Grabbing out individual columns
    - To select a column just do: dataframe[“columnname”] – returns a 1D pandas series
    - To select a column as a dataframe or to select more than 1 column: dataframe[[‘columnname1”, “columnanme2”]]
-	Grabbing out ranges of rows:
    - Mydatafarme[rowstart:rowstop]  
Filtering values: 
-	Finding values that meat certain criteria
    -	Mydtaframe[dataframe[“column”] == value] 

