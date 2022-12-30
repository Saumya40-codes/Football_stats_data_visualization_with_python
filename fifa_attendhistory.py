import pandas as pd
from pandas import DataFrame
from matplotlib import pyplot as pt

#reading file and converting it in DataFrame
df_data = DataFrame(pd.read_excel('FIFA_history.xlsx'))

#adding host countries names
host_name = []
for i in df_data.Hosts.values:
    host_name.append(i)

attend = []

#adding attendance
for i in df_data.attendance.values:
    attend.append(i)

y = attend

grp = pt.bar(host_name,attend,color=['red','yellow'])
pt.xlabel('Host Country')
pt.ylabel('Total attendance of all matches during the tournament(the given values are in crores)')
pt.title('Total attendance in FIFA WORLD CUP since 1960')
pt.xticks(rotation=90)
pt.show()