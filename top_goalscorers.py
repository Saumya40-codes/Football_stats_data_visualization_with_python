import pandas as pd
from pandas import DataFrame
from matplotlib import pyplot

file_read = pd.read_csv('goalscorers.csv',delimiter=',')
to_df = DataFrame(file_read)

list_names = []
list_x = []

for i in to_df.scorer.values:
    if(i not in list_names and i in to_df.tbc.values):
        list_names.append(i)


count = 0
list_goals = []

for i in range(len(list_names)):
    list_x.append(i)
    for j in to_df.scorer.values:
        if(j == list_names[i]):
            count = count + 1
    list_goals.append(count)
    count = 0

print(to_df['scorer'].value_counts().max())
print(to_df['scorer'].value_counts().idxmax())

pyplot.scatter(list_x,list_goals,alpha=0.9,edgecolors=['orange','purple'],label='player names')
pyplot.title("Goals scored by big football players(since 1979(approx)) \t\t src:https://kaggle.com")
pyplot.xlabel('This kind of basically shows who scored first')
pyplot.ylabel("Goals scored")
pyplot.style.use('dark_background')
print(to_df.scorer.iloc[0])
pyplot.legend()
for i in range(len(list_names)):
    pyplot.annotate(list_names[i], (list_x[i], list_goals[i]),c='red')
pyplot.show()

#c == colors