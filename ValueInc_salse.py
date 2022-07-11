# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 07:08:39 2022

@author: Mazadur Rahman
"""
import pandas as pd 

# file_name = pd.read_csv('file.csv')   <------ formate 

data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv', sep=';')

#sumary of the data 
data.info()

# play with variables

# string variable
v_str = 'mazedur'

# integer variable
v_int = 1

# flot variavle
v_float = 1.2

# list variavle
v_list = ['apple','banana','mango']

# tuple variavle
v_tuple = ('apple','banana','mango')

# set variavle
v_set = {'apple','banana','mango'}

# dictionary variavle
v_dict = {'name':'mazedur','location':'gazipur','country':'Bangladesh'}

#boolean variavle
V_bool = True
v_bool = False

# Working with calculation
# cost per transtion column colculation

# how to pull out a single column 

# variable = dataframe['column_name']   <------ formate


# TYPE 1
#pull out column and multiply
CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPertranstion = CostPerItem * NumberOfItemsPurchased

# adding a new column in exist dataframe
data['CostPerTransations'] = CostPertranstion

# TYPE 2
# datafrane['new_column_name'] = operation   <------ formate
data['CostPerTransation'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

# sales per transaction 
data['SalcePerTransation'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

# Profit calculation = Sales - cost
data['Profiteperteansation'] = data['SalcePerTransation'] * data['CostPerTransations']

#Markup = (Sales -cost)/cost
data['Markup'] =  (data['SalcePerTransation'] * data['CostPerTransations'] )/ data['CostPerTransations']
 
# Round marking

roundmarkup = round(data['Markup'],2)

data['Markup'] = round(data['Markup'],2)


# Combine data fiels 
my_name = 'Mazedur'+'Rahman'                 # << concatenate <<
my_date = 'Day'+'-'+'Month'+'-'+'Year'

# my_date = data['Day']+'-'+ date['Month']+'-'+ data['Year']   
# << (python can not concatenate two different type of data/variable) <<

# STEP 1
#cheaking particular column data type
# print(datafram_name['column_name'].dtytpe) <------ formate
print(data['Day'].dtype)           # cheak field 1

# STEP 2
#change column data type
day = data['Day'].astype(str)      
print(day.dtype)


print(data['Month'].dtype)         # cheak field 2
print(data['Year'].dtype)          # cheak field 3

year = data['Year'].astype(str)
print(data['Year'].dtype)
print(year.dtype)

# STEP 3
# concatenate all field
my_date = day + '-' + data['Month'] + '-' + year
#adding in dataframe
data['Date'] = my_date

#use iloc to view spacific column/row

# datafram_name.iloc[Row_index, column_index]        <------ formate
data.iloc[2:8, 2:5]

data.iloc[0]     # viwe that in index 0
data.iloc[0:3]   # view only fist 3 rows
data.iloc[-5]    # view last 5 rows

data.head(10)    # fast 5 rows

data.iloc[:,2]      #view all with only column 2
data.iloc[4,2]      #view only row 4 and column 2
data.iloc[2:8, 2:5] # view only row 2 to 8 and column 2 to 5 

# split a single column into multiplre column useing split function
# new_var = column.str.split('sep' , expand = true)  <------ formate

split_col = data['ClientKeywords'].str.split(',', expand = True)

# adding splited column in dataframe with new column name
# next  line is formate 
# datafram_name['NewColumnName'] = variable_name[columnIndexInVariableTable] 
# in this case variable_name = where the old column is split into new column 

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LeanthofContract'] = split_col[2]

#using the replace function
#datafram['column_name'] = datafram ['column'].str.replace('newCha','oldCha')
                                          
data['ClientAge'] = data['ClientAge'].str.replace('[','')
data['LeanthofContract'] = data['LeanthofContract'].str.replace(']','')


# join / marge files 
# bring in a new dataset / import new csv file

sesion = pd.read_csv('value_ine_seasion.csv')

#marging file 
#marge_df = pd.marge(df_old, df_new, on = key) <------ formate 
#     [df = datafram]

data = pd.merge(data, sesion, on = 'Month')


#drokping columns

# df = df.drop('columnName' , axis = 1)
data = data.drop('ClientKeywords', axis = 1)       # drop single column

data = data.drop(['Year','Month','Day'], axis = 1) # drop multi column


#export after cleaning file
data.to_csv('ValuInc_Cleand.csv')
















