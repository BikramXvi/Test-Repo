**UNIT** 1: **INTRODUCTION** TO **DATA** **SCIENCE** 1.1 What is Data Science? Definition Data Science is an interdisciplinary field that uses statistics, programming, and domain knowledge to analyze structured and unstructured data and generate meaningful insights. It combines techniques from mathematics, computer science, and Artificial Intelligence to solve real-world problems through data-driven approaches.

### Detailed Explanation

Simple Definition: Data Science is the art of learning from data. It is a branch of mathematics that deals with collecting, analyzing, interpreting, presenting, and organizing data.

Arthur Samuel's Definition (**1959**): "A system that learns from data and improves without being explicitly programmed."

Key Aspects:

Collecting: Gathering raw data from various sources

Analyzing: Applying statistical and computational methods

Interpreting: Deriving meaning from analysis results

Presenting: Visualizing findings for stakeholders

Organizing: Structuring data for efficient access

1.2 Data Science vs Data Analytics vs Business Analysis
Aspect	Data Science	Data Analytics	Business Analysis
Focus	Predictive modeling, ML	Descriptive insights, trends	Business needs, requirements
Output	Models, predictions	Reports, dashboards	Solution requirements
Tools	Python, R, TensorFlow	**SQL**, Excel, Tableau	**JIRA**, Visio, **BPMN**
Questions	What will happen?	What happened?	What does business need?
Timeframe	Future prediction	Past & present	Current & future needs
1.3 Real-World Applications of Data Science
## Retail (Predicting What You'll Buy)
Problem: What products will sell tomorrow, next week, or during festivals?

Solution using Data Science:

Historical sales data analysis

Weather data integration (rain, heat waves)

Festival and holiday pattern recognition

Local events tracking

Examples:

Before heavy rain → raincoats, boots, instant noodles increase

Before cold wave → heaters, blankets, hot beverages stocked more

During heat waves → sunscreen, fans, ice cream sales spike

Before school reopening → notebooks, backpacks, pens increase

Before festivals → lights, decorations, gift items stocked more

Association Rule Mining:

Customers buying baby diapers → wipes & baby food stocked nearby

Customers buying barbecue grills → charcoal & sauces nearby

## E-Learning (Course Price Optimization)

Problem: How to maximize course sales while keeping prices attractive?

Solution:

User segmentation based on history, location, device cookies

New users see heavy discounts (e.g., Rs.9.99 instead of Rs.**199**)

High-demand courses maintain higher prices

Low-demand courses get automatic discounts

## Other Applications

Domain	Application
Healthcare	Disease outbreak prediction, medical diagnosis
Finance	Fraud detection, credit scoring
Manufacturing	Quality control, predictive maintenance
Transportation	Autonomous vehicles, traffic prediction
1.4 Gut Feeling vs Data-Driven Decision Making
The Problem with Intuition
Scenario	Intuition	Data-Driven Approach	Impact
Inventory Management	*We'll sell more winter jackets*	Sales trends + weather forecasts	Avoids overstock, reduces costs
Product Launch	*Young customers will buy*	Market research shows 35-50 age group	Correct targeting
Marketing Campaign	*Holiday season is best*	Data shows mid-year sales outperform	Better **ROI**
Example: Inventory Management
A retailer plans inventory based on intuition and orders 10,**000** winter jackets. However, data analysis of historical sales combined with weather forecasts shows a warmer winter, with demand likely only 6,**000** jackets.

Result: Orders reduced to 6,**000** jackets, avoiding 4,**000** unsold units → reduces storage costs, prevents heavy discounting, frees capital for faster-selling products.

1.5 Data-Driven Decision Making Definition The practice of making business decisions based on the analysis of data rather than purely on intuition.

Common Mistakes in Data Science Projects Rushing into data collection and analysis without planning

Spending less time to plan and scope the amount of work involved

Not performing data and business domain understanding

1.6 Data Mining Definition Data mining (or extraction of useful information and knowledge from data) is a process with well-defined stages for discovering patterns in large datasets.

### Key Techniques

Technique	Description	Example
Classification	Predict category/class	Spam detection (spam/not spam)
Regression	Predict continuous value	House price prediction
Clustering	Group similar items	Customer segmentation
Association Rules	Find item relationships	Market basket analysis
Anomaly Detection	Identify unusual patterns	Fraud detection
**UNIT** 2: **CRISP**-DM **METHODOLOGY**
2.1 Introduction to **CRISP**-DM
Definition
**CRISP**-DM (Cross-Industry Standard Process for Data Mining) is a widely used process framework that outlines the complete lifecycle of data-driven projects, from understanding business problems to implementing final solutions.

The 6 Phases
text
Business Understanding → Data Understanding → Data Preparation → Modeling → Evaluation → Deployment
    ↑                                           |
    └───────────────────────────────────────────┘
    (Iterative feedback loops)
2.2 Phase 1: Business Understanding
Most Important Activities:

Understand the current situation and past related data science projects

Frame/state the business problem as an analytics challenge

Map defined business problem to one or more common data science tasks

Assess available resources (technology, systems, tools, people, data)

Example - Retail Inventory Optimization:

Define problem: Overstock of winter jackets increases cost every year

Set business objectives: Reduce unsold jackets by 20%

Define success criteria: Accurate demand prediction before winter season

Identify constraints: Limited storage space, seasonal demand, fixed suppliers

Output: Instead of guessing *we'll sell more jackets,* the company decides to predict demand using data.

2.3 Phase 2: Data Understanding Most Important Activities:

Identify potential data sources (transactional databases, spreadsheets, **CSV**, text files, web logs)

Capture aggregate data sources for previewing

Review raw data to understand interdependencies, content, quality, limitations

Evaluate data structures and tools needed

Example - Retail Inventory:

Collect data: Past jacket sales (5 years), weather data, pricing

Explore patterns: Sales drop during warmer winters

Check quality: Missing sales records in some months

Identify key factors: Temperature has strong impact on jacket sales

Output: Data shows that warmer winters lead to lower jacket sales, contradicting intuition.

2.4 Phase 3: Data Preparation Key Activities:

- Preparing an Analytics Sandbox
Create a dedicated environment separate from production (Data Warehouse, Data Lake, or Big Data Platform) as a research *playground.*

- Performing **ETL**/**ELT**
Move data from source systems into the sandbox using Extract, Transform, and Load (**ETL**) or Extract, Load, and Transform (**ELT**) pipelines.

- Data Discovery and Gap Analysis
Audit available data to clarify what is accessible and what is missing.

- Data Conditioning
Process of cleaning data, normalizing datasets, and performing transformations.

- Survey and Visualize
Use visualization tools to gain a bird's-eye view of distributions and nuances (histograms, scatter plots, summary statistics).

2.5 Phase 4: Modeling
Types of Modeling Tasks
Task Type	Description	Example Question
Classification	Predict which of a small set of classes	*Which customers will respond to an offer?*
Regression	Estimate numerical value	*How much will a customer use the service?*
Clustering	Group by similarity	*Do customers form natural segments?*
Co-occurrence Grouping	Find associations between entities	*What items are commonly purchased together?*
2.6 Phase 5: Evaluation
Key Activities:

Select modeling techniques appropriate for problem type

Build models on prepared dataset (multiple for comparison)

Assess performance using appropriate metrics

Review to ensure model meets business objectives

2.7 Phase 6: Deployment Key Activities:

Plan Deployment: Decide how model/insights will be used (batch processing vs real-time scoring)

Plan Monitoring & Maintenance: Set up processes to ensure model remains accurate

Model Implementation: Integrate into business processes or IT systems

User Training: Train business users to understand and interpret model outputs

Feedback & Iteration: Collect feedback and monitor business impact

**UNIT** 3: **PYTHON** **DATA** **STRUCTURES** 3.1 Lists Definition An ordered collection of elements accessible by index, mutable (can be modified), and can contain heterogeneous (different types) or homogeneous elements.

### Creation Methods

python # Method 1 (without constructor) empty_list = [] int_list = [7, 8, 9] mixed_list = [1, *Hello*, 3.4] nested_list = [*Welcome*, [4, 5, 6]]

# Method 2 (with constructor)

empty_list = list() int_list = list([7, 8, 9]) ### Slicing Lists python A = [1, 2, 3, 4, 5] print(A[0:4])    # [1, 2, 3, 4] - positive indexing print(A[-2:-1])  # [4] - negative indexing (starts from end) Index Visualization:

text
Elements:   1    2    3    4    5
Positive:   0    1    2    3    4
Negative:  -5   -4   -3   -2   -1
### List Methods
Method	Description	Example
append(x)	Add item to end	nums.append(7)
extend(iterable)	Add multiple items	nums.extend([8, 9])
insert(i, x)	Insert at position	nums.insert(0, 1)
remove(x)	Remove first occurrence	nums.remove(3)
pop(i)	Remove and return at index	nums.pop(2)
index(x)	Return index of first occurrence	nums.index(4)
sort()	Sort in ascending order	nums.sort()
reverse()	Reverse the list	nums.reverse()
Examples
python
# Append and Extend
nums = [1, 3, 4, 5]
nums.append(7)        # [1, 3, 4, 5, 7]
nums.extend([8, 9])   # [1, 3, 4, 5, 7, 8, 9]

# Sort

nums = [5, 3, 8, 1] nums.sort()           # [1, 3, 5, 8] 3.2 Tuples Definition An ordered collection of elements that is immutable (cannot be changed after creation). Allows duplicate values.

Creation python my_tuple = (1, 2, 3, 4) single_element = (5,)  # Note: comma required Packing & Unpacking python t = (10, 20, 30) a, b, c = t   # Unpacking print(a, b, c)  # Output: 10 20 30 ### Use Cases Fixed configuration settings

Function returning multiple values

Dictionary keys (since immutable)

3.3 Sets Definition An unordered collection of unique elements. Mutable (can add/remove items).

Creation
python
my_set = {1, 2, 3, 4}
### Set Operations
Operation	Method	Operator	Description
Union	set1.union(set2)	set1 | set2	All elements from both sets
Intersection	set1.intersection(set2)	set1 & set2	Common elements
Difference	set1.difference(set2)	set1 - set2	Elements in set1 not in set2
Symmetric Diff	set1.symmetric_difference(set2)	set1 ^ set2	Elements in either, not both
### Set Methods
python
# Adding elements
my_set.add(5)

# Removing elements

my_set.remove(3)     # Raises error if not found my_set.discard(3)    # No error if not found ### Use Cases Removing duplicates from a dataset

Membership testing

Mathematical set operations

3.4 Dictionaries Definition A collection of key-value pairs. Mutable. Keys must be unique and immutable (strings, numbers, tuples). Values can be any type.

Creation python my_dict = {'a': 1, 'b': 2} Why Use Dictionaries? Suppose your program stores millions of student records and needs frequent searching. Dictionaries allow O(1) lookup time vs O(n) for lists.

### Dictionary Methods

Method	Description
keys()	Returns all keys
values()	Returns all values
items()	Returns key-value pairs
get(key)	Returns value or None
update(other_dict)	Merges dictionary
pop(key)	Removes and returns value
Examples
python
student = {'name': 'Alice', 'age': 25}
print(student['name'])        # 'Alice'
print(student.get('grade'))   # None
student['grade'] = 'A'        # Add new key-value
3.5 Comparison of Data Structures
Feature	List	Tuple	Set	Dictionary
Ordered	Yes	Yes	No	Yes (Python 3.7+)
Mutable	Yes	No	Yes	Yes
Duplicates	Allowed	Allowed	Not allowed	Keys: No, Values: Yes
Indexing	Integer	Integer	No	Keys
Use Case	Dynamic sequences	Fixed data	Unique items	Key-value lookups
### Best Practices
Use lists when data needs frequent modification

Use tuples for fixed data that should not change

Use sets when uniqueness is required

Use dictionaries for fast lookups and key-value mapping

**UNIT** 4: **NUMPY** (**NUMERICAL** **PYTHON**) 4.1 Introduction to NumPy Definition NumPy (Numerical Python) is a core library for numerical computing in Python that provides powerful multi-dimensional arrays and mathematical functions to efficiently work with large amounts of numerical data.

### Key Features

Much faster than Python lists for mathematical operations

Provides support for large multi-dimensional arrays and matrices

Brings computational power of C and Fortran to Python

Includes tools for linear algebra, statistics, and mathematical functions

Uses less memory due to efficient data storage

Foundation for Pandas, SciPy, TensorFlow, and scikit-learn

4.2 NumPy ndarray Definition An ndarray (N-dimensional array) is the main data structure in NumPy.

What *ndarray* Means:

n = any number

dimensional = dimensions (1D, 2D, 3D, etc.)

array = ordered collection of elements

NumPy Array vs Python List
Feature	Python List	NumPy Array
Data types	Can mix types	All elements same type (homogeneous)
Speed	Slower for numerical ops	Much faster
Memory	More memory usage	Less memory
Operations	Element-wise loops needed	Vectorized operations
4.3 Array Creation
### Basic Creation
python
import numpy as np

# From Python lists/tuples

arr_from_list = np.array([1, 2, 3, 4, 5])
arr_from_tuple = np.array((1, 2, 3, 4, 5))
### Array Creation Functions
Function	Description	Example
np.array([...])	Create from sequence	np.array([1,2,3])
np.zeros(n)	Array of zeros	np.zeros(5) → [0.,0.,0.,0.,0.]
np.ones(n)	Array of ones	np.ones(5) → [1.,1.,1.,1.,1.]
np.empty(n)	Uninitialized (garbage values)	np.empty(5)
np.full(n, val)	Fill with constant	np.full(5, -1) → [-1,-1,-1,-1,-1]
np.arange(start, stop, step)	Range of values	np.arange(0, 10, 2) → [0,2,4,6,8]
np.linspace(start, stop, num)	Evenly spaced	np.linspace(0, 1, 5) → [0,0.25,0.5,0.75,1]
Examples
python
# Array with initial placeholders
zeros_arr = np.zeros(5)      # [0. 0. 0. 0. 0.]
ones_arr = np.ones(3)        # [1. 1. 1.]
empty_arr = np.empty(4)      # random garbage values
full_arr = np.full(5, -1)    # [-1 -1 -1 -1 -1]

# Range functions

arange_arr = np.arange(0, 10, 2)     # [0 2 4 6 8] linspace_arr = np.linspace(0, 1, 5)  # [0.   0.25 0.5  0.75 1.  ] 4.4 Multidimensional Arrays python # 2D array (matrix) matrix_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Check shape

print(matrix_2d.shape)  # (2, 3) - 2 rows, 3 columns

# 3D array

array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]) print(array_3d.shape)   # (2, 2, 2) 4.5 Basic Operations Element-wise Operations python arr = np.array([1, 2, 3, 4])

# Arithmetic operations (element-wise)

arr + 2    # [3, 4, 5, 6] arr * 3    # [3, 6, 9, 12] arr ** 2   # [1, 4, 9, 16]

# Operations between arrays

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr1 + arr2   # [5, 7, 9]
arr1 * arr2   # [4, 10, 18]
### Comparison Operations
python
arr = np.array([1, 2, 3, 4, 5])
arr > 3    # [False, False, False, True, True]
arr == 3   # [False, False, True, False, False]
4.6 Aggregate Functions
Function	Description
np.sum(arr)	Sum of all elements
np.mean(arr)	Arithmetic mean
np.median(arr)	Median value
np.std(arr)	Standard deviation
np.var(arr)	Variance
np.min(arr)	Minimum value
np.max(arr)	Maximum value
np.argmin(arr)	Index of minimum
np.argmax(arr)	Index of maximum
Examples
python
arr = np.array([10, 20, 30, 40, 50])

print(np.sum(arr))     # **150** print(np.mean(arr))    # 30.0 print(np.std(arr))     # 14.**142**... print(np.min(arr))     # 10 print(np.argmax(arr))  # 4 (index of 50) Axis Parameter (for 2D arrays) python matrix = np.array([[1, 2, 3], [4, 5, 6]]) print(np.sum(matrix, axis=0))  # Sum down columns: [5, 7, 9] print(np.sum(matrix, axis=1))  # Sum across rows: [6, 15] 4.7 Indexing and Slicing python arr = np.array([10, 20, 30, 40, 50, 60])

# Basic slicing

arr[0]        # 10 (first element) arr[-1]       # 60 (last element) arr[1:4]      # [20, 30, 40] arr[::2]      # [10, 30, 50] (step of 2)

# 2D array indexing

matrix = np.array([[1, 2, 3], [4, 5, 6]]) matrix[0, 1]     # 2 (row 0, column 1) matrix[:, 1]     # [2, 5] (all rows, column 1) matrix[0, :]     # [1, 2, 3] (row 0, all columns) ### Fancy Indexing python arr = np.array([10, 20, 30, 40, 50]) indices = [0, 2, 4] print(arr[indices])  # [10, 30, 50] 4.8 Boolean Masking Definition Applying a condition to an array and selecting elements that satisfy that condition.

Syntax python arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) mask = arr > 5 print(mask)           # [False False False False False True True True True True] print(arr[mask])      # [6, 7, 8, 9, 10]

# Combined conditions

mask = (arr > 3) & (arr < 8)  # **AND** print(arr[mask])      # [4, 5, 6, 7]

mask = (arr < 3) | (arr > 8)  # OR print(arr[mask])      # [1, 2, 9, 10] Use Cases for Masking Data preprocessing

Scientific computing

Machine learning

Filtering invalid data

Applying thresholds

4.9 Reshaping Arrays python arr = np.arange(12)           # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# Reshape to 3x4 matrix

reshaped = arr.reshape(3, 4) # [[0, 1, 2, 3], #  [4, 5, 6, 7], #  [8, 9, 10, 11]]

# Flatten

flattened = reshaped.flatten() 4.10 Broadcasting Definition Broadcasting allows NumPy to perform element-wise operations on arrays of different shapes by automatically expanding smaller arrays to match the shape of larger ones.

### Broadcasting Rules

If arrays have different dimensions, prepend 1s to shape

Dimensions must match or one of them should be 1

Arrays with size 1 in a dimension get stretched

Examples python # Scalar broadcasting arr = np.array([1, 2, 3, 4]) result = arr * 2     # [2, 4, 6, 8] - 2 is broadcast to shape (4,)

# Array broadcasting

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])  # Shape (2, 3) arr_1d = np.array([10, 20, 30])             # Shape (3,) result = arr_2d + arr_1d  # arr_1d broadcast to (2, 3) # [[11, 22, 33], #  [14, 25, 36]] 4.11 Working with Files python # Saving arrays arr = np.array([1, 2, 3, 4, 5]) np.save('my_array.npy', arr)        # Binary .npy format np.savetxt('my_array.txt', arr)     # Text format

# Loading arrays

loaded_arr = np.load('my_array.npy') loaded_txt = np.loadtxt('my_array.txt')

# CSV files

data = np.loadtxt('data.csv', delimiter=',') 4.12 Statistical Operations Example python # Sales data analysis sales = np.array([**25000**, **31000**, **28000**, **35000**, **29000**, **40000**, **38000**])

mean_sales = np.mean(sales)      # Average sales std_sales = np.std(sales)        # Variability min_sales = np.min(sales)        # Minimum sale max_sales = np.max(sales)        # Maximum sale

print(f*Mean: ${mean_sales:.2f}*) print(f*Std Dev: ${std_sales:.2f}*) **UNIT** 5: **PANDAS** 5.1 Introduction to Pandas Definition Pandas is a fast, powerful, flexible, and easy-to-use open-source data analysis and manipulation tool built on top of Python.

Name Origin: *Panel Data* + *Python Data Analysis*

Created by: Wes McKinney (**2008**)

Why Use Pandas? Simplifies data manipulation, cleaning, and analysis

High-level data structures for intuitive operations

Built-in I/O tools for multiple formats (**CSV**, Excel, **SQL**)

Handles missing data elegantly

Strong integration with NumPy

5.2 Pandas Data Structures Series (1-Dimensional) Definition: A one-dimensional labeled array capable of holding any data type.

python import pandas as pd

# Creating a Series

s = pd.Series([2, 3, -2, 1]) print(s)

# Output:

# 0    2 # 1    3 # 2   -2 # 3    1 # dtype: int64 DataFrame (2-Dimensional) Definition: A two-dimensional table with labeled axes (rows and columns). Can be thought of as a dictionary of Series sharing the same index.

python
# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)
print(df)

# Output:

#       Name  Age      City
# 0    Alice   25  New York
# 1      Bob   30    London
# 2  Charlie   35     Paris
5.3 Indexing and Selecting Data
loc[] vs iloc[]
Method	Description	Example
loc[]	Label-based indexing	df.loc[0, 'Name'] → 'Alice'
iloc[]	Integer position-based indexing	df.iloc[0, 1] → 25
python
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['NY', 'London', 'Paris']
}, index=['a', 'b', 'c'])

# loc uses index labels

print(df.loc['a', 'Name'])     # 'Alice' print(df.loc['a':'b', 'Name'])  # 'a' to 'b' inclusive

# iloc uses integer positions

print(df.iloc[0, 0])            # 'Alice' (row 0, col 0)
print(df.iloc[0:2, 0:2])        # rows 0-1, cols 0-1
5.4 Basic DataFrame Methods
Method	Description
df.head(n)	Returns first n rows (default 5)
df.tail(n)	Returns last n rows (default 5)
df.info()	Displays DataFrame structure, data types, memory usage
df.describe()	Provides summary statistics of numerical columns
df.shape	Returns (rows, columns) tuple
df.sample(n)	Returns random n rows
Examples
python
df = pd.read_csv('data.csv')

print(df.head())      # First 5 rows print(df.tail(3))     # Last 3 rows print(df.info())      # Column names, types, non-null counts print(df.describe())  # count, mean, std, min, 25%, 50%, 75%, max print(df.shape)       # (**1000**, 10) - **1000** rows, 10 columns print(df.sample(5))   # Random 5 rows 5.5 Reading and Writing Data python # CSV df = pd.read_csv('data.csv') df.to_csv('output.csv', index=False)

# Excel

df = pd.read_excel('data.xlsx', sheet_name='Sheet1') df.to_excel('output.xlsx', index=False)

# JSON

df = pd.read_json('data.json') df.to_json('output.json')

# Text files

df = pd.read_table('data.txt', delimiter='\t')

# SQL

import sqlite3 conn = sqlite3.connect('database.db') df = pd.read_sql('**SELECT** * **FROM** table', conn) 5.6 Grouping and Aggregation groupby() Method python # Group by a column and aggregate grouped = df.groupby('Category')['Sales'].sum() print(grouped)

# Multiple aggregations

result = df.groupby('Category').agg({
    'Sales': ['sum', 'mean', 'count'],
    'Profit': 'sum'
})
Common Aggregate Functions with groupby
Function	Description
sum()	Sum of values
mean()	Average
count()	Number of non-null values
min()	Minimum
max()	Maximum
std()	Standard deviation
5.7 Pivot Tables
Syntax
python
pd.pivot_table(df, 
    values='Sales', 
    index='Region', 
    columns='Year', 
    aggfunc='sum')
Parameters
Parameter	Description
values	Column to aggregate
index	Row grouping variable
columns	Column grouping variable
aggfunc	Aggregation function (sum, mean, count, etc.)
fill_value	Value to replace missing values
Example
python
# Sales by region and year
pivot = pd.pivot_table(sales_df, 
    values='Revenue',
    index='Region',
    columns='Year',
    aggfunc='sum',
    fill_value=0)
5.8 Sorting and Filtering Data
python
# Sorting
df_sorted = df.sort_values(by='Age')           # Ascending (default)
df_sorted = df.sort_values(by='Age', ascending=False)  # Descending
df_sorted = df.sort_values(by=['Age', 'Name']) # Multiple columns

# Filtering

filtered = df[df['Age'] > 25] filtered = df[(df['Age'] > 25) & (df['City'] == 'New York')] filtered = df[df['Name'].str.startswith('A')] 5.9 Handling Missing Values Checking for Missing Values python # Check for missing values df.isnull()                    # Boolean DataFrame df.isnull().sum()              # Count per column df.isnull().sum().sum()        # Total missing count

# Check for non-missing

df.notnull().sum() Filling Missing Values (fillna) python # Fill with constant df.fillna(0)

# Fill with column mean

df['column_name'].fillna(df['column_name'].mean())

# Fill with column median

df['column_name'].fillna(df['column_name'].median())

# Forward fill (use previous value)

df.fillna(method='ffill')

# Backward fill (use next value)

df.fillna(method='bfill') Removing Missing Values (dropna) python # Remove rows with any missing values df.dropna()

# Remove rows where all values are missing

df.dropna(how='all')

# Remove columns with missing values

df.dropna(axis=1)

# Remove rows with missing values in specific columns

df.dropna(subset=['column1', 'column2']) ### Replacing Special Symbols python # Replace '?' with NaN df.replace('?', pd.NA)

# Replace multiple symbols

df.replace(['?', 'NA', 'null'], pd.NA) 5.10 Removing Duplicate Data python # Identify duplicates df.duplicated()                 # Boolean Series df.duplicated().sum()           # Count duplicates

# Remove duplicates

df.drop_duplicates()            # Remove all duplicate rows

# Remove duplicates based on specific columns

df.drop_duplicates(subset=['Name'])

# Keep last occurrence instead of first

df.drop_duplicates(keep='last') 5.11 Merging and Concatenation concat() - Stacking DataFrames python # Vertical stacking (row-wise) df_combined = pd.concat([df1, df2], axis=0)

# Horizontal stacking (column-wise)

df_combined = pd.concat([df1, df2], axis=1) merge() - Joining Based on Keys python # Inner join (only matching keys) merged = pd.merge(df1, df2, on='common_column')

# Left join (all from left, matching from right)

merged = pd.merge(df1, df2, on='common_column', how='left')

# Right join (all from right, matching from left)

merged = pd.merge(df1, df2, on='common_column', how='right')

# Outer join (all from both)

merged = pd.merge(df1, df2, on='common_column', how='outer')
Join Type	Description
inner	Only rows with matching keys in both tables
left	All rows from left table + matching from right
right	All rows from right table + matching from left
outer	All rows from both tables
5.12 Working with Dates and Times
python
# Convert to datetime
df['date'] = pd.to_datetime(df['date'])

# Extract components

df['year'] = df['date'].dt.year df['month'] = df['date'].dt.month df['day'] = df['date'].dt.day df['weekday'] = df['date'].dt.dayofweek

# Date filtering

df_filtered = df[(df['date'] >= '**2023**-01-01') & (df['date'] <= '**2023**-12-31')]

# Date as index

df.set_index('date', inplace=True) df.loc['**2023**-01-01':'**2023**-01-31']  # Select date range 5.13 Advanced DataFrame Operations apply() - Apply Function to Data python # Apply to column df['doubled'] = df['value'].apply(lambda x: x * 2)

# Apply to entire DataFrame

df = df.apply(lambda x: x * 2)

# Apply function to rows

df['sum'] = df.apply(lambda row: row['col1'] + row['col2'], axis=1) vectorized string operations python df['name'].str.lower()           # Convert to lowercase df['name'].str.contains('John')  # Check if contains df['name'].str.split()           # Split strings 5.14 Data Visualization with Pandas python # Line plot df['column'].plot() df.plot(x='date', y='sales')

# Bar plot

df['column'].value_counts().plot(kind='bar') df.plot(kind='bar', x='category', y='value')

# Histogram

df['column'].plot(kind='hist', bins=20)

# Scatter plot

df.plot(kind='scatter', x='x_column', y='y_column')

# Box plot

df.boxplot(column='value', by='category') 5.15 Performance Optimization Tips Vectorized operations are faster than loops

Use NumPy functions when possible

Use .apply() wisely (not always faster than vectorized)

Specify data types when reading files (dtype parameter)

Use chunksize for large files

python
# Instead of loop
for i in range(len(df)):
    df.loc[i, 'new'] = df.loc[i, 'a'] * 2

# Use vectorized operation

df['new'] = df['a'] * 2  # Much faster
**UNIT** 6: **STATISTICS** **FOR** **DATA** **SCIENCE**
6.1 Types of Statistics
Type	Description	Purpose
Descriptive Statistics	Summarize and describe data	Understand basic features
Inferential Statistics	Draw conclusions about population from sample	Make predictions, test hypotheses
6.2 Descriptive Statistics
Measures of Central Tendency
## Mean (Average)

Formula:
x
# ˉ
∑
# i
1
n
x
i
# n
x
1
- x
2
- .
.
.
- x
n
n
x
ˉ
 = 
n
∑ 
i=1
n
​
 x 
i
​
 
​
 = 
n
x 
1
​
 +x 
2
​
 +...+x 
n
​
 
​

Example: Pizza slices: 2, 3, 4, 6, 20
x
# ˉ
2
- 3
- 4
- 6
- 20
# 5
35
# 5
7
x
ˉ
 = 
5
2+3+4+6+20
​
 = 
5
35
​
 =7

Note: Mean is sensitive to outliers (20 slices skews the average).

Applications in Data Science:

Linear regression minimizes distance from mean

K-Means clustering uses mean

Performance evaluation (average returns)

Data imputation (fill missing values)

## Median

Definition: The middle value when data is arranged in ascending/descending order.

Calculation:

Odd number of values: Middle value

Even number of values: Average of two middle values

Example: Pizza slices: 2, 3, 4, 6, 20 (sorted) Median = 4 (the middle value)

Why Median? Tells reality better when outliers exist (someone eating 20 slices doesn't affect median).

Applications:

Robustness to outliers (billionaire doesn't skew median income)

Data imputation for skewed data

Decision Trees use median for balanced splits

Robust feature scaling

3. Mode

Definition: The most frequently occurring value(s).

Example: Shoe sizes sold: 7, 8, 8, 9, 8, 10 Mode = 8 (most common size)

Applications:

Categorical data analysis (most popular product)

Inventory management (most sold shoe size)

Data preprocessing imputation

Measures of Dispersion (Variability)
1. Range

Formula: Range = Maximum - Minimum

Example: Marks: 10, 20, 30, 40 Range = 40 - 10 = 30

Limitation: Only depends on extreme values (listens only to loudest students).

## Variance

Formula (Population): σ # 2 ∑ # i 1 n ( x i − μ ) 2 n σ 2 = n ∑ i=1 n ​ (x i ​ −μ) 2  ​

Formula (Sample): s # 2 ∑ # i 1 n ( x i − x ˉ ) 2 n − 1 s 2 = n−1 ∑ i=1 n ​ (x i ​ − x ˉ ) 2  ​

Explanation: Measures average squared deviation from the mean.

## Standard Deviation

Formula: # σ σ 2 σ= σ 2  ​

Why Important: Standard deviation is in the same unit as the original data (unlike variance).

Example Comparison:

Class A	Class B
70, 71, 69, 70, 70	40, 90, 30, **100**, 80
Mean = 70	Mean = 68
Low variance (consistent)	High variance (chaotic)
Applications:

Domain	Use
Finance	High standard deviation → high risk
Education	Low dispersion → consistent students
Manufacturing	Low variation → good quality
Quartiles and Percentiles
Quartiles: Divide dataset into four equal parts (each 25%)

Quartile	Percentile	Meaning
Q1	25th percentile	25% of data below this value
Q2	50th percentile	Median
Q3	75th percentile	75% of data below this value
Interquartile Range (**IQR**): **IQR** = Q3 - Q1
Measures spread of middle 50% of data.

Outlier Detection using **IQR**:

Lower bound: Q1 - 1.5 × **IQR**

Upper bound: Q3 + 1.5 × **IQR**

Data points outside these bounds are outliers

Percentiles: A percentile tells the value below which a certain percentage of data falls.

Example: 80th percentile = *80% of values are below this*

Percentile Usage:

Student Evaluation: **GRE**, **SAT** exams (marks alone are misleading)

Healthcare: Growth charts (height, weight, **BMI**)

Salary Analysis: 25th percentile (low range), 50th (median), 90th (top earners)

Skewness and Kurtosis Skewness: Measures asymmetry of data distribution

Type	Description	Example
Positive (Right) Skew	Tail on right side	Income distribution (few high earners)
Negative (Left) Skew	Tail on left side	Exam scores (most students score high)
Zero Skew	Symmetric	Normal distribution
Skewness Applications:

Identify if exam was too easy (negative skew)

Identify **VIP** customers (positive skew in spending)

Customer segmentation

Kurtosis: Measures *tailedness* of distribution (sharpness of peak)

Type	Description	Risk Implication
Leptokurtic (High)	Heavy tails, sharp peak	More extreme movements (high risk)
Mesokurtic	Normal distribution	Normal risk
Platykurtic (Low)	Light tails, flat peak	Less extreme movements (low risk)
Kurtosis Applications:

Finance: High kurtosis → extreme market movements → risk management needed

Education: High kurtosis → students either fail badly or score very high → uneven teaching effectiveness

6.3 Inferential Statistics Definition Inferential statistics allows us to make inferences about a population based on a sample of data drawn from that population.

Analogy: *You taste one spoon of soup to check salt* – you don't drink the whole soup.

6.4 Hypothesis Testing Definition A method for testing a claim or hypothesis about a parameter in a population using sample data.

### Key Concepts

Term	Definition
Null Hypothesis (H₀)	Statement of no effect or no difference
Alternative Hypothesis (H₁ or Ha)	Statement indicating presence of effect or difference
Significance Level (α)	Threshold for rejecting H₀ (commonly 0.05 or 0.01)
p-value	Probability of observing results if H₀ is true
Steps of Hypothesis Testing
State H₀ and H₁ hypotheses

Choose significance level α (0.05 or 0.01)

Select appropriate statistical test

Compute test statistic from sample data

Calculate p-value

Compare p-value with α → Reject or fail to reject H₀

Decision Rule:

p-value < α → Reject H₀ (results are statistically significant)

p-value ≥ α → Fail to reject H₀ (no significant evidence)

One-Tailed vs Two-Tailed Tests
Test Type	Description	Hypotheses Example
One-Tailed	Tests for effect in one direction	H₀: μ ≤ **165** cm, H₁: μ > **165** cm
Two-Tailed	Tests for effect in either direction	H₀: μ = 68 inches, H₁: μ ≠ 68 inches
Examples of Hypothesis Testing
Example 1: Education

Scenario: A school implements a new teaching method

H₀: The new teaching method has no effect on student performance

H₁: The new teaching method improves student performance

Example 2: Medical Research

Scenario: A new drug for blood pressure

H₀: The new drug does not lower blood pressure more effectively than existing drug

H₁: The new drug lowers blood pressure more effectively

Understanding p-value:

Small p-value → Surprising result → Reject H₀

Large p-value → Normal result → Accept H₀

6.5 Statistical Tests
Test	When to Use
Z-Test	Large sample size, known population standard deviation
T-Test	Small sample size, unknown population standard deviation, comparison of means
Chi-Square Test	Categorical data, testing for independence or goodness-of-fit
F-Test	Comparing variances of two or more groups (**ANOVA**)
6.6 Chi-Square Test
Purpose: Tests for independence between categorical variables.

Example Question: Is there a relationship between gender and product preference?

6.7 Correlation Analysis Definition Correlation establishes the relationships between two variables. Visualized using scatter plots.

Correlation Coefficient (r) Range: -1 to +1

r Value	Interpretation
r ≈ +1	Strong positive relationship (both increase together)
r ≈ -1	Strong negative relationship (one increases, other decreases)
r ≈ 0	Little or no relationship
Types of Correlation
Type	Description	Example
Positive	Variables move in same direction	Height and weight
Negative	Variables move in opposite direction	Price and demand
No Correlation	No linear relationship	Shoe size and IQ
### Correlation Methods
Method	Data Type
Pearson's r	Interval/ratio data (most widely used)
Spearman's rho	Ordinal data
6.8 Probability
Definition
Probability is a number between 0 and 1 that expresses the likelihood of an event occurring.

Formula: P(A) = favorable outcomes / total outcomes

### Key Probability Rules

## Addition Rule (OR)
P
(
A
∪
B
# )
P
(
A
)
- P
(
B
)
−
P
(
A
∩
B
)
P(A∪B)=P(A)+P(B)−P(A∩B)

## Multiplication Rule (AND)

P ( A ∩ B # ) P ( A ) t i m e s P ( B ∣ A ) P(A∩B)=P(A)timesP(B∣A) If independent: P ( A ∩ B # ) P ( A ) × P ( B ) P(A∩B)=P(A)×P(B)

## Complement Rule (NOT)

P ( A ′ # ) 1 − P ( A ) P(A ′ )=1−P(A)

Independent vs Dependent Events
Type	Description	Example
Independent	One event doesn't affect another	Coin toss outcomes
Dependent	One event affects another	Studying and passing
6.9 Applications of Statistics in Data Science
## Exploratory Data Analysis (EDA)
Histograms, box plots, scatter plots

Detect outliers, skewness, patterns

Correlation matrices & heatmaps

Understand feature distributions

## Data Preprocessing

Impute missing values using mean/median

Handle outliers (**IQR** method)

Normalize/standardize (z-score)

Feature scaling

## Machine Learning Foundations

Naive Bayes: Uses probability to make predictions

Linear/Logistic Regression: Models relationships

Decision Trees: Split data using entropy/information gain

Regularization: Prevents overfitting

## Model Evaluation & Validation

Accuracy, Precision, Recall, F1, **AUC**-**ROC**

Cross-validation

Confidence intervals

Statistical significance

## A/B Testing & Experiments

Control vs treatment

t-test / chi-square test

Sample size (power analysis)

## Time Series Analysis

Moving averages

Autocorrelation (**ACF**/**PACF**)

**ARIMA**/**SARIMA**

Stationarity tests (**ADF**)

**SEMESTER** 1: **QUICK** **REVISION** **SUMMARY**
### Key Formulas
Concept	Formula
Mean	
x
# ˉ
∑
x
i
n
x
ˉ
 = 
n
∑x 
i
​
 
​
 
Variance (sample)	
s
# 2
∑
(
x
i
−
x
ˉ
)
2
n
−
1
s 
2
 = 
n−1
∑(x 
i
​
 − 
x
ˉ
 ) 
2
 
​
 
Standard Deviation	
# s
s
2
s= 
s 
2
 
​
 
**IQR**	Q3 - Q1
Probability	P(A) = favorable/total
Correlation	-1 ≤ r ≤ +1
### Key Definitions
Term	Definition
Data Science	Art of learning from data
**CRISP**-DM	6-phase data mining framework
NumPy	Numerical computing library
Pandas	Data analysis library (DataFrame, Series)
Mean	Average value
Median	Middle value
Mode	Most frequent value
Variance	Average squared deviation from mean
Skewness	Asymmetry of distribution
Kurtosis	Tailedness of distribution
H₀	Null hypothesis (no effect)
H₁	Alternative hypothesis (effect exists)
p-value	Probability if H₀ is true
**SEMESTER** 2 (Weeks 7-12)
**UNIT** 7: **MACHINE** **LEARNING**
7.1 Introduction to Machine Learning
Definition
Machine Learning is a subfield of artificial intelligence that gives computers the ability to learn without being explicitly programmed. Systems learn from data and improve with experience.

Arthur Samuel (**1959**): "A system that learns from data and improves without being explicitly programmed."

7.2 Applications of Machine Learning
Domain	Application
Healthcare	Disease outbreak prediction, medical diagnosis
Finance	Fraud detection, credit scoring
Retail	Sentiment analysis, recommendation systems
Manufacturing	Quality control, predictive maintenance
Transportation	Autonomous vehicles, traffic prediction
7.3 Types of Machine Learning
text
### Machine Learning
├── Supervised Learning
│   ├── Classification (discrete labels)
│   └── Regression (continuous values)
├── Unsupervised Learning
│   ├── Clustering
│   ├── Association Rule Mining
│   └── Dimensionality Reduction
└── Reinforcement Learning
    ├── Game AI
    ├── Robotics
    └── Self-driving cars
7.4 Supervised Learning
Definition
Algorithms learn from labeled data, where input-output relationship is known.

Characteristics Uses historical labeled data

Has both input (features) and output (labels)

Goal: Predict output for new inputs

Types of Supervised Learning Problems
Type	Output	Examples
Classification	Discrete categories	Spam detection, tumor classification
Regression	Continuous values	House price prediction, test scores
7.5 Unsupervised Learning
Definition
Works with unlabeled data to discover hidden patterns or structures without predefined outputs.

Types
Type	Purpose	Example
Clustering	Group similar items	Customer segmentation
Association Rule Mining	Find item relationships	Market basket analysis
Dimensionality Reduction	Reduce number of features	**PCA**
7.6 Reinforcement Learning
Definition
Trains an agent to make decisions by interacting with an environment, learning through rewards and penalties.

Goal: Maximize long-term reward

Examples: Game AI, Robotics, Self-driving cars

7.7 Supervised Machine Learning Process
text
    ┌─────────────────┐
    │   Historical    │
    │   Labeled Data  │
    └────────┬────────┘
    │
    ┌────────▼────────┐
    │ Features (X)    │
    │ Labels (y)      │
    └────────┬────────┘
    │
    ┌──────────────┼──────────────┐
    │              │              │
    ┌────▼────┐    ┌─────▼─────┐  ┌─────▼─────┐
    │Training │    │   Test   │  │ Validation│
    │  (70%)  │    │  (30%)   │  │  (if used)│
    └────┬────┘    └─────┬─────┘  └───────────┘
    │               │
    ┌────▼────┐    ┌─────▼─────┐
    │  Train  │    │ Evaluate  │
    │  Model  │───►│Performance│
    └─────────┘    └─────┬─────┘
    │
    ┌─────────▼─────────┐
    │ Performance OK?   │
    └─────────┬─────────┘
    │
    ┌───────────────┼───────────────┐
    │               │               │
    ┌────▼────┐    ┌──────▼──────┐  ┌─────▼─────┐
    │ Adjust  │    │   Deploy   │  │  Monitor  │
    │Hyperpara│    │   Model    │  │Performance│
    └─────────┘    └────────────┘  └───────────┘
7.8 Regression
Definition
Regression is used to predict continuous values and understand the relationship between variables.

### Linear Regression

Simple Linear Regression:
# y
β
0
- β
1
x
- ε
y=β 
0
​
 +β 
1
​
 x+ε

Multiple Linear Regression:
# Y
b
0
- b
1
X
1
- b
2
X
2
- .
.
.
- b
n
X
n
Y=b 
0
​
 +b 
1
​
 X 
1
​
 +b 
2
​
 X 
2
​
 +...+b 
n
​
 X 
n
​

Where:

Y = dependent variable (output)

X = independent variables (inputs)

β₀ = y-intercept

β₁ = slope

Example - House Price Prediction:

Model: Price = b₀ + b₁ × Size

If b₀ = **50000**, b₁ = **250**

House with **1800** sq ft: Price = **50000** + **250** × **1800** = **500**,**000**

### Linear Regression Code Example

python import numpy as np import pandas as pd from sklearn.model_selection import train_test_split from sklearn.linear_model import LinearRegression from sklearn.metrics import mean_squared_error, r2_score

# Create sample data

np.random.seed(42) data_size = **150** Feature = np.random.rand(data_size) * 10 Target = 3.5 * Feature + np.random.randn(data_size) * 2

# Create DataFrame

df = pd.DataFrame({'Feature': Feature, 'Target': Target})

# Split data

X = df[['Feature']] y = df['Target'] X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train model

model = LinearRegression() model.fit(X_train, y_train)

# Predict

y_pred = model.predict(X_test)

# Evaluate

mse = mean_squared_error(y_test, y_pred) r2 = r2_score(y_test, y_pred)

print(f*Slope (b₁): {model.coef_[0]:.2f}*) print(f*Intercept (b₀): {model.intercept_:.2f}*) print(f***MSE**: {mse:.2f}*) print(f*R²: {r2:.2f}*) 7.9 Logistic Regression Definition Used for binary classification problems. Predicts the probability that a given input belongs to a particular category.

Sigmoid Function (Logistic Function):
P
(
# y
1
# )
1
1
- e
−
(
β
0
- β
1
x
)
P(y=1)= 
1+e 
−(β 
0
​
 +β 
1
​
 x)
 
1
​

Key Characteristics:

Output is probability between 0 and 1

S-shaped curve

Used for: spam detection, heart attack prediction, enrollment prediction

### Logistic Regression Example

python from sklearn.datasets import load_iris from sklearn.linear_model import LogisticRegression from sklearn.metrics import accuracy_score, classification_report

# Load data

iris = load_iris() X = iris.data y = iris.target

# Split data

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train model

model = LogisticRegression(max_iter=**200**) model.fit(X_train, y_train)

# Predict and evaluate

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f*Accuracy: {accuracy:.2f}*)
print(classification_report(y_test, y_pred, target_names=iris.target_names))
7.10 Common ML Algorithms Comparison
Algorithm	Type	Use Case	Pros	Cons
Linear Regression	Regression	Continuous prediction	Simple, interpretable	Assumes linearity
Logistic Regression	Classification	Binary classification	Probabilistic output	Assumes linear decision boundary
Decision Trees	Both	Interpretable models	Easy to understand	Prone to overfitting
K-Nearest Neighbors	Both	Pattern recognition	No training phase	Slow for large datasets
**SVM**	Classification	Complex boundaries	Effective in high dimensions	Less interpretable
7.11 Feature Engineering
Definition
Using domain knowledge to extract features from raw data for better model performance.

Approaches ## Extracting Information

From timestamp ***2020**-10-9 09:11:13*:

Year: **2020**

Month: 10

Day: 9

Hour: 9

Minute: 11

## Combining Information

Adding marks of two terms

Adding sales of various quarters

## Transforming Information (Encoding)

Integer Encoding: Converts categories to integers 1, 2, 3, ..., N

python # Before: ['Red', 'Blue', 'Red', 'Green'] # After:  [1, 2, 1, 3] One-Hot Encoding (Dummy Variables): Converts each category into individual binary features (0 or 1)

python # Before: ['Red', 'Blue', 'Red', 'Green'] # After: #   Red  Blue  Green #   1    0     0 #   0    1     0 #   1    0     0 #   0    0     1 Note: One-hot encoding can cause feature duplication. One column can be dropped (dummy variable trap).

**UNIT** 8: **RELATIONAL** **DATABASES** & **SQL** 8.1 Introduction to Data Structures Definition Data structure is data organization, management, and storage format that enables efficient access and modification.

Types of Data
text
### Data Types
├── Structured Data
│   ├── **CSV**, Spreadsheets
│   ├── Relational database tables
│   └── Flat files
├── Unstructured Data
│   ├── Text files
│   ├── Photographs
│   ├── Videos
│   └── Audio recordings
└── Semi-structured Data
    ├── **JSON**
    └── **XML**
Type	Format	Example	Query Efficiency
Structured	Schema-defined	**SQL** tables	High
Unstructured	No format	Images, videos	Low
Semi-structured	Partial schema	**JSON**, **XML**	Medium
8.2 Relational Data Model
Definition
A model where data is organized in tables with rows and columns, with relationships between tables.

Example: A single Excel sheet is a relational data model (2D), with:

Columns containing same type of information

Rows representing the same object/event

Relations between all columns belonging to a row

### Key Terms

Term	Definition
Attribute	Properties that describe an entity (e.g., ROLL_NO, **NAME**)
Relation Schema	Structure showing name and attributes (e.g., **STUDENT**(ROLL_NO, **NAME**))
Tuple	A single row representing one record
Relation Instance	Set of tuples at a specific time
Degree	Total number of attributes
Cardinality	Total number of tuples (rows)
**NULL** Value	Unknown, missing, or not available value
8.3 Types of Keys
Key Type	Definition	Example
Primary Key	Uniquely identifies each tuple; cannot be **NULL**	student_id
Candidate Key	Set of attributes that can uniquely identify a tuple	email, citizenship_no
Super Key	Set of attributes that can uniquely identify a tuple	(student_id, name)
Foreign Key	Attribute in one table that refers to primary key of another	course_id in Enrollment
Composite Key	Two or more attributes combined to uniquely identify	(student_id, course_id)
Alternate Key	Candidate key not used as primary key	email (if student_id is PK)
**SQL** Example - Creating Keys
sql
**CREATE** **TABLE** Student (
    student_id **INT** **PRIMARY** **KEY**,              -- Primary Key
    email **VARCHAR**(**100**) **UNIQUE**,               -- Unique Key
    citizenship_no **VARCHAR**(50) **UNIQUE**,       -- Candidate Key
    name **VARCHAR**(**100**) **NOT** **NULL**
);

**CREATE** **TABLE** Course (
    course_id **VARCHAR**(10) **PRIMARY** **KEY**,
    course_name **VARCHAR**(**100**) **NOT** **NULL**
);

**CREATE** **TABLE** Enrollment (
    student_id **INT**,
    course_id **VARCHAR**(10),
    enrollment_date **DATE**,
    **PRIMARY** **KEY** (student_id, course_id),     -- Composite Key
    **FOREIGN** **KEY** (student_id) **REFERENCES** Student(student_id),
    **FOREIGN** **KEY** (course_id) **REFERENCES** Course(course_id)
);
8.4 **SQL** (Structured Query Language)
Basic **SQL** Commands
**SELECT** and **WHERE** - Retrieve and filter rows

sql **SELECT** * **FROM** Customers **WHERE** Country = 'Nepal'; **ORDER** BY - Sort results

sql **SELECT** * **FROM** Products **ORDER** BY Price; -- **DESC** for descending order **SELECT** * **FROM** Products **ORDER** BY Price **DESC**; **BETWEEN** - Select values within range (inclusive)

sql **SELECT** * **FROM** Products **WHERE** Price **BETWEEN** 10 **AND** 20; 8.5 **SQL** Joins Purpose Combine data from two or more tables based on a related column (usually a key).

### Join Types

text Join Types Visualization:

**INNER** **JOIN**:      **LEFT** **JOIN**:        **RIGHT** **JOIN**:       **FULL** **JOIN**: ┌─────┬─────┐    ┌─────┬─────┐     ┌─────┬─────┐     ┌─────┬─────┐ │     │     │    │█████│     │     │     │█████│     │█████│█████│ │  █  │  █  │    │█████│  █  │     │  █  │█████│     │█████│█████│ │     │     │    │█████│     │     │     │█████│     │█████│█████│ └─────┴─────┘    └─────┴─────┘     └─────┴─────┘     └─────┴─────┘ Only overlap     All left          All right        Everything **INNER** **JOIN** Returns only matching records from both tables.

sql **SELECT** s.student_id, s.name, e.course **FROM** Student s **INNER** **JOIN** Enrollment e ON s.student_id = e.student_id; **LEFT** **JOIN** (**LEFT** **OUTER** **JOIN**) Returns all records from left table + matching from right.

sql **SELECT** s.student_id, s.name, e.course **FROM** Student s **LEFT** **JOIN** Enrollment e ON s.student_id = e.student_id; **RIGHT** **JOIN** (**RIGHT** **OUTER** **JOIN**) Returns all records from right table + matching from left.

sql **SELECT** s.student_id, s.name, e.course **FROM** Student s **RIGHT** **JOIN** Enrollment e ON s.student_id = e.student_id; **FULL** **JOIN** (**FULL** **OUTER** **JOIN**) Returns all records from both tables.

sql **SELECT** s.student_id, s.name, e.course **FROM** Student s **FULL** **OUTER** **JOIN** Enrollment e ON s.student_id = e.student_id; **CROSS** **JOIN** Returns Cartesian product (all combinations).

sql
**SELECT** s.name, e.course
**FROM** Student s
**CROSS** **JOIN** Enrollment e;
-- Rows = (Students count × Enrollments count)
8.6 Aggregate Functions
Function	Description
**COUNT**()	Number of rows
**SUM**()	Sum of values
**AVG**()	Average
**MAX**()	Maximum value
**MIN**()	Minimum value
sql
**SELECT** 
    **COUNT**(*) as total_students,
    **AVG**(marks) as average_marks,
    **MAX**(marks) as highest_mark
**FROM** Students;
**UNIT** 9: **DATA** **WAREHOUSING**
9.1 Challenges of Current Business Environment
The Data Problem Today:

Large and varied datasets generated daily from many disconnected sources

Example: Amazon processes over 3.75 million orders per day from website, mobile app, Alexa, third-party sellers, warehouses — all in different formats

Solution Requirements:

Centralized repository

Integrated data

Summarized or aggregated information

Easy and quick retrieval/analysis of data

9.2 What is Data Warehousing? Definition Data warehousing is a data management technology that provides a central repository of corporate data optimized for reporting, ad hoc queries, and analysis purposes.

Alternative Definition: A single, complete, and consistent store of data obtained from a variety of sources and made available to end users in a way they can understand and use in business context.

9.3 Properties of a Data Warehouse
Property	Description
Subject-Oriented	Organized around major business subjects, not departments or locations
Integrated	Consistent across systems, unified view from different sources
Time-Variant	Accurate and valid at a specific point or over a time interval
Non-Volatile	Once recorded, data stays in warehouse (not updatable or removable)
9.4 Why Data Warehousing?
Purpose: Meet reporting and analysis requirements of a business or enterprise.

Benefits:

Integrates enterprise-wide corporate data into single centralized repository

Business users can easily and quickly:

Run queries

Produce reports

Perform analysis

Example Business Questions:

What has been total sale by product this year to date?

Which products are popular or profitable in past four weeks?

What was effect of promotion on sales volume or revenue?

What is future demand of each product category?

9.5 Data Warehouse Architecture
text
    ┌─────────────────────────────────────┐
    │         Data Access Tools           │
    │  (Reporting, Queries, Analysis, DM) │
    └─────────────────┬───────────────────┘
    │
    ┌─────────────────▼───────────────────┐
    │        Data Presentation Area       │
    │  (Metadata, Detailed Data, Summary) │
    └─────────────────┬───────────────────┘
    │
    ┌─────────────────▼───────────────────┐
    │          Data Staging Area          │
    │         (**ETL** Processes)             │
    └─────────────────┬───────────────────┘
    │
    ┌─────────────────▼───────────────────┐
    │        Operational Data Sources     │
    │  (Databases, Files, Web Services)   │
    └─────────────────────────────────────┘
Components:

Operational Data Sources: Various sources for data collection

Data Staging Area: **ETL** processes (Extract, Transform, Load)

Data Presentation Area: Centralized storage (metadata, detailed data, summarized data)

Data Access Tools: Reporting, ad hoc queries, analysis, data mining

9.6 Advantages and Disadvantages
Advantages	Disadvantages
Potential high **ROI**	Problems with source systems
Increased competitive advantage	Required data might not be available
Improved productivity of decision-makers	Long project duration
Stores only structured data
9.7 Dimensional Data Modeling
Definition
A design technique used in data warehousing to organize data into fact tables and dimension tables.

Table Type	Description	Characteristics
Fact Table	Stores numerical data about business activities	Has foreign keys to dimensions, usually very large
Dimension Table	Stores descriptive information about facts	Contains attributes (text/categorical), helps filter
9.8 Data Warehouse Schemas
## Star Schema
Structure: One central fact table connected to multiple dimension tables (star-like shape).

text
    ┌─────────────┐
    │   Time_Dim  │
    └──────┬──────┘
    │
┌──────────────┼──────────────────┐
│ Product_Dim──┼───Sales_Fact─────┼───Customer_Dim
└──────────────┼──────────────────┘
    │
    ┌──────▼──────┐
    │  Store_Dim  │
    └─────────────┘
Advantages:

Simple queries, easy joins

Faster data retrieval

Good for **OLAP**

Disadvantages:

Redundancy (duplicate data)

Less flexible for changing requirements

Many-to-many issues need bridge tables

## Snowflake Schema

Structure: Extension of star schema where dimension tables are normalized (broken into subdimensions). **ERD** looks like a snowflake.

Advantages:

Less redundancy

Saves storage space

Disadvantages:

More complex queries

Slower performance (more joins)

## Fact Constellation Schema (Galaxy Schema)

Structure: Multiple fact tables sharing common dimensional tables.

Advantages:

Enhanced query performance

Flexibility in reporting

Improved scalability

Disadvantages:

Increased design complexity

Performance issues with complex queries

Data redundancy and storage overhead

9.9 **OLAP** vs **OLTP**
Feature	**OLAP**	**OLTP**
Purpose	Analysis, reporting	Transaction processing
Queries	Complex, read-intensive	Simple, write-intensive
Data	Historical, summarized	Current, detailed
Updates	Periodic batch	Real-time
Users	Analysts, managers	Customers, clerks
Design	Star/Snowflake schemas	Normalized (**3NF**)
**OLAP** (Online Analytical Processing):

Software tools for data analysis in business decision-making

Allows extracting and viewing data from various perspectives

Used for trend analysis, financial forecasting, in-depth data analysis

**OLTP** (Online Transaction Processing):

Data processing for real-time execution of transactions

Manages daily operational data with fast insert, update, delete

Supports **ACID** properties (Atomicity, Consistency, Isolation, Durability)

9.10 Operational Database vs Data Warehouse
Aspect	Operational Database	Data Warehouse
Purpose	Day-to-day operations	Analysis and reporting
Data	Point-by-point, current status	Historical, aggregated
Updates	Frequent (real-time)	Periodic (batch)
Query type	Simple transactions	Complex analytical
Users	Operational staff	Decision-makers
9.11 Data Mining
Definition
Extracts hidden patterns and relationships from large datasets to help organizations analyze historical data and make data-driven decisions.

Techniques:

Classification

Clustering

Regression

### Association Rules

Applications:

Marketing

Finance

Healthcare

Business analytics

**UNIT** 10: **POWER** BI 10.1 Introduction to Business Intelligence Definition BI is a set of processes, architectures, and technologies that convert raw data into meaningful information that drives profitable business actions. BI combines business analytics, data mining, data visualization, data tools, and best practices.

10.2 What is Microsoft Power BI? Definition Power BI is an interactive data visualization software product developed by Microsoft, with a primary focus on business intelligence. Part of the Microsoft Power Platform.

Components
Component	Purpose
Power Query	Cleans and transforms raw data
Power Pivot	Builds data models and relationships using **DAX**
Power View	Creates basic visual reports (mostly replaced)
Power BI Desktop	Main tool to create reports and dashboards
Power BI Gateway	Connects local data to cloud for updates
Power BI Mobile Apps	Access dashboards on mobile devices
Power BI Service	Share, publish, and collaborate online
10.3 Features of Power BI
Business analytics solution for data visualization and insight sharing

Embed visuals in applications or websites

Import data from **100**+ different data sources

Cost-effective compared to other visualization tools

10.4 Power BI vs Other Tools
Feature	Power BI	Tableau	Google Data Studio
Price	Low (starting ~$10/user)	High (starting ~$70/user)	Free
Data Sources	**100**+	75+	Limited
Ease of Use	Moderate	Advanced	Simple
Integration	Microsoft ecosystem	Many	Google products
Mobile App	Yes	Yes	Yes
10.5 Evolution of Power BI
Before **2010** - Excel Only:

Data in multiple sheets (Sales, Products, Regions)

Manual **VLOOKUP** to combine data

Slow with large datasets

No automatic relationships

Limited visualization

**2010**-**2013** - Power Pivot & Power Query (Excel add-ins):

Import multiple tables

Create relationships

Clean data automatically

Interactive charts with Power View/Map

**2015** - Standalone Power BI:

Independent BI tool

Integrated data modeling, transformation, visualization

Real-time analytics, AI features

Big data integration

10.6 Why Power BI Was Introduced
Limitation in Excel	Power BI Solution
Struggles with millions of rows	In-memory storage (VertiPaq engine)
Limited data connectivity	**100**+ data sources (**SQL**, APIs, cloud)
Static charts and PivotTables	Real-time interactive dashboards
Difficult to share	Power BI Service for cloud sharing
10.7 Power BI Interface
View Navigator (Left): Switch between Report, Data, Model, **DAX** query views

Get Data Button (Top): Connect to various data sources

Visualizations Pane (Right): Select, configure, format charts

Page Navigator (Bottom): Create, rename, navigate between pages

10.8 Loading and Transforming Data in Power BI Steps:

Click *Get Data* → Select Excel

Choose worksheet

Load or Transform Data

In Power Query Editor:

Remove columns

Change data types

Fill missing values

Filter rows

Click *Close & Apply*

Filling Missing Values in Power Query:

Select column

Right-click → Replace Values

Or use Transform → Fill → Down/Up

**UNIT** 11: **WEB** **SCRAPING** 11.1 What is Web Scraping? Definition Web scraping is the automated process of extracting structured or semi-structured data from websites using software or scripts.

Characteristics:

Automated: Scripts run without manual intervention

Structured Data: Convert unstructured web content to usable formats

At Scale: Process thousands of pages efficiently

Non-invasive: Uses public **HTTP** requests like regular users

11.2 Why Web Scraping?
Purpose	Application
Data Collection	Gather market data, prices, reviews at scale
Competitive Analysis	Monitor competitors' products and pricing
Content Aggregation	Collect news, articles, information
Research & Analysis	Analyze trends and patterns
Automation	Automate repetitive data collection
Business Intelligence	Extract insights for strategic decisions
11.3 Steps in Web Scraping
text
## Send HTTP Request
   └── Use requests library to fetch **HTML** content

## Parse HTML Content

└── Use parser (html.parser, html5lib) to create parse tree

## Extract Data

    └── Use BeautifulSoup to navigate parse tree
    └── Target specific tags, classes, IDs

## Save Data

└── Export to **CSV**, **JSON**, or database 11.4 BeautifulSoup Library Definition BeautifulSoup is a Python library for parsing **HTML**/**XML** that works with multiple parsers. It is lightweight, intuitive, and great for web scraping.

Key Advantages:

Simple syntax

Powerful parsing

Active community

Well documented

11.5 Web Scraping Implementation Step 1: Install Required Libraries bash pip install requests beautifulsoup4 Step 2: Import Libraries python import requests from bs4 import BeautifulSoup import csv Step 3: Fetch **HTML** Content python url = *[https://example.com/quotes*](https://example.com/quotes") response = requests.get(url) html_content = response.text  # Returns **HTML** as string Step 4: Parse **HTML** with BeautifulSoup python soup = BeautifulSoup(html_content, 'html.parser') Step 5: Extract Data python # Find all quote containers quotes = soup.find_all('div', class_='quote')

# Extract specific data

for quote in quotes:
    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
Step 6: Save Data to **CSV**
python
with open('quotes.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['text', 'author'])
    writer.writeheader()
    for quote in quotes_data:
    writer.writerow(quote)
11.6 **HTTP** Requests & Responses
Component	Description
**GET**	Request data from server
**POST**	Send data to server
Status **200**	OK - Request successful
Status **404**	Not Found - Resource doesn't exist
Headers	Metadata about request/response
Body	**HTML** content of the page
11.7 **HTML** Basics
html
<!**DOCTYPE** html>
<html>
<head>
    <title>Page Title</title>
</head>
<body>
    <h1>Heading</h1>
    <p class=*description*>Paragraph text</p>
    <div id=*main-content*>
    <a href=*[https://example.com*>Link</a>](https://example.com">Link</a>)
    </div>
</body>
</html>
Key Elements: Tags, Attributes, Classes, IDs, Hierarchy

11.8 **CSS** Selectors for Web Scraping
Selector	Description
div	Select all <div> tags
.classname	Select elements with class 'classname'
#id	Select element with id 'id'
div.special	Select <div> with class 'special'
ul > li	Select <li> direct children of <ul>
a[href]	Select <a> tags with href attribute
11.9 Handling Headers & User-Agent
python
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/**537**.36'
}
response = requests.get(url, headers=headers)
11.10 Error Handling
python
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # Raises error for 4xx/5xx
except requests.exceptions.RequestException as e:
    print(f*Error: {e}*)
11.11 Legal & Ethical Considerations
✅ DO's	❌ **DON**'Ts
Check robots.txt	Overload servers
Read Terms of Service	Bypass authentication
Respect rate limits	Scrape personal data
Use appropriate delays	Ignore Copyright
Set User-Agent header	Claim data as your own
Cache data when possible	Block legitimate users
Cite sources	
11.12 Handling JavaScript Content
Challenge: BeautifulSoup can't handle JavaScript-loaded content.

Solutions:

Selenium (Browser Automation)

python from selenium import webdriver driver = webdriver.Chrome() driver.get(url) html = driver.page_source soup = BeautifulSoup(html, 'html.parser') Check for **API** calls

python
import json
api_url = '[https://api.example.com/data'](https://api.example.com/data')
response = requests.get(api_url)
data = response.json()
11.13 Common Issues & Debugging
Issue	Solution
**404** Error	Check **URL**, verify site accessibility
Empty Results	Inspect page structure, check selectors
Timeout	Increase timeout, add retries
Blocked/**403**	Add headers, use proxies, slow down
Bad Encoding	Specify encoding: BeautifulSoup(..., 'encoding=utf-8')
Dynamic Content	Use Selenium, check **API** calls
11.14 Related Tools & Libraries
Tool	Purpose
Selenium	Browser automation, handle JavaScript
Scrapy	Full-featured web scraping framework
Requests	**HTTP** library (covered)
Playwright	Modern browser automation
lxml	Fast **XML**/**HTML** processing
Puppeteer	Node.js browser automation
11.15 Best Practices Summary
Always check robots.txt and Terms of Service

Respect server resources with delays (time.sleep())

Set proper User-Agent headers

Implement error handling and retry logic

Use sessions for multiple requests

Cache data locally to minimize requests

Validate and clean extracted data

Log errors and activities for debugging

Consider using APIs when available

Keep scraper maintainable and documented

**UNIT** 12: **REVISION** & **EXAM** **PREPARATION**
12.1 Module Summary by Week
Week	Topic	Key Concepts
1	Data Science Introduction	**CRISP**-DM, **EDA**, Applications
2-4	Python Libraries	NumPy, Pandas, Data structures
5	Data Visualization	Matplotlib (line, bar, scatter, hist, pie)
6	Statistical Analysis	Mean, median, mode, variance, skewness, kurtosis, hypothesis testing
7	Machine Learning	Supervised/Unsupervised, Linear/Logistic Regression
8	Database & **SQL**	Relational model, Joins, Keys
9	Data Warehouse	Schemas (Star, Snowflake), **OLAP** vs **OLTP**
10	Power BI	BI tools, Data visualization
11	Web Scraping	BeautifulSoup, Requests, Ethics
12.2 Important Exam Questions
Theory Questions (High Probability)
🔥 Highly Important for Exam

Explain the **CRISP**-DM methodology with all six phases.

Differentiate between supervised and unsupervised learning with examples.

Explain the difference between loc[] and iloc[] in Pandas.

What is the difference between structured, unstructured, and semi-structured data?

Explain **INNER** **JOIN**, **LEFT** **JOIN**, **RIGHT** **JOIN**, and **FULL** **JOIN** in **SQL**.

Differentiate between Star Schema and Snowflake Schema.

What are the properties of a Data Warehouse?

Explain the difference between **OLAP** and **OLTP**.

What are the steps involved in web scraping using BeautifulSoup?

Explain the difference between mean, median, and mode with examples.

Quantitative/Numerical Questions Calculate mean, median, mode for a given dataset.

Calculate variance and standard deviation.

Interpret skewness and kurtosis values.

Apply **IQR** method to detect outliers.

Calculate probability using addition and multiplication rules.

Interpret correlation coefficient values.

Code-Based Questions Write code to create a NumPy array and perform basic operations.

Write code to load a **CSV** file in Pandas and handle missing values.

Write code to create a DataFrame and use loc/iloc.

Write code to create a bar plot and scatter plot using Matplotlib.

Write code to implement Linear Regression using scikit-learn.

Write **SQL** queries using **SELECT**, **WHERE**, **JOIN**.

Write code to scrape data from a website using BeautifulSoup.

### Viva Questions

What is data science?

Why is Python used for data science?

What is the difference between a list and a tuple?

What is the purpose of NumPy?

What is a DataFrame in Pandas?

What is the difference between correlation and causation?

What is a p-value?

What is the difference between classification and regression?

What is feature engineering?

What is the purpose of **ETL**?

12.3 Quick Reference: Key Formulas
Concept	Formula
Mean	
x
# ˉ
∑
x
i
n
x
ˉ
 = 
n
∑x 
i
​
 
​
 
Sample Variance	
s
# 2
∑
(
x
i
−
x
ˉ
)
2
n
−
1
s 
2
 = 
n−1
∑(x 
i
​
 − 
x
ˉ
 ) 
2
 
​
 
Sample Std Dev	
# s
s
2
s= 
s 
2
 
​
 
**IQR**	
I
Q
# R
Q
3
−
Q
1
**IQR**=Q3−Q1
Outlier bounds	
[
Q
1
−
1.5
×
I
Q
R
,
Q
3
- 1.5
×
I
Q
R
]
[Q1−1.5×**IQR**,Q3+1.5×**IQR**]
Probability	
P
(
A
# )
favorable
total
P(A)= 
total
favorable
​
 
Addition Rule	
P
(
A
∪
B
# )
P
(
A
)
- P
(
B
)
−
P
(
A
∩
B
)
P(A∪B)=P(A)+P(B)−P(A∩B)
Linear Regression	
# y
β
0
- β
1
x
y=β 
0
​
 +β 
1
​
 x
Sigmoid (Logistic)	
P
(
# y
1
# )
1
1
- e
−
z
P(y=1)= 
1+e 
−z
 
1
​
 
12.4 Quick Reference: Python/Pandas Methods
Task	Code
Create DataFrame	pd.DataFrame({'col': [1,2,3]})
Read **CSV**	pd.read_csv('file.csv')
First 5 rows	df.head()
Info	df.info()
Describe stats	df.describe()
Filter	df[df['col'] > 5]
Fill NaN	df.fillna(0)
Drop NaN	df.dropna()
Group by	df.groupby('col').sum()
Merge	pd.merge(df1, df2, on='key')
Pivot table	pd.pivot_table(df, values='v', index='i', columns='c')
12.5 Quick Reference: **SQL** Commands
Task	Code
Select all	**SELECT** * **FROM** table;
Filter	**SELECT** * **FROM** table **WHERE** condition;
Sort	**SELECT** * **FROM** table **ORDER** BY col;
Inner Join	**SELECT** * **FROM** t1 **INNER** **JOIN** t2 ON t1.id = t2.id;
Left Join	**SELECT** * **FROM** t1 **LEFT** **JOIN** t2 ON t1.id = t2.id;
Count	**SELECT** **COUNT**(*) **FROM** table;
Group by	**SELECT** col, **COUNT**(*) **FROM** table **GROUP** BY col;
# END OF COMPLETE STUDY NOTES

*These notes cover all content from the uploaded lectures (Weeks 1-12) and tutorial materials. For practical demonstrations and code execution, please refer to the original lab files.*
