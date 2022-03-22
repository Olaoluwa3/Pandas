import pandas as pd

grades = pd.Series([87,100,94])

#print(grades)

a = pd.Series(98.6, range(3))



b = grades[0]
c = grades.count()
d = grades.mean()

print(grades.describe())

grades = pd.Series([87,100,94], index=['Wally', 'Eva','Sam'])

grades_dict = {'Wally':87, 'Eva':100, 'Sam':94}

grades_ds = pd.Series(grades_dict)

print(grades_ds)

eva = grades['Eva']
wally = grades.Wally  #dot notation only works with string indexes


e = grades.values


hardware = pd.Series(['Hammer','Saw','Wrench'])
f = hardware.str.contains('a')
g = hardware.str.upper()

#convert a series object to a Python list
hardware_list = hardware.to_list()

#Compare 2 series
ds1 = pd.Series([2,4,6,8,10])
ds2 = pd.Series([1,3,5,7,10])

h = ds1 == ds2
i = ds1 > ds2
j = ds1 < ds2


#list of series
list_of_series = pd.Series([
    ['Red', 'Green', 'White'],
    ['Red', 'Black'],
    ['Yellow']
])

#Make all the elements just one series and reset the index
list_of_series = list_of_series.apply(pd.Series).stack().reset_index(drop=True)

#Sort a series
s = pd.Series(['100','200','python','300.12','400'])
sorted_series = s.sort_values()

#s = pd.Series(['100',200,'python',300.12,'400'])  #causes error. Elements have to be all of the same data type
#sorted_series = s.sort_values()


#Adding to a Series
s = s.append(pd.Series(['500','php'])).reset_index(drop=True)  #Have to use s = 

#Write a Pandas program to calculate the frequency counts of each unique value of a given series.
import random
list1 = [random.randrange(1,10) for i in range (0,100)]
s = pd.Series(list1)
result = s.value_counts()  #shows frequency of each unique number

print()