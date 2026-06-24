#Cleaning data

#Bad data is:
# - empty cells
# - data in wrong format
# - wrong data
# - duplicates

import pandas as pd

#Removing rows with empty cells

df = pd.read_csv('data2.csv')
print(df.to_string())
new_df = df.dropna() #removes all rows with any missing cells, but doesn't change the OG DataFrame, dropna() returns a new df
print(new_df.to_string()) 


#df.dropna(inplace = True) #to change the original df then use 'inplace = True'
#print(df.to_string())


#Replace Empty Values For Specified Columns

new_df = df.fillna({"Calories" : 130})
print(new_df.to_string())


#Replacing cells with Mean, Median, Mode

x = df["Calories"].mean() #selects the 'Calories' column from the table
new_df = df.fillna({"Calories": x})
print(new_df.to_string())

y = df["Calories"].median()
new_df = df.fillna({"Calories" : y})
print(new_df)

#print(df["Calories"].mode()) returns 0 300.0
z = df["Calories"].mode()[0] #need [0] to select the first winner of the mode if there is a tie
new_df = df.fillna({"Calories": z})
print(new_df.to_string())

date = " '2020/12/22' "
new_df = df.fillna({"Date": date})
print(new_df.to_string())


print(df.isnull().sum()) #prints a list of the columns with the counts of blanks


#df.fillna({"Date" : date,"Calories" : x}, inplace = True) #one single dictionary and replaces all missing values in the table
#print(df.to_string())


#Converting cells in the correct format

df["Date"] = pd.to_datetime(df['Date'], format ='mixed')
print(df.to_string)

df.dropna(subset = ['Date'], inplace = True) # removes row with NULL value in the 'Date' column


#Replacing Wrong Values

df.loc[7, 'Duration'] = 45 # replaces the cell if you know where the mistake is

#For bigger datasets can set any value that complies with a rule to a certain value

for x in df.index:
    if df.loc[x, 'Duration'] > 120:
        df.loc[x, 'Duration'] = 120

# removes all rows where the duration > 120

for x in df.index:
    if df.loc[x, 'Duration'] > 120:
        df.drop(x, inplace = True)


#Removing Duplicates

#for x in df.index:
#    if df.loc[x, 'Date'] == df.loc[x+1, 'Date']:
#        ...

print(df.duplicated()) # prints True for every row that is a duplicate

df.drop_duplicates(inplace = True)
print(df.to_string)