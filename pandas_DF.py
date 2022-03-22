#Series = one dimensional array
#Dataframe = two dimensional array
    #Each column in a DF is a series




import pandas as pd

grades_dict = {
    'Wally':[87,96,70],
    'Eva':[100,87,90],
    'Sam':[94,77,90],
    'Katie':[100,81,82],
    'Bob':[83,65,85],
}

grades = pd.DataFrame(grades_dict)

grades.index = ['Test1', 'Test2', 'Test3']

print(grades)

eva = grades['Eva']
sam = grades.sample


#Using the loc and iloc methods
test2 = grades.loc['Test2']
test1 = grades.iloc[0]  #Uses integers. Starts from 0


###  - consecutive rows --- can just use a colon
###  - non-consecutive row  --- will need a comma and has to be in a list
#For consecutive rows
test1_thru_test3 = grades.loc['Test1':'Test3']
#For non-consecutive rows
test1_and_test3 = grades.loc[['Test1', 'Test3']]  #Uses the list so 2 brackets

test1_and_test2 = grades.iloc[0:2]  #Does not include the upper index

#View only Eva's and Katie's grades for Test1 and Test2
eva_katie_test1_test2 = grades.loc['Test1':'Test2',['Eva','Katie']]
eva_katie_test1_test2 = grades.loc[:'Test2',['Eva','Katie']]   #python automatically knows to start at the lowest value

#View only Sam's THRU Bob's grades for Test1 and Test3
sam_thru_bob_test1_test3 = grades.loc[['Test1','Test3'],'Sam':'Bob']
sam_thru_bob_test1_test3 = grades.loc[['Test1','Test3'],'Sam':]  #Don't have to list Bob since its the upper limit


#Boolean Indexing
# Select everyone with an A grade
grades_A = grades[grades>=90]

#Create a dataframe for everyone with a B grade
grades_B = grades[(grades>=80) & (grades<90)]

#Create a dataframe for everyone with an A or B grade
grades_A_or_B = grades[(grades>=90) | (grades>=80)]

#Set precision to only 2 decimal places at the pd (panda) level
pd.set_option('precision',2)

#by student
print(grades.describe())

#by test
print(grades.T.describe())  #Transpose it to see by test

#Exercise - Get the average of all the student grades on each test
print(grades.T.mean())

#Sort rows by their indices (Test name)
r_sorted_grades_i = grades.sort_index(ascending=False)  #descending order

#Sort columns by their column names (Student names)
# axis = 1 indicates to sort by column indices
# axis = 0 indicates to sort by row indices

c_sorted_grades_i = grades.sort_index(axis=1)
c_sorted_grades_i = grades.sort_index(axis=1, ascending=False) #Reverse order for column names


print()