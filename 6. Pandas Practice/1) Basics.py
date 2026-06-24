import pandas as pd

df = pd.read_csv('data.csv')
print(df.to_string())
print()

#Pandas Series - column in a table, 1D array holding any type of data
nums = [1, 2, 3, 4, 5]

mySeries = pd.Series(nums) #wraps nums list and wraps it inside a Series object 
print(mySeries) #labels will be 0,1,2, etc if not specified with 'index'
print()
print(mySeries[0]) #prints the first value of the Series
print()



#Creating labels for dataframe

nums = [1, 7, 2]
mySeries = pd.Series(nums, index = ["x", "y", "z"])
print(mySeries)
print(mySeries["x"]) #accesses an item by referring to the label
print()


#Creating a Series from a dictionary 

calories = {"Day 1" : 420, "Day 2" : 380, "Day 3" : 390}
myCalSeries = pd.Series(calories) #The keys in the dict become the labels
print(myCalSeries)
print()

#Selecting only some items from the dict
myCalSeries = pd.Series(calories, index = ["Day 1", "Day 2"]) #The keys in the dict become the labels
print(myCalSeries)
print()


#DataFrames - multi-dimensional tables/data sets

#Creating a DataFrame from two Series
myDataSet = { 
    'cars': ['BMW', 'Volvo', 'Ford'],
    'passengers': [3, 7, 2]
}

myDataFrame = pd.DataFrame(myDataSet) #loads data into a DataFrame object

print(myDataFrame)
print()


data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data)
print(df)
print()

#loc attribute
print(df.loc[0]) #prints data from first row in the form of a Series
print(df.loc[[0, 1]]) #prints first two rows in the form of a DataFrame

df = pd.DataFrame(data, index = ["Day 1", "Day 2", "Day 3"])
print(df)

print(df.loc["Day 2"]) #returns data from "Day 2" row in Series form


#Loading files into a DataFrame - CSV (comma separated file)

df = pd.read_csv('data.csv')
print(df.to_string()) #prints the entire table
print(df) #if have large DataFrame then only prints the first and last 5 rows, prints dimensions too

print(pd.options.display.max_rows) #max rows for my system is 60, so if df has > 60 will shorten it
pd.options.display.max_rows = 9999 #can manually change the max_rows
df = pd.read_csv('data.csv')
print(df)

#"Big data sets are often stored, or extracted as JSON." 
#"JSON is plain text, but has the format of an object, and is well known in the world of programming, including Pandas."
#"JSON objects have the same format as Python dictionaries."


#Loading a Python Dictionary into a DataFrame

import pandas as pd

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)

print(df) 



#Analysing DataFrames

df = pd.read_csv('data.csv') #automatically creates a DataFrame
print(df.head(10)) #prints the headers and the first 10 rows of the df
print(df.head()) #if no of rows are not specified then it will print the first 5 rows

print(df.tail()) #prints the headers and the last 5 rows

print(df.info()) #tells you no of rows and cols, names of cols and data type, no of non-null values
