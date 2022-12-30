import pandas as pd
from pandas import DataFrame
from matplotlib import pyplot as plt

#reading csv file and converting it to a DataFrame
df_data = DataFrame(pd.read_csv('Attendance Sheet.csv',delimiter=','))

match_name = []
str = ""

#made this just for proper description of who was playing whom
for i in range(len(df_data.Home.values)):
    str = df_data.Home[i]+ ' vs ' + df_data.Away[i]
    match_name.append(str)
    str = ""

attend_count = []

#for total attendance count
for i in df_data.Attendance.values:
    attend_count.append(i)

#using plot function of pyplot
grp = plt.plot(match_name,attend_count,c='orange',linestyle='dashed',marker='o',markerfacecolor='green')
plt.xticks(rotation=90)
plt.title('Attendance during the world cup games    src:https://kaggle.com')
plt.xlabel("Matches")
plt.ylabel('Attendance')
plt.show()

