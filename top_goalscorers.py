import pandas as pd
from pandas import DataFrame
from matplotlib import pyplot  

#reading the csv file
file_read = pd.read_csv('goalscorers.csv',delimiter=',')
#converting this to the DataFrame
to_df = DataFrame(file_read)

list_names = []
list_x = []

#appending only big players to the list for a better visualization
for i in to_df.scorer.values:
    if(i not in list_names and i in to_df.tbc.values):
        list_names.append(i)


count = 0
list_goals = []

#appending goals scored by the respective player at that index
for i in range(len(list_names)):
    list_x.append(i)
    for j in to_df.scorer.values:
        if(j == list_names[i]):
            count = count + 1
    list_goals.append(count)
    count = 0

#printing the most goals scored and by whom
print("Most goals scored:",to_df['scorer'].value_counts().max())
print("Scored by:",to_df['scorer'].value_counts().idxmax())

#using scatter plot function of pyplot
pyplot.scatter(list_x,list_goals,alpha=0.9,edgecolors=['orange','purple'],label='player names')
pyplot.title("Most International goals scored by big football players(since 1979(approx)) \t\t src:https://kaggle.com")
pyplot.xlabel('This kind of basically shows who scored first')
pyplot.ylabel("Goals scored")

#using annotate function so that i can see player names as labels at the scatter point
for i in range(len(list_names)):
    pyplot.annotate(list_names[i], (list_x[i], list_goals[i]),c='red')
pyplot.show()

